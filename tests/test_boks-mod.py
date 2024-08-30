from playwright.sync_api import Playwright, sync_playwright, expect


def test_boks():
    with sync_playwright() as p:
       browser = p.chromium.launch(headless=False)
       page = browser.new_page()

       page.goto("https://www.sinsay.com/ua/uk/")




       browser.close()