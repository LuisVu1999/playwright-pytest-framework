from pages.client_page import ClientPage

def test_view_client(page):
    client_page = ClientPage(page)
    client_page.access_client()
    client_page.create_client("Luis_company_view", "Luis_firstname", "Luis_lastname", "test_abc@abc.com")
    client_page.search_client("Luis_company_view")
    client_page.view_client("Client - Luis_company_view", "Luis_company_view", "Luis_company_view", "Luis_firstname Luis_lastname", "App Development", "Active")
    client_page.search_client("Luis_company_view")
    client_page.delete_client()