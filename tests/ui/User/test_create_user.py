from pages.login_page import LoginPage
from pages.user_page import UserPage

def test_create_user(page):
    login_page = LoginPage(page)
    user_page = UserPage(page)
    login_page.login("admin@example.com","growcrm")
    user_page.access_user()
    user_page.create_user("Dellon Inc", "Luis_firstname", "Luis_lastname", "test_abc@abc.com", "0976765654", "QA Engineer")
    user_page.search_user("Luis_firstname")
    user_page.delete_user()