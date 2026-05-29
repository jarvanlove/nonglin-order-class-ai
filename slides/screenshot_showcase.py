from playwright.sync_api import sync_playwright
import os

slides = [
    ("day01-cover.html", "showcase-cover.png"),
    ("day01-knowledge.html", "showcase-knowledge.png"),
]

base = os.path.dirname(os.path.abspath(__file__))

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 720})
    for src, dst in slides:
        path = os.path.join(base, src).replace("\\", "/")
        page.goto(f"file:///{path}")
        page.wait_for_timeout(2000)
        out = os.path.join(base, dst)
        page.screenshot(path=out, full_page=True)
        print(f"Saved {out}")
    browser.close()
