import re
from pathlib import Path

SLIDES_DIR = Path("slides")
DAYS = [f"day{i:02d}" for i in range(1, 7)]

for day in DAYS:
    path = SLIDES_DIR / day / "index.html"
    if not path.exists():
        print(f"Skip {day}: not found")
        continue
    
    text = path.read_text(encoding="utf-8")
    original = text
    
    # 1. Remove nav-hint (day01 style)
    text = re.sub(r'\n?<div class="nav-hint">.*?</div>\n?', '\n', text, flags=re.DOTALL)
    
    # 2. Remove external nav buttons and page-indicator (day02-day06 style)
    # Remove nav-btn and page-indicator blocks at the end of file
    text = re.sub(
        r'\n?<button class="nav-btn" onclick="prevSlide\(\)">上一页</button>\n',
        '\n',
        text
    )
    text = re.sub(
        r'\n?<button class="nav-btn" onclick="nextSlide\(\)">下一页</button>\n',
        '\n',
        text
    )
    text = re.sub(
        r'\n?<div class="page-indicator"><span id="page-num">.*?</span></div>\n',
        '\n',
        text
    )
    
    # 3. Simplify slide-footer content
    # Pattern: <div class="slide-footer">\n    <p>LEFT_TEXT</p>\n    <p>... / ...</p>\n  </div>
    # Replace with only the page number, right-aligned
    def simplify_footer(m):
        inner = m.group(1)
        # Find the page number pattern (e.g., "2 / 18" or "Day 1 · 2 / 18")
        page_match = re.search(r'<p>(?:Day \d+ · )?(\d+ / \d+)</p>', inner)
        if page_match:
            page_num = page_match.group(1)
            return f'<div class="slide-footer">\n    <p style="margin-left:auto;">{page_num}</p>\n  </div>'
        return m.group(0)
    
    text = re.sub(
        r'<div class="slide-footer">(.*?)</div>',
        simplify_footer,
        text,
        flags=re.DOTALL
    )
    
    if text != original:
        path.write_text(text, encoding="utf-8")
        print(f"Updated {day}")
    else:
        print(f"No changes {day}")

print("Done")
