from pages.login_page import LoginPage
from pages.user_page import UserPage
from helpers.test_data import TestData

def test_create_user(page):
    user_page = UserPage(page)

    first_name = TestData.random_first_name()
    last_name = TestData.random_last_name()
    email = TestData.random_email()

    user_page.access_user()
    user_page.create_user("Dellon Inc", first_name, last_name, email, "0976765654", "QA Engineer")
    user_page.search_user(first_name)
    user_page.delete_user()