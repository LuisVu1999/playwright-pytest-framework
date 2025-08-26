from pages.base_page import BasePage
from datetime import datetime

class TaskPage (BasePage):
    current_date = datetime.now().strftime("%m-%d-%Y")
    # --- Access Tasks ---
    DASHBOARD = "(//a[@href='/home'])[2]"
    CLICK_TASKS = "//a[@href='/tasks']"

    # --- Create Tasks ---
    CREATE_BUTTON = "//button[@data-modal-title='Add A New Task']"
    CLICK_PROJECT = "//span[@aria-labelledby='select2-task_projectid-container']"
    ENTER_PROJECT = "//*[@id='main-body']/span[3]/span/span[1]/input"
    SELECT_PROJECT = "//li[contains(text(),'Mobile banking app development')]"
    TITLE = "#task_title"
    CLICK_STATUS = "//span[@aria-labelledby='select2-task_status-container']"
    SELECT_STATUS = "//li[contains(text(),'In Progress')]"
    CLICK_PRIORITY = "//span[@aria-labelledby='select2-task_priority-container']"
    SELECT_PRIORITY = "//li[contains(text(),'Low')]"
    CLICK_USER = "//*[@id='commonModalBody']/div/div/div[5]/div/span/span[1]/span"
    SELECT_USER = "//li[contains(text(),'Edwin Cook')]"
    CLICK_CLIENT = "//*[@id='commonModalBody']/div/div/div[7]/div/span/span[1]/span"
    SELECT_CLIENT = "//li[contains(text(),'Jill Rawson')]"
    ENABLE_MORE_INFORMATION = "(//span[@class='lever switch-col-light-blue'])[2]"
    CLICK_QUALITY = "//span[@aria-labelledby='select2-task_custom_field_41-container']"
    SELECT_QUALITY = "//li[contains(text(),'Low Resolution')]"
    CLICK_DEVICE = "//span[@aria-labelledby='select2-task_custom_field_42-container']"
    SELECT_DEVICE = "//li[contains(text(),'Desktop')]"
    ENTER_WORD_COUNT = "#task_custom_field_51"
    ENTER_IMAGE_COUNT = "#task_custom_field_53"
    # CHECK_PLAGIARISM = "//input[@id='task_custom_field_32']"
    ENTER_COMMENTS = "#tinymce"
    ID_FRAME_COMMENTS = "#task_custom_field_21_ifr"
    ENABLE_OPTION = "(//span[@class='lever switch-col-light-blue'])[3]"
    ENTER_DATE = "(//input[@name='task_date_due'])[1]"
    CLICK_TAG = "//*[@id='additional_information_section']/div[2]/div/span/span[1]/span"
    SELECT_TAG = "//li[contains(text(),'graphic-design')]"
    SUBMIT_BUTTON = "#commonModalSubmitButton"

    # --- Search Task ---
    SEARCH = "#search_query"

    # --- Delete Task ---
    CLICK_TASK_NAME = "//div[@class='x-title wordwrap']"
    DELETE_BUTTON = "//a[@data-confirm-title='Delete Item']"
    CONFIRM_DELETE = "//button[@class='btn btn-sm btn-outline-danger']"

    # --- Archive Task ---
    MORE_ACTION = "//span[@class='x-action-button']"
    ARCHIVE_BUTTON = "//a[@data-confirm-title='Archive Task']"
    CONFIRM_ARCHIVE = "//button[@class='btn btn-sm btn-outline-info']"

    # --- View Task ---
    TASK_NAME_TAG = "//div[@class='kanban-card-content-comntainer']//div[@class='x-title wordwrap']"
    PRIORITY_TAG = "//label[@data-original-title='Priority']"
    PROJECT_TAG = "//div[@class='x-meta']//span[1]"
    CLIENT_TAG = "//div[@class='x-meta']//span[2]"
    CREATED_TAG = "//div[@class='x-meta']//span[3]"
    ASSIGNED_USER_TAG1 = "(//img[@data-toggle='tooltip'])[1]"
    ASSIGNED_USER_TAG2 = "(//img[@data-toggle='tooltip'])[2]"

    VIEW_TASK_NAME = "#card-title-editable"
    VIEW_PROJECT_NAME = "#card-task-milestone-title"
    VIEW_STATUS = "#card-task-status-text"
    VIEW_PRIORITY = "#card-task-priority-text"
    VIEW_CREATED_BY = "//table[@class='table table-bordered table-sm']//tbody//tr[2]//td[2]//strong"
    VIEW_DATE_CREATED = "//table[@class='table table-bordered table-sm']//tbody//tr[3]//td[2]//strong"
    CLOSE_BUTTON = "#card-modal-close"

    # --- Edit Tag ---
    CLICK_TASK_TITLE = "#card-title-editable"
    EDIT_TASK_TITLE = "(//*[@id='task_title'])[1]"
    SAVE_TASK_TITLE = "#card-title-button-save"
    CLICK_EDIT_DESCRIPTION = "#card-description-button-edit"
    ID_EDIT_FRAME_COMMENTS = "#card-description-container_ifr"
    EDIT_FRAME_COMMENTS = "#tinymce"
    SAVE_COMMENTS = "#card-description-button-save"
    CREATE_ITEM = "#card-checklist-add-new"
    ENTER_ITEM_NAME = "(//textarea[@id='checklist_text'])[1]"
    SAVE_ITEM = "(//button[@id='checklist-submit-button'])[1]"

    CLICK_EDIT_START_DATE = "#task-start-date-container"
    CLICK_MONTH = "(//th[@class='datepicker-switch'])[1]"
    CLICK_YEAR = "(//th[@class='datepicker-switch'])[2]"
    SELECT_START_YEAR = "(//table[@class='table-condensed']//tbody//tr//td//span[contains(text(),'2027')])[1]"
    SELECT_START_MONTH = "(//table[@class='table-condensed']//tbody//tr//td//span[contains(text(),'Jun')])[1]"
    SELECT_START_DATE = "(//table[@class='table-condensed']//tbody//tr//td[contains(text(),'25')])"

    CLICK_EDIT_STATUS = "#card-task-status-text"
    SELECT_EDIT_STATUS = "(//li[contains(text(),'Awaiting Feedback')])[2]"
    CLICK_EDIT_PRIORITY = "#card-task-priority-text"
    SELECT_EDIT_PRIORITY = "(//li[contains(text(),'Urgent')])[3]"

    CLICK_EDIT_DUE_DATE = "#task-due-date-container"
    SELECT_DUE_YEAR = "(//table[@class='table-condensed']//tbody//tr//td//span[contains(text(),'2029')])[1]"
    SELECT_DUE_MONTH = "(//table[@class='table-condensed']//tbody//tr//td//span[contains(text(),'Dec')])[1]"
    SELECT_DUE_DATE = "(//table[@class='table-condensed']//tbody//tr//td[contains(text(),'20')])"

    UPLOAD_BUTTON = "#js-card-toggle-fileupload"
    FILE_INPUT_LOCATOR = "#card_fileupload"
    FILE_UPLOADED_LOCATOR = "//div[@class='x-name']//span"

    REQUEST_SUCCESSFULL_MESSAGE = "//div[@class='noty_message']"

    def __init__(self, page):
        super().__init__(page)

    def access_task(self):
        self.click(self.DASHBOARD)
        self.click(self.CLICK_TASKS)

    def create_task(self, project_name: str, task_title: str, word_count: str, image_count: str, text: str, date: str):
        self.wait_for_load_page()
        self.click(self.CREATE_BUTTON)
        self.click(self.CLICK_PROJECT)
        self.fill(self.ENTER_PROJECT, project_name)
        self.click(self.SELECT_PROJECT)
        self.fill(self.TITLE, task_title)
        self.click(self.CLICK_STATUS)
        self.click(self.SELECT_STATUS)
        self.click(self.CLICK_PRIORITY)
        self.click(self.SELECT_PRIORITY)
        self.wait_thread_sleep(2)
        self.click(self.CLICK_USER)
        self.click(self.SELECT_USER)
        self.click(self.CLICK_CLIENT)
        self.click(self.SELECT_CLIENT)
        self.click(self.ENABLE_MORE_INFORMATION)
        self.click(self.CLICK_QUALITY)
        self.click(self.SELECT_QUALITY)
        self.click(self.CLICK_DEVICE)
        self.click(self.SELECT_DEVICE)
        self.fill(self.ENTER_WORD_COUNT, word_count)
        self.fill(self.ENTER_IMAGE_COUNT, image_count)
        self.fill_iframe(self.ID_FRAME_COMMENTS, self.ENTER_COMMENTS, text)
        self.click(self.ENABLE_OPTION)
        self.type_text(self.ENTER_DATE, date)
        self.click(self.CLICK_TAG)
        self.click(self.SELECT_TAG)
        self.click(self.SUBMIT_BUTTON)
        self.wait_for_load_page()

    def view_task(self, task_name_tag: str, priority_tag: str, project_tag: str, client_tag: str, 
                  assigned_user_tag_1: str, assigned_user_tag_2: str, view_task_name: str, view_project_name: str, view_status: str, 
                  view_priority: str, view_created_by: str):
        self.wait_for_load_page()
        self.assert_text_contain(self.TASK_NAME_TAG, task_name_tag, "View task name list")
        self.assert_text(self.PRIORITY_TAG, priority_tag, "View priority list")
        self.assert_attribute(self.PROJECT_TAG, "title", project_tag, "View project list")
        self.assert_attribute(self.CLIENT_TAG, "title", client_tag, "View client list")
        #self.assert_text_contain(self.CREATED_TAG, self.current_date, "view created tag list")
        self.assert_attribute(self.ASSIGNED_USER_TAG1, "data-original-title", assigned_user_tag_1)
        self.assert_attribute(self.ASSIGNED_USER_TAG2, "data-original-title", assigned_user_tag_2)
        self.click(self.CLICK_TASK_NAME)
        self.assert_text(self.VIEW_TASK_NAME, view_task_name, "view task name")
        self.assert_text(self.VIEW_PROJECT_NAME, view_project_name)
        self.assert_text(self.VIEW_STATUS, view_status)
        self.assert_text(self.VIEW_PRIORITY, view_priority)
        self.assert_text(self.VIEW_CREATED_BY, view_created_by)
        #self.assert_text(self.VIEW_DATE_CREATED, self.current_date)
        self.click(self.CLOSE_BUTTON)

    def delete_task(self):
        self.wait_for_load_page()
        self.click(self.MORE_ACTION)
        self.click(self.DELETE_BUTTON)
        self.click(self.CONFIRM_DELETE)
        self.wait_for_load_page()
        self.wait_thread_sleep(2)

    def archive_task(self):
        self.wait_for_load_page()
        self.click(self.MORE_ACTION)
        self.click(self.ARCHIVE_BUTTON)
        self.click(self.CONFIRM_ARCHIVE)
        self.wait_for_load_page()

    def search_task(self, task_title: str):
        self.wait_for_load_page()
        self.access_task
        self.wait_for_load_page()
        self.fill(self.SEARCH, task_title)
        self.wait_thread_sleep(4)

    def edit_task(self, task_title_modified: str, comment: str, item_name: str, ):
        self.wait_for_load_page()
        self.click(self.TASK_NAME_TAG)
        self.click(self.CLICK_TASK_TITLE)
        self.wait_thread_sleep(1)
        self.fill(self.EDIT_TASK_TITLE, task_title_modified)
        self.click(self.SAVE_TASK_TITLE)
        
        self.click(self.CLICK_EDIT_DESCRIPTION)
        self.fill_iframe(self.ID_EDIT_FRAME_COMMENTS, self.EDIT_FRAME_COMMENTS, comment)
        self.click(self.SAVE_COMMENTS)

        self.click(self.CREATE_ITEM)
        self.fill(self.ENTER_ITEM_NAME, item_name)
        self.click(self.SAVE_ITEM)

        self.click(self.CLICK_EDIT_DUE_DATE)
        self.click(self.CLICK_MONTH)
        self.click(self.CLICK_YEAR)
        self.click(self.SELECT_DUE_YEAR)
        self.click(self.SELECT_DUE_MONTH)
        self.click(self.SELECT_DUE_DATE)

        self.click(self.CLICK_EDIT_START_DATE)
        self.click(self.CLICK_MONTH)
        self.click(self.CLICK_YEAR)
        self.click(self.SELECT_START_YEAR)
        self.click(self.SELECT_START_MONTH)
        self.click(self.SELECT_START_DATE)

        self.click(self.CLICK_EDIT_STATUS)
        self.click(self.SELECT_EDIT_STATUS)
        self.click(self.CLICK_EDIT_PRIORITY)
        self.click(self.SELECT_EDIT_PRIORITY)
        self.click(self.CLOSE_BUTTON)
        self.wait_for_load_page()