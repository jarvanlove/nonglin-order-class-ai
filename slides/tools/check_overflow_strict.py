"""Strict overflow check: compare scrollHeight vs clientHeight of content areas."""
from playwright.sync_api import sync_playwright
from pathlib import Path

DAYS = [f"day{i:02d}" for i in range(1, 7)]

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(viewport={"width": 1280, "height": 720})
    page = context.new_page()

    for day in DAYS:
        src = Path(f"{day}/index.html").resolve()
        if not src.exists():
            continue
        page.goto(f"file:///{src.as_posix()}")
        page.wait_for_timeout(2000)

        total = page.evaluate("() => document.querySelectorAll('.slide').length")
        bad = []
        for i in range(total):
            page.evaluate(f"if(typeof showSlide==='function') showSlide({i+1}); else if(typeof show==='function') show({i});")
            page.wait_for_timeout(600)

            # Check content area scrollHeight vs clientHeight
            overflow = page.evaluate("""() => {
                const slide = document.querySelector('.slide.active');
                if (!slide) return 'no active slide';
                const content = slide.querySelector('.slide-content, .content');
                if (!content) return 'no content area';
                if (content.scrollHeight > content.clientHeight + 2) {
                    return {type:'content', sh: content.scrollHeight, ch: content.clientHeight, diff: content.scrollHeight - content.clientHeight};
                }
                // Also check any child that visually protrudes
                const cr = content.getBoundingClientRect();
                const slideRect = slide.getBoundingClientRect();
                const kids = content.querySelectorAll('*');
                for (const k of kids) {
                    const r = k.getBoundingClientRect();
                    if (r.height > 0 && r.bottom > slideRect.bottom + 1) {
                        return {type:'child', tag:k.tagName, cls:k.className, childBottom:r.bottom, slideBottom:slideRect.bottom};
                    }
                }
                return null;
            }""")
            if overflow:
                bad.append((i+1, overflow))

        if bad:
            print(f"[{day}] {len(bad)}/{total} OVERFLOW:")
            for num, info in bad:
                if info.get('type') == 'content':
                    print(f"  Slide {num}: content overflow scrollHeight={info['sh']:.0f} > clientHeight={info['ch']:.0f} (diff={info['diff']:.0f})")
                else:
                    print(f"  Slide {num}: {info.get('tag','')}.{info.get('cls','')} bottom={info.get('childBottom',0):.0f} > slide={info.get('slideBottom',0):.0f}")
        else:
            print(f"[{day}] OK {total}/{total}")

    browser.close()
