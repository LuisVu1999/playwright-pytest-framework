from pages.login_page import LoginPage
from pages.client_page import ClientPage

def test_edit_client(page):
    login_page = LoginPage(page)
    client_page = ClientPage(page)

    login_page.login("admin@example.com","growcrm")
    client_page.access_client()
    client_page.create_client("Luis_company", "Luis_firstname", "Luis_lastname", "test_abc@abc.com")
    client_page.search_client("Luis_company")
    client_page.edit_client("Luis_company_modified")
    client_page.search_client("Luis_company_modified")
    client_page.delete_client()