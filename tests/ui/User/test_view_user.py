from pages.login_page import LoginPage
from pages.user_page import UserPage
from datetime import datetime

current_date = datetime.now().strftime("%m-%d-%Y")

def test_view_user(auth_context):
    page = auth_context
    user_page = UserPage(page)
    user_page.access_user()
    user_page.create_user("Dellon Inc", "Luis_firstname_vi", "Luis_lastname_vi", "test_abc_vi@abc.com", "0976765654", "QA Engineer")
    user_page.search_user("Luis_firstname_vi")
    user_page.view_user("Luis_firstname_vi Luis_lastname_vi", "test_abc_vi@abc.com", "Client User", "0976765654", "QA Engineer", "---")
    user_page.search_user("Luis_firstname_vi")
    user_page.delete_user()