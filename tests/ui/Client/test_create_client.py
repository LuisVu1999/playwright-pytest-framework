from pages.client_page import ClientPage

def test_create_client(auth_context):
    page = auth_context
    client_page = ClientPage(page)
    client_page.access_client()
    client_page.create_client("Luis_company_create", "Luis_firstname", "Luis_lastname", "test_abc@abc.com")
    client_page.search_client("Luis_company_create")
    client_page.delete_client()