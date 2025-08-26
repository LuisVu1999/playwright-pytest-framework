from pages.login_page import LoginPage
from pages.client_page import ClientPage

def test_create_client(page):
    login_page = LoginPage(page)
    client_page = ClientPage(page)

    login_page.login("admin@example.com","growcrm")
    client_page.access_client()
    client_page.create_client("Luis_company_create", "Luis_firstname", "Luis_lastname", "test_abc@abc.com")
    client_page.search_client("Luis_company_create")
    client_page.delete_client()