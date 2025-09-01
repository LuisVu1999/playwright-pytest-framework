from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = "#email"
    PASSWORD_INPUT = "#password"
    SUBMIT_BUTTON = "#loginSubmitButton"
    PAGE_TITLE = "//*[@id='topnav-logo-container']/div/a/img[2]"

    FORGOT_PASSWORD = "//a[@data-target='login-forms-forgot']"
    FORGOT_PASSWORD_BUTTON = "#forgotSubmitButton"
    SUCCESSFULLY_RESET = "//div[@class='noty_message']"

    AVATAR = "//li[@class='nav-item dropdown u-pro']//a[@data-toggle='dropdown']"
    LOGOUT_BUTTON = "//a[@href='/logout']"
    SIGNIN_TEXT = "//h4[@class='box-title m-t-10 text-center']"

    def __init__(self, page):
        super().__init__(page)

    def login(self, username: str, password: str):
        self.navigate("https://demo.growcrm.io/login")
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

    def logout(self, signin_text: str):
        self.click(self.AVATAR)
        self.click(self.LOGOUT_BUTTON)
        #self.wait_for_load_page()
        self.assert_text_contain(self.SIGNIN_TEXT, signin_text, "Verify Sign In Page")