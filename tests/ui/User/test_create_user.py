from pages.login_page import LoginPage
from pages.user_page import UserPage

def test_create_user(page):
    user_page = UserPage(page)
    user_page.access_user()
    user_page.create_user("Dellon Inc", "Luis_firstname_cr", "Luis_lastname_cr", "test_abc_cr@abc.com", "0976765654", "QA Engineer")
    user_page.search_user("Luis_firstname_cr")
    user_page.delete_user()