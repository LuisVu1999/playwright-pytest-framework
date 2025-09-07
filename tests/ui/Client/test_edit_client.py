from pages.client_page import ClientPage
from helpers.test_data import TestData

def test_edit_client(page, client_fixture):
    client_page = ClientPage(page)
    client_id, data = client_fixture
    company = data["company"]
    company_name_created = TestData.random_company()
    company_name_edited = TestData.random_company()

    # client_page.access_client()
    # client_page.create_client(company_name_created, TestData.random_first_name(),TestData.random_last_name(), TestData.random_email())
    client_page.search_client(company)
    client_page.edit_client(company_name_edited)
    # client_page.search_client(company_name_edited)
    # client_page.delete_client()