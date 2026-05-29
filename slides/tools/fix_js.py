import re
from pathlib import Path

for day in [f"day{i:02d}" for i in range(1, 7)]:
    path = Path(f"slides/{day}/index.html")
    text = path.read_text(encoding="utf-8")
    
    # Fix day01 style
    text = text.replace(
        "document.getElementById('pageIndicator').textContent = (current + 1) + ' / ' + total;",
        "const pi = document.getElementById('pageIndicator'); if(pi) pi.textContent = (current + 1) + ' / ' + total;"
    )
    
    # Fix day02-day06 style
    text = text.replace(
        "document.getElementById('page-num').textContent = n + ' / ' + totalSlides;",
        "const pn = document.getElementById('page-num'); if(pn) pn.textContent = n + ' / ' + totalSlides;"
    )
    
    path.write_text(text, encoding="utf-8")
    print(f"Fixed {day}")
