"""Check for content overflow in slides."""
import asyncio
import re
from pathlib import Path

from playwright.async_api import async_playwright
from PIL import Image


SLIDES_DIR = Path(__file__).parent.resolve()
DAYS = [f"day{i:02d}" for i in range(1, 7)]


def extract_slide_title(html: str, slide_idx: int) -> str:
    """Extract title from slide HTML by index."""
    # Find all slide divs
    pattern = r'<div class="slide[^"]*"[^>]*>(.*?)</div>\s*(?=<div class="slide|<script|$)'
    slides = re.findall(pattern, html, re.DOTALL)
    if slide_idx >= len(slides):
        return "Unknown"
    slide_html = slides[slide_idx]
    # Try h1/h2/h3
    for tag in ['h1', 'h2', 'h3']:
        m = re.search(rf'<{tag}[^>]*>(.*?)</{tag}>', slide_html, re.DOTALL)
        if m:
            return re.sub(r'<[^>]+>', '', m.group(1)).strip()
    # Try slide-title class
    m = re.search(r'class="slide-title"[^>]*>(.*?)</', slide_html, re.DOTALL)
    if m:
        return re.sub(r'<[^>]+>', '', m.group(1)).strip()
    return "Unknown"


async def check_day(day_dir: Path):
    index_html = day_dir / "index.html"
    if not index_html.exists():
        return []

    results = []
    html_content = index_html.read_text(encoding='utf-8')

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 720})

        file_url = f"file:///{index_html.resolve().as_posix()}"
        await page.goto(file_url, wait_until="networkidle")
        await asyncio.sleep(1)

        slide_count = await page.evaluate("""() => document.querySelectorAll('.slide').length""")

        for i in range(slide_count):
            # Activate slide
            await page.evaluate(f"""() => {{
                document.querySelectorAll('.slide').forEach((s, idx) => {{
                    s.classList.toggle('active', idx === {i});
                }});
            }}""")
            await asyncio.sleep(0.8)

            # JS bounding box overflow check - only check direct children of .slide-content
            overflow_info = await page.evaluate("""() => {
                const slide = document.querySelector('.slide.active');
                if (!slide) return [];
                const slideRect = slide.getBoundingClientRect();
                const issues = [];

                // Find the content container
                const content = slide.querySelector('.slide-content') || slide.querySelector('.content') || slide;
                const elements = content.querySelectorAll('*');

                for (const el of elements) {
                    const style = window.getComputedStyle(el);
                    if (style.display === 'none' || style.visibility === 'hidden') continue;
                    const rect = el.getBoundingClientRect();
                    if (rect.width === 0 || rect.height === 0) continue;

                    // Skip elements that are intentionally positioned outside (like decorative shapes)
                    const pos = style.position;
                    if (pos === 'fixed' || pos === 'absolute') {
                        // Check if it's a decorative element with low opacity or z-index
                        const opacity = parseFloat(style.opacity);
                        const zIndex = parseInt(style.zIndex) || 0;
                        if (opacity < 0.5 || zIndex < 0) continue;
                    }

                    const overflowRight = rect.right > slideRect.right + 2;
                    const overflowBottom = rect.bottom > slideRect.bottom + 2;
                    const overflowLeft = rect.left < slideRect.left - 2;
                    const overflowTop = rect.top < slideRect.top - 2;

                    if (overflowRight || overflowBottom || overflowLeft || overflowTop) {
                        issues.push({
                            tag: el.tagName.toLowerCase(),
                            className: el.className || '',
                            text: el.textContent ? el.textContent.trim().substring(0, 40) : '',
                            overflowRight, overflowBottom, overflowLeft, overflowTop,
                            rect: {left: rect.left, top: rect.top, right: rect.right, bottom: rect.bottom},
                            slideRect: {left: slideRect.left, top: slideRect.top, right: slideRect.right, bottom: slideRect.bottom}
                        });
                    }
                }
                return issues;
            }""")

            title = extract_slide_title(html_content, i)
            issues = []

            if overflow_info:
                if any(o['overflowRight'] for o in overflow_info):
                    issues.append("右侧内容超出")
                if any(o['overflowBottom'] for o in overflow_info):
                    issues.append("底部内容超出")
                if any(o['overflowLeft'] for o in overflow_info):
                    issues.append("左侧内容超出")
                if any(o['overflowTop'] for o in overflow_info):
                    issues.append("顶部内容超出")

            if issues:
                results.append({
                    "day": day_dir.name,
                    "slide_num": i + 1,
                    "title": title,
                    "issues": issues,
                    "overflow_count": len(overflow_info),
                })

        await browser.close()

    return results


async def main():
    all_results = {}
    for day in DAYS:
        day_dir = SLIDES_DIR / day
        print(f"Checking {day}...")
        if day_dir.exists():
            results = await check_day(day_dir)
            all_results[day] = results
            if not results:
                print(f"  {day}: 无溢出问题")
            else:
                print(f"  {day}: 发现 {len(results)} 个问题slide")
        else:
            print(f"  {day}: 目录不存在")
            all_results[day] = []

    # Write report to file with UTF-8 encoding
    report_path = SLIDES_DIR / "overflow_report.md"
    lines = []
    lines.append("# 幻灯片内容溢出检查报告")
    lines.append("")
    lines.append("画布尺寸: 960pt x 540pt")
    lines.append("Viewport: 1280 x 720")
    lines.append("")

    total_issues = 0
    for day in DAYS:
        results = all_results.get(day, [])
        lines.append(f"## {day.upper()}")
        if not results:
            lines.append("- 无溢出问题")
        else:
            total_issues += len(results)
            for r in results:
                lines.append(f"")
                lines.append(f"### Slide {r['slide_num']:02d}: {r['title']}")
                for issue in r['issues']:
                    lines.append(f"- **{issue}**")
                if r['overflow_count'] > 0:
                    lines.append(f"- 详情: {r['overflow_count']} 个元素溢出画布边界")
        lines.append("")

    lines.append("---")
    lines.append(f"总计: {total_issues} 个 slide 存在溢出问题")

    report_path.write_text("\n".join(lines), encoding='utf-8')
    print(f"\n报告已保存至: {report_path}")


if __name__ == "__main__":
    from io import BytesIO
    asyncio.run(main())
