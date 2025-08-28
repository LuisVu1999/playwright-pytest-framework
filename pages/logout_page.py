from pages.base_page import BasePage

class LogoutPage(BasePage):
    AVATAR = "//li[@class='nav-item dropdown u-pro']//a[@data-toggle='dropdown']"
    LOGOUT_BUTTON = "//a[@href='/logout']"
    SIGNIN_TEXT = "//h4[@class='box-title m-t-10 text-center']"

    def __init__(self, page):
        super().__init__(page)

    def logout(self, signin_text: str):
        self.click(self.AVATAR)
        self.click(self.LOGOUT_BUTTON)
        self.wait_for_load_page()
        self.assert_text_contain(self.SIGNIN_TEXT, signin_text, "Verify Sign In Page")