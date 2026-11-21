"""Render each <section class="slide"> in carousel.html to a 1080x1350 PNG."""
import pathlib, sys
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent
html = (HERE / "carousel.html").as_uri()

with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")
    pg = b.new_page(viewport={"width": 1200, "height": 1500}, device_scale_factor=1)
    pg.goto(html, wait_until="networkidle")
    pg.evaluate("document.fonts.ready")
    fonts = pg.evaluate("[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+' '+f.weight)")
    print("fonts loaded:", sorted(set(fonts)))
    for i in range(1, 8):
        el = pg.locator(f"#s{i}")
        path = OUT / f"slide-{i:02d}.png"
        el.screenshot(path=str(path))
        print("wrote", path)
    b.close()
