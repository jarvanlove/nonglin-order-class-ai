import re
from pathlib import Path

for day in [f"day{i:02d}" for i in range(4, 7)]:
    path = Path(f"{day}/index.html")
    text = path.read_text(encoding="utf-8")
    original = text
    
    text = text.replace(
        ".card { background: #ffffff; border: 1pt solid #e2e8f0; border-radius: 6pt; padding: 10pt 12pt; }",
        ".card { background: #ffffff; border: 1pt solid #e2e8f0; border-radius: 6pt; padding: 7pt 9pt; }"
    )
    text = text.replace(
        ".card h3 { font-size: 13pt; color: #084E8F; font-weight: 700; margin-bottom: 6pt; }",
        ".card h3 { font-size: 11.5pt; color: #084E8F; font-weight: 700; margin-bottom: 4pt; }"
    )
    text = text.replace(
        ".card p, .card li { font-size: 10pt; color: #333333; line-height: 1.6; }",
        ".card p, .card li { font-size: 9.5pt; color: #333333; line-height: 1.45; }"
    )
    text = text.replace(
        ".content { position: absolute; top: 40pt; bottom: 28pt; left: 0; right: 0; padding: 14pt 28pt; box-sizing: border-box; overflow: hidden; }",
        ".content { position: absolute; top: 40pt; bottom: 28pt; left: 0; right: 0; padding: 10pt 24pt; box-sizing: border-box; overflow: hidden; }"
    )
    text = text.replace(
        ".two-col { display: flex; gap: 14pt; height: calc(100% - 56pt); }",
        ".two-col { display: flex; gap: 10pt; height: calc(100% - 56pt); }"
    )
    text = text.replace(
        ".col { flex: 1; display: flex; flex-direction: column; gap: 8pt; }",
        ".col { flex: 1; display: flex; flex-direction: column; gap: 5pt; }"
    )
    text = text.replace(
        ".col-left { flex: 1; display: flex; flex-direction: column; gap: 8pt; }",
        ".col-left { flex: 1; display: flex; flex-direction: column; gap: 5pt; }"
    )
    text = text.replace(
        ".col-right { flex: 1; display: flex; flex-direction: column; gap: 8pt; }",
        ".col-right { flex: 1; display: flex; flex-direction: column; gap: 5pt; }"
    )
    text = text.replace(
        ".bullet-list li { padding-left: 14pt; position: relative; margin-bottom: 4pt; }",
        ".bullet-list li { padding-left: 14pt; position: relative; margin-bottom: 2pt; }"
    )
    text = text.replace(
        ".hint-box { background: rgba(8,78,143,0.04); border-left: 3pt solid #084E8F; border-radius: 0 4pt 4pt 0; padding: 8pt 10pt; }",
        ".hint-box { background: rgba(8,78,143,0.04); border-left: 3pt solid #084E8F; border-radius: 0 4pt 4pt 0; padding: 5pt 8pt; }"
    )
    text = text.replace(
        ".hint-box p { font-size: 10pt; line-height: 1.5; margin: 0; }",
        ".hint-box p { font-size: 9.5pt; line-height: 1.4; margin: 0; }"
    )
    text = text.replace(
        ".compare-table th { background: #084E8F; color: #ffffff; padding: 5pt 8pt; text-align: left; font-weight: 700; }",
        ".compare-table th { background: #084E8F; color: #ffffff; padding: 3pt 6pt; text-align: left; font-weight: 700; }"
    )
    text = text.replace(
        ".compare-table td { padding: 5pt 8pt; border-bottom: 1pt solid #e2e8f0; color: #333333; }",
        ".compare-table td { padding: 3pt 6pt; border-bottom: 1pt solid #e2e8f0; color: #333333; }"
    )
    text = text.replace(
        ".kicker { display: inline-flex; align-items: center; gap: 8pt; margin-bottom: 6pt; }",
        ".kicker { display: inline-flex; align-items: center; gap: 8pt; margin-bottom: 4pt; }"
    )
    text = text.replace(
        ".page-title { font-size: 24pt; font-weight: 700; color: #084E8F; line-height: 1.2; margin-bottom: 10pt; }",
        ".page-title { font-size: 22pt; font-weight: 700; color: #084E8F; line-height: 1.15; margin-bottom: 6pt; }"
    )
    
    if text != original:
        path.write_text(text, encoding="utf-8")
        print(f"Updated {day}")
    else:
        print(f"No changes {day}")

print("Done")
