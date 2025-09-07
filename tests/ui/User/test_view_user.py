from pages.login_page import LoginPage
from pages.user_page import UserPage
from datetime import datetime

current_date = datetime.now().strftime("%m-%d-%Y")

def test_view_user(page, user_fixture):
    user_page = UserPage(page)

    user_id, data = user_fixture
    first_name = data["first"]
    last_name = data["last"]
    email = data["email"]

    # user_page.access_user()
    # user_page.create_user("Dellon Inc", "Luis_firstname_vi", "Luis_lastname_vi", "test_abc_vi@abc.com", "0976765654", "QA Engineer")
    # first_name="Luis_firstname", last_name="Luis_lastname", email="test_abc%40abc.com"
    user_page.search_user(first_name)
    user_page.view_user(f"{first_name} {last_name}", email, "Client User", "0976765654", "QA Engineer", "---")
    # user_page.search_user("Luis_firstname_vi")
    # user_page.delete_user()