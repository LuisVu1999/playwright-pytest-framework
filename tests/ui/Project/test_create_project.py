from pages.project_page import ProjectPage
from pages.client_page import ClientPage
from helpers.test_data import TestData

def test_create_project(page):
    project_page = ProjectPage(page)
    client_page = ClientPage(page)

    company = TestData.random_company()
    project_title = TestData.random_title()

    project_page.access_project()
    project_page.create_project(company, TestData.random_first_name(), TestData.random_last_name(), TestData.random_email(), project_title, "12-13-2024", "11-18-2026", 87)
    project_page.search_project(project_title)
    project_page.delete_project()

    client_page.search_client(company)
    client_page.delete_client()