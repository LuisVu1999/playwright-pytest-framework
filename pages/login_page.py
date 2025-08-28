from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = "#email"
    PASSWORD_INPUT = "#password"
    SUBMIT_BUTTON = "#loginSubmitButton"
    PAGE_TITLE = "//*[@id='topnav-logo-container']/div/a/img[2]"

    FORGOT_PASSWORD = "//a[@data-target='login-forms-forgot']"
    FORGOT_PASSWORD_BUTTON = "#forgotSubmitButton"
    SUCCESSFULLY_RESET = "//div[@class='noty_message']"


    def __init__(self, page):
        super().__init__(page)

    def login(self, username: str, password: str):
        self.fill(self.USERNAME_INPUT, "")
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, "")
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)
        self.is_visible(self.PAGE_TITLE)
        #self.wait_thread_sleep(3)

    def forgot_password(self, email: str, reset_successfully_text: str):
        #1. Click on forgot password
        self.click(self.FORGOT_PASSWORD)
        self.fill(self.USERNAME_INPUT, email)
        self.click(self.FORGOT_PASSWORD_BUTTON)
        self.assert_text_contain(self.SUCCESSFULLY_RESET, reset_successfully_text)