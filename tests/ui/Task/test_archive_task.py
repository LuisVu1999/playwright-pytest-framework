from pages.task_page import TaskPage

def test_archive_task(auth_context):
    page = auth_context
    task_page = TaskPage(page)

    task_page.access_task()
    task_page.create_task("bank", "Luis task title_ar", "1999", "100", "Luis test", "08-12-2025")

    task_page.search_task("Luis task title_ar")
    task_page.archive_task()

    task_page.search_task("Luis task title_ar")
    task_page.delete_task()