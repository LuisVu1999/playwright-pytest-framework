from pages.base_page import BasePage
from pages.locators.template import TemplateLocator

class TemplatePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def access_template(self):
        self.wait_for_load_page()
        self.click(TemplateLocator.DASHBOARD)
        self.click(TemplateLocator.CLICK_PROJECT)
        self.click(TemplateLocator.CLICK_TEMPLATE)

    def create_template(self, project_title: str, billing: str, estimated_hour: str, estimated_cost: str):
        self.click(TemplateLocator.CREATE_BUTTON)
        self.fill(TemplateLocator.PROJECT_TITLE, project_title)
        self.click(TemplateLocator.CLICK_CATEGORY)
        self.click(TemplateLocator.SELECT_APP_DEVELOPMENT)
        self.click(TemplateLocator.ENABLE_USER_PERMISSION)
        self.click(TemplateLocator.CHECK_TASK_COLLABORATION)
        self.click(TemplateLocator.ENABLE_PROJECT_PERMISSION)
        self.click(TemplateLocator.CHECK_VIEW_TASK)
        self.click(TemplateLocator.CHECK_TASK_PARTICIPATION)
        self.click(TemplateLocator.CHECK_CREATE_TASKS)
        self.click(TemplateLocator.CHECK_TIMESHEET)
        self.click(TemplateLocator.CHECK_EXPENSE)
        self.click(TemplateLocator.ENABLE_PROJECT_BILLING)
        self.fill(TemplateLocator.BILLING, billing)
        self.click(TemplateLocator.CLICK_HOURLY)
        self.click(TemplateLocator.SELECT_FIXED_FEE)
        self.fill(TemplateLocator.ESTIMATED_HOUR, estimated_hour)
        self.fill(TemplateLocator.ESTIMATED_COSTS, estimated_cost)
        self.click(TemplateLocator.SUBMIT_BUTTON)

    def view_template(self, details_tab: str, task_tab: str, milestones_tab: str, testing: str, 
                      development: str, planning: str, design: str, uncategoried: str, file_tab: str):
        self.click(TemplateLocator.CLICK_DEFAULT_TEMPLATE_NAME)
        self.assert_text(TemplateLocator.DETAILS_TAB, details_tab, "view details tab")
        self.assert_text(TemplateLocator.TASK_TAB, task_tab, "view task tab")
        self.assert_text(TemplateLocator.MILESTONES_TAB, milestones_tab, "view milestone tab")
        self.click(TemplateLocator.MILESTONES_TAB)
        actual_result = self.page.text_content(TemplateLocator.TESTING)
        print(f"DEBUG: actual_result = '{actual_result}'")
        self.assert_text(TemplateLocator.TESTING, testing, "view testing")
        self.assert_text(TemplateLocator.DEVELOPMENT, development, "view development")
        self.assert_text(TemplateLocator.PLANNING, planning, "view planning")
        self.assert_text(TemplateLocator.DESIGN, design, "view design")
        self.assert_text(TemplateLocator.UNCATEGORIED, uncategoried, "view uncategoried")
        self.assert_visible(TemplateLocator.DELETE, "Check delete button display")
        self.assert_visible(TemplateLocator.EDIT_IN_MILESTONE_BUTTON, "check edit in milestone button")
        self.assert_text(TemplateLocator.FILE_TAB, file_tab, "view file tab")

    def edit_template(self):
        self.click(TemplateLocator.CLICK_CUSTOM_TEMPLATE_EDIT)
        self.click(TemplateLocator.EDIT_BUTTON)
        self.click(TemplateLocator.ENABLE_USER_PERMISSION)
        self.click(TemplateLocator.SUBMIT_BUTTON)
        self.wait_for_load_page()

    def delete_template(self):
        self.click(TemplateLocator.CLICK_CUSTOM_TEMPLATE_CREATE)
        self.click(TemplateLocator.DELETE_BUTTON)
        self.click(TemplateLocator.CONFIRM_DELETE)
        self.wait_for_load_page()
        self.wait_thread_sleep(2)