import os
from cloakbrowser import launch

# Chromium needs an explicit proxy setting in proxy-only environments.
options = {}
if os.environ.get("HTTPS_PROXY"):
    options["proxy"] = {
        "server": os.environ["HTTPS_PROXY"],
        "bypass": "127.0.0.1,localhost",
    }
    options["args"] = ["--license-route=proxy"]

browser = launch(headless=True, **options)
try:
    page = browser.new_page(viewport={"width": 1280, "height": 800})
    response = page.goto("http://127.0.0.1:8000/", wait_until="load")
    assert response is not None and response.status == 200
    assert page.title() == "Release checklist"
    assert page.locator("li").count() == 3
    print("Status:", response.status)
    print("Title:", page.title())
    print("Checklist items:", page.locator("li").count())
    page.screenshot(path="page.png", full_page=True)
finally:
    browser.close()
