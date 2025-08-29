from pages.base_page import BasePage

class TemplatePage(BasePage):
    # --- Create Template ---
    CLICK_PROJECT = "//li[@data-modular-id='main_menu_team_projects']"
    CLICK_TEMPLATE = "//a[@href='https://demo.growcrm.io/templates/projects']"
    CREATE_BUTTON = "//button[@data-modal-title='Create A Project Template']"

    PROJECT_TITLE = "#project_title"
    CLICK_CATEGORY = "//span[@aria-labelledby='select2-project_categoryid-container']"
    SELECT_APP_DEVELOPMENT = "//li[contains(text(),'App Development')]"

    ENABLE_USER_PERMISSION = "(//span[@class='lever switch-col-light-blue'])[2]"
    CHECK_TASK_COLLABORATION = "//label[@for='assignedperm_tasks_collaborate']"

    ENABLE_PROJECT_PERMISSION = "(//span[@class='lever switch-col-light-blue'])[3]"
    CHECK_VIEW_TASK = "//label[@for='clientperm_tasks_view']"
    CHECK_TASK_PARTICIPATION = "//label[@for='clientperm_tasks_collaborate']"
    CHECK_CREATE_TASKS = "//label[@for='clientperm_tasks_create']"
    CHECK_TIMESHEET = "//label[@for='clientperm_timesheets_view']"
    CHECK_EXPENSE = "//label[@for='clientperm_expenses_view']"

    ENABLE_PROJECT_BILLING = "(//span[@class='lever switch-col-light-blue'])[4]"
    BILLING = "#project_billing_rate"
    CLICK_HOURLY = "//span[@aria-labelledby='select2-project_billing_type-container']"
    SELECT_FIXED_FEE = "//li[contains(text(),'Fixed Fee')]"
    ESTIMATED_HOUR = "#project_billing_estimated_hours"
    ESTIMATED_COSTS = "#project_billing_costs_estimate"

    SUBMIT_BUTTON = "#commonModalSubmitButton"

    # --- View Template ---
    CLICK_DEFAULT_TEMPLATE_NAME = "//a[contains(.,'Graphic Design Template')]"
    DETAILS_TAB = "#tabs-menu-details"
    EDIT_DESCRIPTION = "#project-description-button-edit"

    TASK_TAB = "#tabs-menu-tasks"

    MILESTONES_TAB = "#tabs-menu-milestones"
    DESIGN = "(//td[@class='milestones_col_name'])[4]"
    UNCATEGORIED = "(//td[@class='milestones_col_name'])[5]"
    PLANNING = "(//td[@class='milestones_col_name'])[3]"
    DEVELOPMENT = "(//td[@class='milestones_col_name'])[2]"
    TESTING = "(//td[@class='milestones_col_name'])[1]"
    DELETE = "(//button[@id='foobar'])[1]"
    EDIT_IN_MILESTONE_BUTTON = "(//button[@data-modal-title='Edit Milestone'])[1]"

    FILE_TAB = "#tabs-menu-files"

    # --- Edit Template ---
    EDIT_BUTTON = "//button[@data-modal-title='Edit Project Template']"

    # --- Delete Template ---
    CLICK_CUSTOM_TEMPLATE_NAME = "//a[contains(text(),'Luis template')]"
    DELETE_BUTTON = "//button[@data-confirm-title='Delete Template']"
    CONFIRM_DELETE = "//button[@class='btn btn-sm btn-outline-danger']"

    DASHBOARD = "//i[@class='ti-home']"

    REQUEST_SUCCESSFULL_MESSAGE = "//div[@class='noty_message']"

    def __init__(self, page):
        super().__init__(page)

    def access_template(self):
        self.wait_for_load_page()
        self.click(self.DASHBOARD)
        self.click(self.CLICK_PROJECT)
        self.click(self.CLICK_TEMPLATE)

    def create_template(self, project_title: str, billing: str, estimated_hour: str, estimated_cost: str):
        self.click(self.CREATE_BUTTON)
        self.fill(self.PROJECT_TITLE, project_title)
        self.click(self.CLICK_CATEGORY)
        self.click(self.SELECT_APP_DEVELOPMENT)
        self.click(self.ENABLE_USER_PERMISSION)
        self.click(self.CHECK_TASK_COLLABORATION)
        self.click(self.ENABLE_PROJECT_PERMISSION)
        self.click(self.CHECK_VIEW_TASK)
        self.click(self.CHECK_TASK_PARTICIPATION)
        self.click(self.CHECK_CREATE_TASKS)
        self.click(self.CHECK_TIMESHEET)
        self.click(self.CHECK_EXPENSE)
        self.click(self.ENABLE_PROJECT_BILLING)
        self.fill(self.BILLING, billing)
        self.click(self.CLICK_HOURLY)
        self.click(self.SELECT_FIXED_FEE)
        self.fill(self.ESTIMATED_HOUR, estimated_hour)
        self.fill(self.ESTIMATED_COSTS, estimated_cost)
        self.click(self.SUBMIT_BUTTON)

    def view_template(self, details_tab: str, task_tab: str, milestones_tab: str, testing: str, 
                      development: str, planning: str, design: str, uncategoried: str, file_tab: str):
        self.click(self.CLICK_DEFAULT_TEMPLATE_NAME)
        self.assert_text(self.DETAILS_TAB, details_tab, "view details tab")
        self.assert_text(self.TASK_TAB, task_tab, "view task tab")
        self.assert_text(self.MILESTONES_TAB, milestones_tab, "view milestone tab")
        self.click(self.MILESTONES_TAB)
        actual_result = self.page.text_content(self.TESTING)
        print(f"DEBUG: actual_result = '{actual_result}'")
        self.assert_text(self.TESTING, testing, "view testing")
        self.assert_text(self.DEVELOPMENT, development, "view development")
        self.assert_text(self.PLANNING, planning, "view planning")
        self.assert_text(self.DESIGN, design, "view design")
        self.assert_text(self.UNCATEGORIED, uncategoried, "view uncategoried")
        self.assert_visible(self.DELETE, "Check delete button display")
        self.assert_visible(self.EDIT_IN_MILESTONE_BUTTON, "check edit in milestone button")
        self.assert_text(self.FILE_TAB, file_tab, "view file tab")

    def edit_template(self):
        self.click(self.CLICK_CUSTOM_TEMPLATE_NAME)
        self.click(self.EDIT_BUTTON)
        self.click(self.ENABLE_USER_PERMISSION)
        self.click(self.SUBMIT_BUTTON)
        self.wait_for_load_page()

    def delete_template(self):
        self.click(self.CLICK_CUSTOM_TEMPLATE_NAME)
        self.click(self.DELETE_BUTTON)
        self.click(self.CONFIRM_DELETE)
        self.wait_for_load_page()
        self.wait_thread_sleep(2)