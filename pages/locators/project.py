# Access Projects
class ProjectLocator:    
    PROJECT_MAIN = "//li[@data-modular-id='main_menu_team_projects']"
    PROJECT_SUB = "#submenu_projects"

    # Create Projects
    CREATE_BUTTON = "//button[@data-action-ajax-loading-target='commonModalBody']"
    NEW_CLIENT = "//a[@class='client-type-selector']"
    COMPANY_NAME = "(//input[@id='client_company_name'])[1]"
    FIRST_NAME = "(//input[@id='first_name'])[1]"
    LAST_NAME = "(//input[@id='last_name'])[1]"
    EMAIL = "(//input[@id='email'])[1]"
    CLICK_TEMPLATE = "//span[@aria-labelledby='select2-project_template_selector-container']"
    SELECT_LOGO = "//li[contains(text(),'Logo Design Template')]"
    PROJECT_TITLE = "#project_title"
    START_DATE = "//input[@name='project_date_start'][1]"
    DEADLINE_DATE = "//input[@name='project_date_due'][1]"
    SUBMIT_BUTTON = "#commonModalSubmitButton"
    ENABLE_PROGRESS = "//*[@id='js-projects-modal-add-edit']/div/div[11]/div[2]/div/label/span"
    CHECK_MANUALLY = "//label[@for='project_progress_manually']"
    SLIDER = "//div[@class='noUi-handle noUi-handle-lower']"
    START_DATE_TEXT = "//label[contains(text(),'Start Date*')]"

    # View Projects
    CLICK_PROJECT_NAME = "//tbody[@id='projects-td-container']//tr[1]//td[3]"
    VIEW_MANUALLY_PROGRESS = "//div[@class='align-self-end no-shrink']//h6"
    VIEW_PROGRESS_TEXT = "//*[name()='text' and contains(@class,'c3-gauge-v')]"
    CLICK_PROGRESS = "//*[name()='path' and contains(@class,'c3-shape c')]"
    VIEW_PROGRESS_TOOLTIP = "//td[@class='value']"
    VIEW_COMPANY_NAME = "//div[@class='card']//div//div//h6//a"
    VIEW_AVT = "//img[@class='img-circle avatar-xsmall']"
    VIEW_AVT_TOOLTIP = "//div[@class='p-b-20']//span[@data-toggle='tooltip']"
    VIEW_START_DATE = "//*[@id='project_details']/div[6]/div/div[1]/div[1]/div[2]"
    VIEW_DUE_DATE = "//*[@id='project_details']/div[6]/div/div[2]/div[1]/div[2]"

    # Delete Projects
    DELETE_BUTTON = "//button[@data-confirm-title='Delete Item']"
    CONFIRM_DELETE_BUTTON = "//button[@class='btn btn-sm btn-outline-danger']"

    # Search Projects
    DASHBOARD = "//I[@class='ti-home']"
    SEARCH_PROJECT = "#search_query"

    # Edit Project
    EDIT_BUTTON = "//button[@data-modal-title='Edit Project']"

    REQUEST_SUCCESSFULL_MESSAGE = "//div[@class='noty_message']"