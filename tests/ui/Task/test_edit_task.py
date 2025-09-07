from pages.task_page import TaskPage
from helpers.test_data import TestData

def test_edit_task(page):
    task_page = TaskPage(page)

    # task_id, data = task_fixture
    # task_title = data["title"]
    task_title_created = TestData.random_title()
    task_title_modified = f"{TestData.random_title()}_modified"

    task_page.access_task()
    task_page.create_task("bank", task_title_created, "1999", "100", TestData.random_title(), "08-12-2025")

    task_page.search_task(task_title_created)
    task_page.edit_task(task_title_modified, "This is comment of Luis", TestData.random_title())

    task_page.search_task(task_title_modified)
    task_page.delete_task()