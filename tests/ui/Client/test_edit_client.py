from pages.client_page import ClientPage

def test_edit_client(page):
    client_page = ClientPage(page)
    client_page.access_client()
    client_page.create_client("Luis_company_edit", "Luis_firstname", "Luis_lastname", "test_abc@abc.com")
    client_page.search_client("Luis_company_edit")
    client_page.edit_client("Luis_company_modified")
    client_page.search_client("Luis_company_modified")
    client_page.delete_client()