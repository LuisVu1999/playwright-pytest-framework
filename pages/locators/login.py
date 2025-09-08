class LoginLocator:
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