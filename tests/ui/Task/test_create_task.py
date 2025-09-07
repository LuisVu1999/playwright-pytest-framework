from pages.task_page import TaskPage
from helpers.test_data import TestData

def test_create_task(page):
    task_page = TaskPage(page)

    task_title = TestData.random_title()

    task_page.access_task()
    task_page.create_task("bank", task_title, "1999", "100", TestData.random_title(), "08-12-2025")

    task_page.search_task(task_title)
    task_page.delete_task()