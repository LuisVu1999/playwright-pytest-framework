# playwright_test2

#chuyen vao env: .venv\Scripts\activate
#Xem report: allure serve allure-results

#Run tcs: Browser + env + run 3 times + run 3 times same time
pytest --env=dev --browser=chromium --reruns 3 -n 3 tests\ui

#Run 3 browser:
import pytest
@pytest.fixture(params=["chromium", "firefox", "webkit"])
def browser_name(request):
    return request.param
terminal: pytest --env=dev -n 3 --reruns 3
