from pages.base_page import BasePage
from pages.locators.project import ProjectLocator

class ProjectPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
    
    def create_project(self, company_name: str, first_name: str, last_name: str, email: str, project_title: str, 
                       start_date: str, deadline_date: str, target_value: int):
        self.click(ProjectLocator.CREATE_BUTTON)
        self.click(ProjectLocator.NEW_CLIENT)
        self.fill(ProjectLocator.COMPANY_NAME, company_name)
        self.fill(ProjectLocator.FIRST_NAME, first_name)
        self.fill(ProjectLocator.LAST_NAME, last_name)
        self.fill(ProjectLocator.EMAIL, email)
        self.click(ProjectLocator.CLICK_TEMPLATE)
        self.click(ProjectLocator.SELECT_LOGO)
        self.fill(ProjectLocator.PROJECT_TITLE, project_title)
        self.type_text(ProjectLocator.START_DATE, start_date)
        self.keyboard("Enter")
        self.type_text(ProjectLocator.DEADLINE_DATE, deadline_date)
        self.keyboard("Enter")
        self.click(ProjectLocator.ENABLE_PROGRESS)
        self.click(ProjectLocator.CHECK_MANUALLY)
        self.drag_slider_with_keys(ProjectLocator.SLIDER, target_value)
        self.click(ProjectLocator.SUBMIT_BUTTON)
        self.wait_for_load_page()

    def view_project(self, manually_process: str, progress: str, company_name: str, expected_avt: str, expected_avt_tooltip: str, start_date: str, due_date: str):
        self.click(ProjectLocator.CLICK_PROJECT_NAME)
        self.assert_text(ProjectLocator.VIEW_MANUALLY_PROGRESS, manually_process, "view manual process")
        self.assert_text(ProjectLocator.VIEW_PROGRESS_TEXT, progress, "view process")
        self.assert_text(ProjectLocator.VIEW_COMPANY_NAME, company_name, "view company name")
        self.assert_attribute(ProjectLocator.VIEW_AVT, "src", expected_avt, "view avt")
        self.hover_mouse_over(ProjectLocator.VIEW_AVT)
        self.assert_attribute(ProjectLocator.VIEW_AVT_TOOLTIP, "data-original-title", expected_avt_tooltip, "view avt tooltip")
        self.assert_text(ProjectLocator.VIEW_START_DATE, start_date, "view start date")
        self.assert_text(ProjectLocator.VIEW_DUE_DATE, due_date, "view due date")

    def edit_project(self, project_title_modified: str, start_date_modified: str, deadline_date_modified: str):
        self.click(ProjectLocator.EDIT_BUTTON)
        self.wait_for_load_page()
        self.fill(ProjectLocator.PROJECT_TITLE, project_title_modified)
        self.type_text(ProjectLocator.START_DATE, start_date_modified)
        self.keyboard("Enter")
        self.type_text(ProjectLocator.DEADLINE_DATE, deadline_date_modified)
        self.keyboard("Enter")
        self.click(ProjectLocator.SUBMIT_BUTTON)
        self.wait_for_load_page()

    def delete_project(self):
        self.click(ProjectLocator.DELETE_BUTTON)
        self.click(ProjectLocator.CONFIRM_DELETE_BUTTON)
        self.wait_for_load_page()
        self.wait_thread_sleep(2)

    def access_project(self):
        self.wait_for_load_page()
        self.click(ProjectLocator.DASHBOARD)
        self.click(ProjectLocator.PROJECT_MAIN)
        self.click(ProjectLocator.PROJECT_SUB)

    def search_project(self, project_name: str):
        self.access_project()
        self.fill(ProjectLocator.SEARCH_PROJECT, project_name)
        self.wait_thread_sleep(4)