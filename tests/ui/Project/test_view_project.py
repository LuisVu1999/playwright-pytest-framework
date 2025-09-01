from pages.project_page import ProjectPage
from pages.client_page import ClientPage


avatar_url = "https://demo.growcrm.io/storage/avatars/system/default_avatar.jpg"
def test_view_project(auth_context):
    page = auth_context
    project_page = ProjectPage(page)
    client_page = ClientPage(page)

    project_page.access_project()
    project_page.create_project("Luis_company", "Luis_firstname", "Luis_lastname", "test_abc@abc.com", "Luis_project_title", "04-05-2024", "08-18-2026", 87)
    project_page.search_project("Luis_project_title")
    project_page.view_project("Manually Set Progress", "87.0%", "Luis_company", avatar_url, "Luis_firstname Luis_lastname", "04-05-2024", "08-18-2026")

    client_page.search_client("Luis_company")
    client_page.delete_client()