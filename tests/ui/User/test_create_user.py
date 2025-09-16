from pages.login_page import LoginPage
from pages.user_page import UserPage
from helpers.test_data import TestData

def test_create_user(page):
    user_page = UserPage(page)

    first_name = f"012_title{TestData.random_first_name()}"
    last_name = f"013_title{TestData.random_last_name()}"
    email = f"title014{TestData.random_email()}"

    user_page.access_user()
    user_page.create_user("Dellon Inc", first_name, last_name, email, "0976765654", "QA Engineer")
    user_page.search_user(email)
    user_page.delete_user()