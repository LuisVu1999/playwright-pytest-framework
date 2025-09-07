from pages.task_page import TaskPage
from datetime import datetime
from helpers.test_data import TestData

current_date = datetime.now().strftime("%m-%d-%Y")
def test_view_task(page):
    task_page = TaskPage(page)

    # task_id, data = task_fixture
    # task_title = data["title"]
    task_title = TestData.random_title()
    app = "Mobile banking app development"

    task_page.access_task()
    task_page.create_task(app, task_title, "1999", "100", TestData.random_title(), "08-12-2025")

    task_page.search_task(task_title)
    task_page.view_task(task_title, "Low", app, "Dellon Inc",
                        task_title, app, "In Progress","Low", "Steven Mallet")
    task_page.search_task(task_title)
    task_page.delete_task()