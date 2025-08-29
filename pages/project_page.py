from pages.base_page import BasePage

class ProjectPage(BasePage):
    # Access Projects
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

    def __init__(self, page):
        super().__init__(page)
    
    def create_project(self, company_name: str, first_name: str, last_name: str, email: str, project_title: str, 
                       start_date: str, deadline_date: str, target_value: int):
        self.click(self.CREATE_BUTTON)
        self.click(self.NEW_CLIENT)
        self.fill(self.COMPANY_NAME, company_name)
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.EMAIL, email)
        self.click(self.CLICK_TEMPLATE)
        self.click(self.SELECT_LOGO)
        self.fill(self.PROJECT_TITLE, project_title)
        self.type_text(self.START_DATE, start_date)
        self.keyboard("Enter")
        self.type_text(self.DEADLINE_DATE, deadline_date)
        self.keyboard("Enter")
        self.click(self.ENABLE_PROGRESS)
        self.click(self.CHECK_MANUALLY)
        self.drag_slider_with_keys(self.SLIDER, target_value)
        self.click(self.SUBMIT_BUTTON)
        self.wait_for_load_page()

    def view_project(self, manually_process: str, progress: str, company_name: str, expected_avt: str, expected_avt_tooltip: str, start_date: str, due_date: str):
        self.click(self.CLICK_PROJECT_NAME)
        self.assert_text(self.VIEW_MANUALLY_PROGRESS, manually_process, "view manual process")
        self.assert_text(self.VIEW_PROGRESS_TEXT, progress, "view process")
        self.assert_text(self.VIEW_COMPANY_NAME, company_name, "view company name")
        self.assert_attribute(self.VIEW_AVT, "src", expected_avt, "view avt")
        self.hover_mouse_over(self.VIEW_AVT)
        self.assert_attribute(self.VIEW_AVT_TOOLTIP, "data-original-title", expected_avt_tooltip, "view avt tooltip")
        self.assert_text(self.VIEW_START_DATE, start_date, "view start date")
        self.assert_text(self.VIEW_DUE_DATE, due_date, "view due date")

    def edit_project(self, project_title_modified: str, start_date_modified: str, deadline_date_modified: str):
        self.click(self.EDIT_BUTTON)
        self.wait_for_load_page()
        self.fill(self.PROJECT_TITLE, project_title_modified)
        self.type_text(self.START_DATE, start_date_modified)
        self.keyboard("Enter")
        self.type_text(self.DEADLINE_DATE, deadline_date_modified)
        self.keyboard("Enter")
        self.click(self.SUBMIT_BUTTON)
        self.wait_for_load_page()

    def delete_project(self):
        self.click(self.DELETE_BUTTON)
        self.click(self.CONFIRM_DELETE_BUTTON)
        self.wait_for_load_page()
        self.wait_thread_sleep(2)

    def access_project(self):
        self.wait_for_load_page()
        self.click(self.DASHBOARD)
        self.click(self.PROJECT_MAIN)
        self.click(self.PROJECT_SUB)

    def search_project(self, project_name: str):
        self.access_project()
        self.fill(self.SEARCH_PROJECT, project_name)
        self.wait_thread_sleep(4)