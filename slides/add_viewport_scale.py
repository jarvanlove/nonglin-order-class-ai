import re
from pathlib import Path

for day in [f"day{i:02d}" for i in range(2, 7)]:
    path = Path(f"slides/{day}/index.html")
    text = path.read_text(encoding="utf-8")
    original = text

    # 1. Change html,body CSS from absolute centering to flex centering
    text = text.replace(
        "html, body { width: 100%; height: 100%; overflow: hidden; font-family: \"Microsoft YaHei\", \"PingFang SC\", sans-serif; background: #F8FBFF; }",
        "html, body { width: 100vw; height: 100vh; margin: 0; padding: 0; overflow: hidden; font-family: \"Microsoft YaHei\", \"PingFang SC\", sans-serif; background: #1a1a1a; display: flex; align-items: center; justify-content: center; }"
    )

    # 2. Change .slide CSS: remove absolute centering, add relative positioning
    text = text.replace(
        ".slide { width: 960pt; height: 540pt; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); display: none; overflow: hidden; }",
        ".slide { width: 960pt; height: 540pt; position: relative; display: none; overflow: hidden; box-shadow: 0 8pt 32pt rgba(0,0,0,0.3); }"
    )

    # 3. Add .deck-container and .slide-wrapper CSS after .slide.active rule
    old_rule = ".slide.active { display: block; }"
    new_rule = """.slide.active { display: block; }
  .deck-container { width: 100vw; height: 100vh; display: flex; align-items: center; justify-content: center; }
  .slide-wrapper { transform-origin: center center; transition: transform 0.2s ease; }"""
    text = text.replace(old_rule, new_rule)

    # 4. Wrap all <section class="slide"...> elements in deck-container + slide-wrapper
    # Find the first slide and the last slide
    first_slide = text.find('<section class="slide"')
    last_slide_end = text.rfind('</section>') + len('</section>')

    if first_slide != -1 and last_slide_end != -1:
        before = text[:first_slide]
        slides_html = text[first_slide:last_slide_end]
        after = text[last_slide_end:]

        # Insert wrapper
        wrapped = f'<div class="deck-container"><div class="slide-wrapper" id="slideWrapper">\n{slides_html}\n  </div></div>'
        text = before + wrapped + after

    # 5. Add resize JS before the existing showSlide function or at the end of the first <script> block
    resize_js = """
    // Viewport scaling
    function resizeSlides() {
      const wrapper = document.getElementById('slideWrapper');
      if (!wrapper) return;
      const vw = window.innerWidth;
      const vh = window.innerHeight;
      const sw = 960 * 1.333; // 960pt ≈ 1280px
      const sh = 540 * 1.333; // 540pt ≈ 720px
      const scale = Math.min(vw / sw, vh / sh);
      wrapper.style.transform = 'scale(' + scale + ')';
    }
    window.addEventListener('resize', resizeSlides);
    resizeSlides();
"""

    # Find the first <script> block and inject resize function after it starts
    script_start = text.find('<script>')
    if script_start != -1:
        insert_pos = script_start + len('<script>')
        text = text[:insert_pos] + resize_js + text[insert_pos:]

    if text != original:
        path.write_text(text, encoding="utf-8")
        print(f"Updated {day}")
    else:
        print(f"No changes {day}")

print("Done")
