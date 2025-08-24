from playwright.sync_api import Page
import time

class BasePage:
    def __init__(self, page : Page):
        self.page = page
    
    def navigate(self, url : str):
        self.page.goto(url)
        
    def click(self, locator: str):
        self.page.click(locator)

    def fill(self, locator: str, text: str):
        self.page.fill(locator, text)

    def is_visible(self, locator: str) -> bool:
        return self.page.is_visible(locator)
    
    def wait_thread_sleep(self, seconds: float):
        time.sleep(seconds)

    def wait_for_load_page (self):
        self.page.wait_for_load_state("networkidle")

    def keyboard (self, key : str):
        self.page.keyboard.press(key)

    def assert_text (self, locator: str, expected_result: str, message = ""):
        actual_result = self.page.inner_text(locator)
        assert actual_result == expected_result, (message or f"Text mismatch. Expected: '{expected_result}', but got: '{actual_result}'")

    def assert_visible(self, locator: str, message = ""):
        assert self.page.is_visible(locator), message or f"Element '{locator}' not visible"