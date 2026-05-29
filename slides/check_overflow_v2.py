"""Check for content overflow in slides - refined version.

This script checks if any content inside .slide-content overflows the content bounds,
which would cause clipping due to overflow: hidden.
It only reports the TOPMOST overflowing element in each branch to avoid nested duplicates.
"""
import asyncio
import re
from pathlib import Path

from playwright.async_api import async_playwright


SLIDES_DIR = Path(__file__).parent.resolve()
DAYS = [f"day{i:02d}" for i in range(1, 7)]


def extract_slide_title(html: str, slide_idx: int) -> str:
    """Extract title from slide HTML by index."""
    pattern = r'<section class="slide[^"]*"[^>]*>(.*?)</section>'
    slides = re.findall(pattern, html, re.DOTALL)
    if slide_idx >= len(slides):
        return "Unknown"
    slide_html = slides[slide_idx]
    for tag in ['h1', 'h2', 'h3']:
        m = re.search(rf'<{tag}[^>]*>(.*?)</{tag}>', slide_html, re.DOTALL)
        if m:
            return re.sub(r'<[^>]+>', '', m.group(1)).strip()
    m = re.search(r'class="slide-title"[^>]*>(.*?)</', slide_html, re.DOTALL)
    if m:
        return re.sub(r'<[^>]+>', '', m.group(1)).strip()
    return "Unknown"


def generate_fix_recommendation(overflows: list, title: str) -> list:
    """Generate fix recommendations based on overflow patterns."""
    recs = []
    has_bottom_overflow = any(o.get('overflowBottom') for o in overflows)
    has_top_overflow = any(o.get('overflowTop') for o in overflows)
    has_right_overflow = any(o.get('overflowRight') for o in overflows)

    if has_bottom_overflow:
        recs.append("底部内容溢出：减少内容量、缩小间距或字体，或将部分内容移至下一页")
    if has_top_overflow:
        recs.append("顶部内容溢出：检查是否有元素定位超出内容区上方")
    if has_right_overflow:
        recs.append("右侧内容溢出：缩小列宽或减少列数，检查固定宽度元素")

    # Look for specific patterns
    for o in overflows:
        text = o.get('text', '')
        if 'aspect-ratio' in text or '视频' in text or 'img' in text.lower():
            recs.append("建议：缩小图片/视频占位区域尺寸，或调整 aspect-ratio")
        if 'grid-' in text or len([x for x in overflows if x.get('overflowBottom')]) > 2:
            recs.append("建议：卡片/网格内容过多，考虑减少卡片数量或改为横向滚动布局")

    # Deduplicate while preserving order
    seen = set()
    unique_recs = []
    for r in recs:
        if r not in seen:
            seen.add(r)
            unique_recs.append(r)

    return unique_recs[:3]


async def check_day(day_dir: Path):
    index_html = day_dir / "index.html"
    if not index_html.exists():
        return []

    results = []
    html_content = index_html.read_text(encoding='utf-8')

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 720})

        file_url = f"http://127.0.0.1:8768/{day_dir.relative_to(SLIDES_DIR.parent).as_posix()}/index.html"
        await page.goto(file_url, wait_until="networkidle")
        await asyncio.sleep(1)

        slide_count = await page.evaluate("""() => document.querySelectorAll('.slide').length""")

        for i in range(slide_count):
            await page.evaluate(f"""() => {{
                document.querySelectorAll('.slide').forEach((s, idx) => {{
                    s.classList.toggle('active', idx === {i});
                }});
            }}""")
            await asyncio.sleep(0.8)

            overflow_info = await page.evaluate("""() => {
                const slide = document.querySelector('.slide.active');
                if (!slide) return [];
                const content = slide.querySelector('.slide-content') || slide.querySelector('.content') || slide;
                const contentRect = content.getBoundingClientRect();
                const topmostOverflows = [];

                const findOverflows = (el, parentOverflows) => {
                    const style = window.getComputedStyle(el);
                    if (style.display === 'none' || style.visibility === 'hidden') return false;
                    const rect = el.getBoundingClientRect();
                    if (rect.width === 0 || rect.height === 0) return false;

                    const overflowBottom = rect.bottom > contentRect.bottom + 2;
                    const overflowTop = rect.top < contentRect.top - 2;
                    const overflowRight = rect.right > contentRect.right + 2;
                    const overflowLeft = rect.left < contentRect.left - 2;
                    const overflows = overflowBottom || overflowTop || overflowRight || overflowLeft;

                    if (overflows && !parentOverflows) {
                        topmostOverflows.push({
                            tag: el.tagName.toLowerCase(),
                            className: el.className || '',
                            text: el.textContent ? el.textContent.trim().substring(0, 80) : '',
                            overflowBottom, overflowTop, overflowRight, overflowLeft
                        });
                    }

                    for (const child of el.children) {
                        findOverflows(child, parentOverflows || overflows);
                    }
                    return overflows;
                };

                for (const child of content.children) {
                    findOverflows(child, false);
                }

                return topmostOverflows;
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
                recs = generate_fix_recommendation(overflow_info, title)
                results.append({
                    "day": day_dir.name,
                    "slide_num": i + 1,
                    "title": title,
                    "issues": issues,
                    "overflow_count": len(overflow_info),
                    "overflow_elements": overflow_info,
                    "recommendations": recs
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

    report_path = SLIDES_DIR / "overflow_report_v2.md"
    lines = []
    lines.append("# 幻灯片内容溢出检查报告（修正版）")
    lines.append("")
    lines.append("画布尺寸: 960pt x 540pt")
    lines.append("Viewport: 1280 x 720")
    lines.append("检测逻辑: 仅检查 `.slide-content` 内最顶层溢出元素，避免嵌套元素重复报告")
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
                lines.append(f"- 详情: {r['overflow_count']} 个顶层元素溢出内容区")
                for el in r['overflow_elements']:
                    tag = el['tag']
                    cls = f".{el['className']}" if el['className'] else ''
                    text = el['text'].replace('\n', ' ').strip()
                    if len(text) > 40:
                        text = text[:40] + "..."
                    lines.append(f"  - `<{tag}{cls}>`: {text}")
                if r['recommendations']:
                    lines.append("- **修复建议**:")
                    for rec in r['recommendations']:
                        lines.append(f"  - {rec}")
        lines.append("")

    lines.append("---")
    lines.append(f"总计: {total_issues} 个 slide 存在溢出问题")

    report_path.write_text("\n".join(lines), encoding='utf-8')
    print(f"\n报告已保存至: {report_path}")


if __name__ == "__main__":
    asyncio.run(main())
