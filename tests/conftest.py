import pytest
from playwright.sync_api import sync_playwright
from helpers.allure_helper import AllureHelper

BASE_URL = "https://demo.growcrm.io/login"

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless = True)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(BASE_URL)
    yield page
    context.close()

# --- Hook bắt lỗi để attach Allure ---
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            AllureHelper.attach_screenshot(page, "Failed Screenshot")
            AllureHelper.attach_text("URL when failed", page.url)
    