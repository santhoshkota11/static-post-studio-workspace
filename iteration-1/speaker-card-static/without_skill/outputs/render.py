import sys, pathlib
from playwright.sync_api import sync_playwright
here = pathlib.Path(__file__).parent
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")
    pg = b.new_page(viewport={"width":1080,"height":1350}, device_scale_factor=1)
    pg.goto((here/"speaker-card.html").as_uri(), wait_until="networkidle")
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(500)
    pg.screenshot(path=str(here/"pixel-chai-vol4-speaker-1080x1350.png"))
    b.close()
