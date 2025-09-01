from pages.login_page import LoginPage
from pages.user_page import UserPage

def test_edit_user(page):
    user_page = UserPage(page)
    user_page.access_user()
    user_page.create_user("Dellon Inc", "Luis_firstname_ed", "Luis_lastname_ed", "test_abc_ed@abc.com", "0976765654", "QA Engineer")
    user_page.search_user("Luis_firstname_ed")
    user_page.edit_user("Luis_firstname_modified", "Luis_lastname_modified", "test_modified_abc@abc.com", "0976765654", "QA Engineer_modified", "SampleSocialProfile1958")
    user_page.search_user("Luis_firstname_modified")
    user_page.delete_user()