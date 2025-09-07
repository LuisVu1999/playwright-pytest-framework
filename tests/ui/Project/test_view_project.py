from pages.project_page import ProjectPage
from pages.client_page import ClientPage


avatar_url = "https://demo.growcrm.io/storage/avatars/system/default_avatar.jpg"
def test_view_project(page, project_fixture):
    project_page = ProjectPage(page)
    client_page = ClientPage(page)

    project_id, data = project_fixture
    company = data["company"]
    project_title = data["title"]
    first_name = data["first"]
    last_name = data["last"]

    # project_page.access_project()
    # project_page.create_project("Luis_company", "Luis_firstname", "Luis_lastname", "test_abc@abc.com", "Luis_project_title", "04-05-2024", "08-18-2026", 87)
    project_page.search_project(project_title)
    project_page.view_project("Manually Set Progress", "87.0%", company, avatar_url, f"{first_name} {last_name}", "12-13-2024", "11-18-2026")

    client_page.search_client(company)
    client_page.delete_client()