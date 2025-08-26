from pages.login_page import LoginPage
from pages.task_page import TaskPage
from datetime import datetime

current_date = datetime.now().strftime("%m-%d-%Y")
def test_view_task(page):
    login_page = LoginPage(page)
    task_page = TaskPage(page)

    login_page.login("admin@example.com","growcrm")

    task_page.access_task()
    task_page.create_task("bank", "Luis task title_vi", "1999", "100", "Luis test", "08-12-2025")

    task_page.search_task("Luis task title_vi")
    task_page.view_task("Luis task title_vi", "Low", "Mobile banking app development", "Dellon Inc",
                        "Jill", "Edwin", "Luis task title_vi", "Mobile banking app development", "In Progress","Low", "Steven Mallet")
    task_page.search_task("Luis task title_vi")
    task_page.delete_task()