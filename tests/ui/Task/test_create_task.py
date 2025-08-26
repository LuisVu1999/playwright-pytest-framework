from pages.login_page import LoginPage
from pages.task_page import TaskPage

def test_create_task(page):
    login_page = LoginPage(page)
    task_page = TaskPage(page)

    login_page.login("admin@example.com","growcrm")

    task_page.access_task()
    task_page.create_task("bank", "Luis task title_cr", "1999", "100", "Luis test", "08-12-2025")

    task_page.search_task("Luis task title_cr")
    task_page.delete_task()