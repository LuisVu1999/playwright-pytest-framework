from pages.client_page import ClientPage
from helpers.test_data import TestData

def test_create_client(page):
    client_page = ClientPage(page)

    company = TestData.random_company()
    first_name = TestData.random_first_name()
    last_name = TestData.random_last_name()
    email = TestData.random_email()

    client_page.access_client()
    client_page.create_client(company, first_name, last_name, email)
    client_page.search_client(company)
    client_page.delete_client()