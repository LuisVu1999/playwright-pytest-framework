import pytest
import os
from playwright.sync_api import sync_playwright
from helpers.allure_helper import AllureHelper
from helpers.auth import AuthHelper, STORAGE_FILE

BASE_URL = "https://demo.growcrm.io/login"
STORAGE_FILE = "auth.json"
# @pytest.fixture(scope="session")
# def playwright_instance():
#     with sync_playwright() as p:
#         yield p

# @pytest.fixture(scope="session")
# def playwright_context(playwright_instance):
#     browser = playwright_instance.chromium.launch(headless = True)
#     context = browser.new_context(storage_state = "storageState.json")
#     yield context
#     context.close()
#     browser.close()


@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


@pytest.fixture(scope="function")
def page(browser_context):
    page = browser_context.new_page()
    page.goto("https://demo.growcrm.io/projects")
    yield page
    page.close()

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

@pytest.fixture(scope="session")
def auth_context():
    # Nếu storage chưa tồn tại, login và lưu
    if not os.path.exists(STORAGE_FILE):
        AuthHelper.login_and_save_state()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless = True)
        context = browser.new_context(storage_state=STORAGE_FILE)
        page = context.new_page()
        page.goto("https://demo.growcrm.io/home")
        yield page
        context.close()
        browser.close()
    