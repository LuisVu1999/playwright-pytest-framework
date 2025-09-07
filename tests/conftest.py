import pytest
import time
import json
from playwright.sync_api import sync_playwright
from helpers.allure_helper import AllureHelper
from helpers.auth import AuthHelper, STORAGE_FILE
from tests.api.helpers.api_user import api_create_user, api_delete_user
from tests.api.helpers.api_template import api_create_template, api_delete_template
from tests.api.helpers.api_project import api_create_project
from tests.api.helpers.api_client import api_create_client, api_delete_client
from tests.api.helpers.api_task import api_create_task, api_delete_task
from config import ConfigUrl, BrowserConfig, Paths, ENVIRONMENTS

#Browser list
BROWSER = ["chromium", "firefox", "webkit"]

STORAGE_FILE = Paths.STORAGE_FILE

def pytest_addoption(parser):
    """Thêm CLI option: chọn env, browser"""
    parser.addoption("--env", action="store", default="dev", help="dev/staging/prod")
    parser.addoption("--browser-name", action="store", default="chromium", help="chromium/firefox/webkit")

@pytest.fixture
def env_config(request):
    env_name = request.config.getoption("--env")
    return ENVIRONMENTS[env_name]

@pytest.fixture
def browser_name(request):
    return request.config.getoption("--browser-name")

@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = BrowserConfig.HEADLESS)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


@pytest.fixture(scope="function")
def page_logout(browser_context):
    page = browser_context.new_page()
    page.goto(ConfigUrl.BASE_URL)
    yield page
    page.close()

# --- Hook bắt lỗi để attach Allure ---
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(scope="function")
def page_with_video(auth_context, request):
    page = auth_context.new_page(record_video_dir = "videos/")
    page.goto(ConfigUrl.BASE_URL)
    yield page
    video_path = page.video.path()
    page.close()
    #attach video to allure
    if video_path:
        AllureHelper.attach_video(video_path, name=f"{request.node.name}_video")

@pytest.fixture(scope="session")
def auth_context(browser_name):
    # Nếu storage chưa tồn tại, login và lưu
    AuthHelper.ensure_logged_in()
    with sync_playwright() as p:
        browser_type = getattr(p, browser_name)
        browser = browser_type.launch(headless = BrowserConfig.HEADLESS)
        context = browser.new_context(storage_state=STORAGE_FILE)
        context.set_default_timeout(BrowserConfig.DEFAULT_TIMEOUT)              # 60s cho mọi action
        context.set_default_navigation_timeout(BrowserConfig.DEFAULT_TIMEOUT)
        yield context
        context.close()
        browser.close()

@pytest.fixture
def page(auth_context, request):
    """Page luôn record video (để lấy khi fail)"""
    page = auth_context.new_page(record_video_dir="videos/")
    page.goto(ConfigUrl.BASE_URL)
    yield page
    # Always capture screenshot
    AllureHelper.attach_screenshot(page, f"{request.node.name}_screenshot")
    AllureHelper.attach_text("Final URL", page.url)

    video_path = page.video.path() if page.video else None
    # Only attach video if failed
    if request.node.rep_call.failed and video_path:
        AllureHelper.attach_video(video_path, name=f"{request.node.name}_video")

    page.close()

@pytest.fixture
def user_fixture(page):
    user_id, create_response, data = api_create_user(page)
    assert create_response.ok, "Cannot create user"
    yield user_id, data
    if user_id:
        delete_response = api_delete_user(page, user_id)

@pytest.fixture
def client_fixture(page):
    client_id, create_response, data = api_create_client(page)
    assert create_response.ok, "Cannot create client"
    yield client_id, data
    if client_id:
        delete_response = api_delete_client(page, client_id)

@pytest.fixture
def template_fixture(page):
    template_id, create_response = api_create_template(page)
    assert create_response.ok, "Cannot create template"
    yield template_id
    if template_id:
        delete_response = api_delete_template(page, template_id)

@pytest.fixture
def project_fixture(page):
    template_id, response, data = api_create_project(page)
    assert response.ok, "Cannot create project"
    yield template_id, data

@pytest.fixture
def task_fixture(page):
    task_id, response = api_create_task(page)
    assert response.ok, "Cannot create task"
    yield task_id
    if task_id:
        delete_response = api_delete_task(page, task_id)
    
def pytest_runtest_teardown(item, nextitem):
    time.sleep(3)

