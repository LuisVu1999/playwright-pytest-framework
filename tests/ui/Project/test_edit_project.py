from pages.project_page import ProjectPage
from pages.client_page import ClientPage
from helpers.test_data import TestData

def test_edit_project(page, project_fixture):
    project_page = ProjectPage(page)
    client_page = ClientPage(page)

    project_id, data = project_fixture
    project_title = data["title"]
    company = data["company"]

    # project_page.access_project()
    # project_page.create_project("Luis_company", "Luis_firstname", "Luis_lastname", "test_abc@abc.com", "Luis_project_title", "12-13-2024", "11-18-2026", 87)
    project_page.search_project(project_title)
    project_page.edit_project(TestData.random_title(), "12-12-2028", "01-01-2031")
    client_page.search_client(company)
    client_page.delete_client()