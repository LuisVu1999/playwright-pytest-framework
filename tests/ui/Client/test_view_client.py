from pages.client_page import ClientPage

def test_view_client(page, client_fixture):
    client_page = ClientPage(page)
    client_id, data = client_fixture
    company = data["company"]
    first_name = data["first"]
    last_name = data["last"]
    email = data["email"]

    # client_page.access_client()
    # client_page.create_client("Luis_company_view", "Luis_firstname", "Luis_lastname", "test_abc@abc.com")
    client_page.search_client(company)
    client_page.view_client(f"Client - {company}", company, company, f"{first_name} {last_name}", "App Development", "Active")
    # client_page.search_client("Luis_company_view")
    # client_page.delete_client()