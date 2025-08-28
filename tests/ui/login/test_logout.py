from pages.logout_page import LogoutPage
from pages.login_page import LoginPage

def test_logout(page):
    login_page = LoginPage(page)
    logout_page = LogoutPage(page)
    login_page.login("admin@example.com","growcrm")
    logout_page.logout("Sign in to your account")