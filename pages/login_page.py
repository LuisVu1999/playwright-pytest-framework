from pages.base_page import BasePage
from pages.locators.login import LoginLocator

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def login(self, username: str, password: str):
        self.navigate("https://demo.growcrm.io/login")
        self.fill(LoginLocator.USERNAME_INPUT, "")
        self.fill(LoginLocator.USERNAME_INPUT, username)
        self.fill(LoginLocator.PASSWORD_INPUT, "")
        self.fill(LoginLocator.PASSWORD_INPUT, password)
        self.click(LoginLocator.SUBMIT_BUTTON)
        self.is_visible(LoginLocator.PAGE_TITLE)
        #self.wait_thread_sleep(3)

    def forgot_password(self, email: str, reset_successfully_text: str):
        #1. Click on forgot password
        self.click(LoginLocator.FORGOT_PASSWORD)
        self.fill(LoginLocator.USERNAME_INPUT, email)
        self.click(LoginLocator.FORGOT_PASSWORD_BUTTON)
        self.assert_text_contain(LoginLocator.SUCCESSFULLY_RESET, reset_successfully_text)

    def logout(self, signin_text: str):
        self.click(LoginLocator.AVATAR)
        self.click(LoginLocator.LOGOUT_BUTTON)
        #self.wait_for_load_page()
        self.assert_text_contain(LoginLocator.SIGNIN_TEXT, signin_text, "Verify Sign In Page")