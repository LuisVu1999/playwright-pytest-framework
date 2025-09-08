class TaskLocator:
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
    TOOLTIP_1 = "(//div[@class='tooltip-inner'])[1]"
    TOOLTIP_2 = "(//div[@class='tooltip-inner'])[2]"
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