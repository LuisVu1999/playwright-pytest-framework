import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://demo.growcrm.io/login"

# @pytest.fixture(scope="session")
# def playwright_instance():
#     with sync_playwright() as p:
#         yield p

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(BASE_URL)
    yield page
    context.close()
    