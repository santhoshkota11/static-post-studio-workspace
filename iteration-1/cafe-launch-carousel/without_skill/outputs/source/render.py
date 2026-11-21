"""Render each 1080x1350 slide in carousel.html to PNG."""
import pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent
NAMES = ["01-cover", "02-fourteen-hours", "03-classic", "04-jaggery-cardamom", "05-kokum-tonic", "06-details"]

with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")
    pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
    pg.goto((HERE / "carousel.html").as_uri(), wait_until="networkidle")
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(600)
    for i, name in enumerate(NAMES, 1):
        pg.locator(f"#s{i}").screenshot(path=str(OUT / f"second-crack-coldbrew-{name}.png"))
        print("saved", name)
    b.close()
