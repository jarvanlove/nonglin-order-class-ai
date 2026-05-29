"""Strict overflow check v3 - handles multiple content class names."""
from playwright.sync_api import sync_playwright
from pathlib import Path

DAYS = [f"day{i:02d}" for i in range(1, 7)]
CONTENT_SELECTORS = ['.slide-content', '.content', '.obj-content', '.intro-content']

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(viewport={"width": 1280, "height": 720})
    page = context.new_page()

    for day in DAYS:
        src = Path(f"slides/{day}/index.html").resolve()
        page.goto(f"file:///{src.as_posix()}")
        page.wait_for_timeout(2000)
        total = page.evaluate("() => document.querySelectorAll('.slide').length")
        bad = []
        for i in range(total):
            # Try 0-based first (day01), then 1-based (day02-06)
            page.evaluate(f"if(typeof showSlide==='function') showSlide({i}); else if(typeof show==='function') show({i});")
            page.wait_for_timeout(400)
            page.evaluate(f"if(typeof showSlide==='function') showSlide({i+1}); else if(typeof show==='function') show({i});")
            page.wait_for_timeout(400)

            overflow = page.evaluate("""() => {
                const slide = document.querySelector('.slide.active');
                if (!slide) return 'no active slide';
                const selectors = ['.slide-content', '.content', '.obj-content', '.intro-content', '.end-content'];
                let content = null;
                for (const s of selectors) {
                    content = slide.querySelector(s);
                    if (content) break;
                }
                if (!content) return 'no content area';
                if (content.scrollHeight > content.clientHeight + 2) {
                    return {type:'content', sh: content.scrollHeight, ch: content.clientHeight, diff: content.scrollHeight - content.clientHeight};
                }
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
            real = [b for b in bad if isinstance(b[1], dict)]
            nocontent = [b for b in bad if not isinstance(b[1], dict)]
            if real:
                print(f"[{day}] {len(real)}/{total} REAL OVERFLOW:")
                for num, info in real:
                    if info.get('type') == 'content':
                        print(f"  Slide {num}: scrollHeight={info['sh']:.0f} > clientHeight={info['ch']:.0f} (diff={info['diff']:.0f})")
                    else:
                        print(f"  Slide {num}: {info.get('tag','')}.{info.get('cls','')} bottom={info.get('childBottom',0):.0f} > slide={info.get('slideBottom',0):.0f}")
            if nocontent:
                print(f"[{day}] {len(nocontent)}/{total} no-content slides (cover/end/etc): {[b[0] for b in nocontent]}")
        else:
            print(f"[{day}] OK {total}/{total}")
    browser.close()
