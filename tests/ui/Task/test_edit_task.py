from pages.task_page import TaskPage

def test_edit_task(page):
    task_page = TaskPage(page)

    task_page.access_task()
    task_page.create_task("bank", "Luis task title_ed", "1999", "100", "Luis test", "08-12-2025")

    task_page.search_task("Luis task title_ed")
    task_page.edit_task("Luis task title modified", "This is comment of Luis", "Luis_test_item")

    task_page.search_task("Luis task title modified")
    task_page.delete_task()