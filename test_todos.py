from playwright.sync_api import sync_playwright


def test_testcase1_todos():
    with sync_playwright() as p:
       browser = p.chromium.launch(headless=False)
       page = browser.new_page()
       page.goto("https://todomvc.com/examples/react/dist/#/")
       page.get_by_test_id("text-input").click()
       page.get_by_test_id("text-input").fill("1 нотаток")
       page.get_by_test_id("text-input").press("Enter")
       browser.close()


def test_testcase2_todos():
   with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      page = browser.new_page()
      page.goto("https://todomvc.com/examples/react/dist/#/")
      page.get_by_test_id("text-input").click()
      page.get_by_test_id("text-input").fill("1 нотаток")
      page.get_by_test_id("text-input").press("Enter")
      page.get_by_test_id("text-input").fill("2 нотаток")
      page.get_by_test_id("text-input").press("Enter")
      page.get_by_test_id("text-input").fill("3нотаток")
      page.get_by_test_id("text-input").press("Enter")
      page.get_by_test_id("text-input").fill("4 нотаток")
      page.get_by_test_id("text-input").press("Enter")
      browser.close()
def test_testcase3_todos():
   with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      page = browser.new_page()
      page.goto("https://todomvc.com/examples/react/dist/#/")
      page.get_by_test_id("text-input").click()
      page.get_by_test_id("text-input").fill("1 нотаток")
      page.get_by_test_id("text-input").press("Enter")
      page.get_by_test_id("text-input").fill("2 нотаток")
      page.get_by_test_id("text-input").press("Enter")
      page.get_by_test_id("text-input").fill("3нотаток")
      page.get_by_test_id("text-input").press("Enter")
      page.get_by_test_id("text-input").fill("4 нотаток")
      page.get_by_test_id("text-input").press("Enter")
      page.locator("div").filter(has_text="2 нотаток").get_by_test_id("todo-item-toggle").check()
      page.locator("div").filter(has_text="3нотаток").get_by_test_id("todo-item-toggle").check()

      browser.close()
def test_testcase4_todos():
   with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      page = browser.new_page()
      page.goto("https://todomvc.com/examples/react/dist/#/")
      page.get_by_test_id("text-input").click()
      page.get_by_test_id("text-input").fill("1 нотаток")
      page.get_by_test_id("text-input").press("Enter")
      page.get_by_test_id("text-input").fill("2 нотаток")
      page.get_by_test_id("text-input").press("Enter")
      page.get_by_test_id("text-input").fill("3нотаток")
      page.get_by_test_id("text-input").press("Enter")
      page.get_by_test_id("text-input").fill("4 нотаток")
      page.get_by_test_id("text-input").press("Enter")
      page.locator("div").filter(has_text="2 нотаток").get_by_test_id("todo-item-toggle").check()
      page.locator("div").filter(has_text="3нотаток").get_by_test_id("todo-item-toggle").check()
      page.get_by_role("link", name="Completed").click()
      browser.close()
def test_testcase5_todos():
   with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      page = browser.new_page()
      page.goto("https://todomvc.com/examples/react/dist/#/")
      page.get_by_test_id("text-input").click()
      page.get_by_test_id("text-input").fill("1 нотаток")
      page.get_by_test_id("text-input").press("Enter")
      page.get_by_test_id("text-input").fill("2 нотаток")
      page.get_by_test_id("text-input").press("Enter")
      page.get_by_test_id("text-input").fill("3нотаток")
      page.get_by_test_id("text-input").press("Enter")
      page.get_by_test_id("text-input").fill("4 нотаток")
      page.get_by_test_id("text-input").press("Enter")
      page.locator("div").filter(has_text="2 нотаток").get_by_test_id("todo-item-toggle").check()
      page.locator("div").filter(has_text="3нотаток").get_by_test_id("todo-item-toggle").check()
      page.get_by_role("link", name="Completed").click()
      page.get_by_role("link", name="Active").click()
      browser.close()
def test_testcase6_todos():
   with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      page = browser.new_page()
      page.goto("https://todomvc.com/examples/react/dist/#/")
      page.get_by_test_id("text-input").click()
      page.get_by_test_id("text-input").fill("1 нотаток")
      page.get_by_test_id("text-input").press("Enter")
      page.get_by_test_id("text-input").fill("2 нотаток")
      page.get_by_test_id("text-input").press("Enter")
      page.get_by_test_id("text-input").fill("3нотаток")
      page.get_by_test_id("text-input").press("Enter")
      page.get_by_test_id("text-input").fill("4 нотаток")
      page.get_by_test_id("text-input").press("Enter")
      page.locator("div").filter(has_text="2 нотаток").get_by_test_id("todo-item-toggle").check()
      page.locator("div").filter(has_text="3нотаток").get_by_test_id("todo-item-toggle").check()
      page.get_by_role("link", name="Completed").click()
      page.get_by_role("link", name="Active").click()
      page.get_by_role("link", name="All").click()
      browser.close()

def test_testcase7_todos():
   with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      page = browser.new_page()
      page.goto("https://todomvc.com/examples/react/dist/#/")
      page.get_by_test_id("text-input").click()
      page.get_by_test_id("text-input").fill("1 нотаток")
      page.get_by_test_id("text-input").press("Enter")
      page.get_by_test_id("text-input").fill("2 нотаток")
      page.get_by_test_id("text-input").press("Enter")
      page.get_by_test_id("text-input").fill("3нотаток")
      page.get_by_test_id("text-input").press("Enter")
      page.get_by_test_id("text-input").fill("4 нотаток")
      page.get_by_test_id("text-input").press("Enter")
      page.locator("div").filter(has_text="2 нотаток").get_by_test_id("todo-item-toggle").check()
      page.locator("div").filter(has_text="3нотаток").get_by_test_id("todo-item-toggle").check()
      page.get_by_role("link", name="Completed").click()
      page.get_by_role("link", name="Active").click()
      page.get_by_role("link", name="All").click()
      page.get_by_role("button", name="Clear completed").click()
      browser.close()
