from pages.project_page import ProjectPage
from helpers.test_data import TestData

avatar_url = "https://demo.growcrm.io/storage/avatars/system/default_avatar.jpg"
def test_view_project(page, client_fixture):
    project_page = ProjectPage(page)

    client_id, data = client_fixture
    company = data["company"]
    project_title = f"Titile916_{TestData.random_title()}"
    first_name = data["first"]
    last_name = data["last"]
    user_name = f"{first_name} {last_name}"

    #1. Create Project
    project_page.access_project()
    project_page.create_project_existing_client(company, project_title, "12-13-2024", "11-18-2026", 87)
    
    #2. View Project
    project_page.search_project(project_title)
    project_page.view_project("Manually Set Progress", "87.0%", company, avatar_url, user_name, "12-13-2024", "11-18-2026")