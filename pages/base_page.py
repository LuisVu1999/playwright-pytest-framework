from playwright.sync_api import Page
import time

class BasePage:
    def __init__(self, page : Page):
        self.page = page
    
    def navigate(self, url : str):
        self.page.goto(url)
        
    def click(self, locator: str):
        self.page.locator(locator).click()

    def fill(self, locator: str, text: str):
        self.page.locator(locator).fill(text)

    def is_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()
    
    def wait_thread_sleep(self, seconds: float):
        time.sleep(seconds)