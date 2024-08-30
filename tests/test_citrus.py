
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.ctrs.com.ua/")
    page.get_by_role("button", name="Увійти").click()
    page.get_by_role("button", name="Увійти по email").click()
    page.get_by_placeholder("Email").fill("stixset@gmail.com")
    page.get_by_role("button", name="Далі").click()
    #  Пароль не вірний
    page.locator("input[name=\"password\"]").fill("1234")
    page.locator("#portal-root").get_by_role("button", name="Увійти").click()
    error_message = page.locator(".Input-module__assistiveText___1RxmM")
    expect(error_message).to_be_visible()
    page.screenshot(path="screenshot_Fail.png")
    #  Пароль вірний
    page.locator("input[name=\"password\"]").fill("12345")
    page.locator("#portal-root").get_by_role("button", name="Увійти").click()
    page.screenshot(path="screenshot_Try.png")
    context.close()
    browser.close()

def test_testcase():
    with sync_playwright() as playwright:
        run(playwright)