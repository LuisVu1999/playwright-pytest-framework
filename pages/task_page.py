from pages.base_page import BasePage
from datetime import datetime
from pages.locators.task import TaskLocator

class TaskPage (BasePage):
    def __init__(self, page):
        super().__init__(page)

    def access_task(self):
        self.wait_for_load_page()
        self.click(TaskLocator.DASHBOARD)
        self.click(TaskLocator.CLICK_TASKS)

    def create_task(self, project_name: str, task_title: str, word_count: str, image_count: str, text: str, date: str):
        self.click(TaskLocator.CREATE_BUTTON)
        self.click(TaskLocator.CLICK_PROJECT)
        self.fill(TaskLocator.ENTER_PROJECT, project_name)
        self.click(TaskLocator.SELECT_PROJECT)
        self.fill(TaskLocator.TITLE, task_title)
        self.click(TaskLocator.CLICK_STATUS)
        self.click(TaskLocator.SELECT_STATUS)
        self.click(TaskLocator.CLICK_PRIORITY)
        self.click(TaskLocator.SELECT_PRIORITY)
        self.wait_thread_sleep(2)
        self.click(TaskLocator.CLICK_USER)
        self.click(TaskLocator.SELECT_USER)
        self.click(TaskLocator.CLICK_CLIENT)
        self.click(TaskLocator.SELECT_CLIENT)
        self.click(TaskLocator.ENABLE_MORE_INFORMATION)
        self.click(TaskLocator.CLICK_QUALITY)
        self.click(TaskLocator.SELECT_QUALITY)
        self.click(TaskLocator.CLICK_DEVICE)
        self.click(TaskLocator.SELECT_DEVICE)
        self.fill(TaskLocator.ENTER_WORD_COUNT, word_count)
        self.fill(TaskLocator.ENTER_IMAGE_COUNT, image_count)
        self.fill_iframe(TaskLocator.ID_FRAME_COMMENTS, TaskLocator.ENTER_COMMENTS, text)
        self.click(TaskLocator.ENABLE_OPTION)
        self.type_text(TaskLocator.ENTER_DATE, date)
        self.click(TaskLocator.CLICK_TAG)
        self.click(TaskLocator.SELECT_TAG)
        self.click(TaskLocator.SUBMIT_BUTTON)
        self.wait_for_load_page()

    def view_task(self, task_name_tag: str, priority_tag: str, project_tag: str, client_tag: str, 
                  view_task_name: str, view_project_name: str, view_status: str, 
                  view_priority: str, view_created_by: str):
        self.assert_text_contain(TaskLocator.TASK_NAME_TAG, task_name_tag, "View task name list")
        self.assert_text(TaskLocator.PRIORITY_TAG, priority_tag, "View priority list")
        self.assert_attribute(TaskLocator.PROJECT_TAG, "title", project_tag, "View project list")
        self.assert_attribute(TaskLocator.CLIENT_TAG, "title", client_tag, "View client list")
        #self.assert_text_contain(self.CREATED_TAG, self.current_date, "view created tag list")
        self.hover_mouse_over(TaskLocator.ASSIGNED_USER_TAG1)
        self.assert_have_text(TaskLocator.TOOLTIP_1)
        self.hover_mouse_over(TaskLocator.ASSIGNED_USER_TAG2)
        self.assert_have_text(TaskLocator.TOOLTIP_2)
        self.click(TaskLocator.CLICK_TASK_NAME)
        self.assert_text(TaskLocator.VIEW_TASK_NAME, view_task_name, "view task name")
        self.assert_text(TaskLocator.VIEW_PROJECT_NAME, view_project_name)
        self.assert_text(TaskLocator.VIEW_STATUS, view_status)
        self.assert_text(TaskLocator.VIEW_PRIORITY, view_priority)
        self.assert_text(TaskLocator.VIEW_CREATED_BY, view_created_by)
        #self.assert_text(self.VIEW_DATE_CREATED, self.current_date)
        self.click(TaskLocator.CLOSE_BUTTON)

    def delete_task(self):
        self.click(TaskLocator.MORE_ACTION)
        self.click(TaskLocator.DELETE_BUTTON)
        self.click(TaskLocator.CONFIRM_DELETE)
        self.wait_for_load_page()
        self.wait_thread_sleep(2)

    def archive_task(self):
        self.click(TaskLocator.MORE_ACTION)
        self.click(TaskLocator.ARCHIVE_BUTTON)
        self.click(TaskLocator.CONFIRM_ARCHIVE)
        self.wait_for_load_page()

    def search_task(self, task_title: str):
        self.access_task
        self.fill(TaskLocator.SEARCH, task_title)
        self.wait_thread_sleep(4)

    def edit_task(self, task_title_modified: str, comment: str, item_name: str, ):
        self.click(TaskLocator.TASK_NAME_TAG)
        self.click(TaskLocator.CLICK_TASK_TITLE)
        self.wait_thread_sleep(1)
        self.fill(TaskLocator.EDIT_TASK_TITLE, task_title_modified)
        self.click(TaskLocator.SAVE_TASK_TITLE)
        
        self.click(TaskLocator.CLICK_EDIT_DESCRIPTION)
        self.fill_iframe(TaskLocator.ID_EDIT_FRAME_COMMENTS, TaskLocator.EDIT_FRAME_COMMENTS, comment)
        self.click(TaskLocator.SAVE_COMMENTS)

        self.click(TaskLocator.CREATE_ITEM)
        self.fill(TaskLocator.ENTER_ITEM_NAME, item_name)
        self.click(TaskLocator.SAVE_ITEM)

        self.click(TaskLocator.CLICK_EDIT_DUE_DATE)
        self.click(TaskLocator.CLICK_MONTH)
        self.click(TaskLocator.CLICK_YEAR)
        self.click(TaskLocator.SELECT_DUE_YEAR)
        self.click(TaskLocator.SELECT_DUE_MONTH)
        self.click(TaskLocator.SELECT_DUE_DATE)

        self.click(TaskLocator.CLICK_EDIT_START_DATE)
        self.click(TaskLocator.CLICK_MONTH)
        self.click(TaskLocator.CLICK_YEAR)
        self.click(TaskLocator.SELECT_START_YEAR)
        self.click(TaskLocator.SELECT_START_MONTH)
        self.click(TaskLocator.SELECT_START_DATE)

        self.click(TaskLocator.CLICK_EDIT_STATUS)
        self.click(TaskLocator.SELECT_EDIT_STATUS)
        self.click(TaskLocator.CLICK_EDIT_PRIORITY)
        self.click(TaskLocator.SELECT_EDIT_PRIORITY)
        self.click(TaskLocator.CLOSE_BUTTON)
        self.wait_for_load_page()