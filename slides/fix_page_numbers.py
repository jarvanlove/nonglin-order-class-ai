"""
Fix footer page numbers in all slide HTML files.
"""
import re
from pathlib import Path
import glob

slides_dir = Path(__file__).parent

# Group files by day
days = {}
for f in sorted(slides_dir.glob("day*.html")):
    name = f.name
    if not re.match(r"day\d{2}-\d{2,3}-", name):
        continue
    day_prefix = name.split("-")[0]
    days.setdefault(day_prefix, []).append(f)

for day, files in sorted(days.items()):
    files.sort(key=lambda f: f.name)
    total = len(files)
    for i, f in enumerate(files, 1):
        content = f.read_text(encoding="utf-8")
        # Replace any <p>X / Y</p> with <p>i / total</p>
        # Only match patterns that look like page numbers (digits / digits)
        new_content, count = re.subn(
            r"<p>\d+\s*/\s*\d+</p>",
            f"<p>{i} / {total}</p>",
            content
        )
        if count > 0 and new_content != content:
            f.write_text(new_content, encoding="utf-8")
            print(f"[{day}] {f.name}: -> {i} / {total}")
        else:
            # Maybe no footer number found, add a warning
            if "slide-footer" in content and f"{i} / {total}" not in content:
                print(f"[{day}] {f.name}: WARNING - no page number pattern found")

print(f"\nDone. Processed {sum(len(v) for v in days.values())} slides across {len(days)} days.")
