from pages.project_page import ProjectPage
from pages.client_page import ClientPage

def test_create_project(page):
    project_page = ProjectPage(page)
    client_page = ClientPage(page)

    project_page.access_project()
    project_page.create_project("Luis_company", "Luis_firstname", "Luis_lastname", "test_abc@abc.com", "Luis_project_title", "12-13-2024", "11-18-2026", 87)
    project_page.search_project("Luis_project_title")
    project_page.delete_project()

    client_page.search_client("Luis_company")
    client_page.delete_client()