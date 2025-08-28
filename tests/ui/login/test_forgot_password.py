from pages.login_page import LoginPage

def test_forgot_password(page):
    login_page = LoginPage(page)
    login_page.forgot_password("admin@example.com", "We have sent you an email with instructions")