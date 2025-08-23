from pages.login_page import LoginPage

def test_login(page):
    login_page = LoginPage(page)
    login_page.login("admin@example.com","growcrm")