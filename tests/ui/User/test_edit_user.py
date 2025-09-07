from pages.login_page import LoginPage
from pages.user_page import UserPage
from helpers.test_data import TestData

def test_edit_user(page, user_fixture):
    user_page = UserPage(page)

    user_id, data = user_fixture
    first_name = data["first"]
    # first_name_created = TestData.random_first_name()
    first_name_edited = TestData.random_first_name()

    # user_page.access_user()
    # user_page.create_user("Dellon Inc", first_name_created, TestData.random_last_name(), TestData.random_email(), "0976765654", "QA Engineer")
    user_page.search_user(first_name)
    user_page.edit_user(first_name_edited, TestData.random_last_name(), TestData.random_email(), "0976765654", "QA Engineer_modified", TestData.random_title())
    # user_page.search_user(first_name_edited)
    # user_page.delete_user()