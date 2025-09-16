from pages.project_page import ProjectPage
from helpers.test_data import TestData

def test_edit_project(page, client_fixture):
    project_page = ProjectPage(page)

    #1. Khai bao
    client_id, data = client_fixture
    company = data["company"]
    project_title_created = f"Titile916_{TestData.random_title()}"
    project_title_modified = f"Titile917_{TestData.random_title()}"

    #2. Create project
    project_page.access_project()
    project_page.create_project_existing_client(company, project_title_created, "12-13-2024", "11-18-2026", 87)
    
    #3. Edit project
    project_page.search_project(project_title_created)
    project_page.edit_project(project_title_modified, "12-12-2028", "01-01-2031")