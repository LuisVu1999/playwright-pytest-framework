from pages.base_page import BasePage
from datetime import datetime
from pages.locators.user import UserLocator

class UserPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def access_user(self):
        self.wait_for_load_page()
        self.click(UserLocator.DASHBOARD)
        self.click(UserLocator.CUSTOMER)
        self.click(UserLocator.CLIENT)

    def create_user(self, company_name : str, first_name : str, last_name : str, 
                    user_email : str, user_phone : str, user_position : str, ):
        self.click(UserLocator.CREATE_USER)
        self.click(UserLocator.CLICK_COMPANY)
        self.fill(UserLocator.SEARCH_COMPANY, company_name)
        self.click(UserLocator.SELECT_COMPANY)
        self.fill(UserLocator.FIRST_NAME, first_name)
        self.fill(UserLocator.LAST_NAME, last_name)
        self.fill(UserLocator.EMAIL, user_email)
        self.fill(UserLocator.PHONE, user_phone)
        self.fill(UserLocator.POSITION, user_position)
        self.click(UserLocator.TIMEZONE)
        self.click(UserLocator.VIETNAM)
        self.click(UserLocator.SUBMIT_BTN)
        self.wait_for_element_visible(UserLocator.REQUEST_SUCCESSFULL_MESSAGE)
        self.wait_for_load_page()

    def view_user(self, expected_name: str, expected_email: str, expected_user_text: str, 
                  expected_phone: str, expected_job_title: str, expected_last_seen: str):
        self.click(UserLocator.CLICK_USER)
        current_date = datetime.now().strftime("%m-%d-%Y")
        print(f"Expected: '{current_date}'")
        actual = self.page.locator(UserLocator.VIEW_LAST_SEEN).inner_text()
        print(f"Actual: '{actual}'")
        self.assert_visible(UserLocator.VIEW_AVATAR, "view avatar")
        self.assert_text(UserLocator.VIEW_USER_NAME, expected_name, "view user name")
        self.assert_text(UserLocator.VIEW_EMAIL, expected_email, "view email")
        self.assert_text(UserLocator.VIEW_USER_TEXT, expected_user_text, "view user text")
        self.assert_text(UserLocator.VIEW_PHONE, expected_phone, "view phone")
        self.assert_text(UserLocator.VIEW_JOB_TITLE, expected_job_title, "view job title")
        #self.assert_text(self.VIEW_DATE, expected_date, "view added date")
        self.assert_text(UserLocator.VIEW_LAST_SEEN, expected_last_seen, "view last seen")
        self.click(UserLocator.CLOSE_BUTTON)

    def edit_user(self, first_name_modified: str, last_name_modified: str, email_modified: str, 
                  phone_modified: str, position_modified: str, twitter_url: str):
        self.click(UserLocator.EDIT_BUTTON)
        self.fill(UserLocator.FIRST_NAME, first_name_modified)
        self.fill(UserLocator.LAST_NAME, last_name_modified)
        self.fill(UserLocator.EMAIL, email_modified)
        self.fill(UserLocator.PHONE, phone_modified)
        self.fill(UserLocator.POSITION, position_modified)
        self.click(UserLocator.TIMEZONE)
        self.click(UserLocator.BERLIN)
        self.click(UserLocator.ENABLE_PROFILE)
        self.fill(UserLocator.TWITTER, twitter_url)
        self.fill(UserLocator.FACEBOOK, twitter_url)
        self.fill(UserLocator.LINKEDIN, twitter_url)
        self.fill(UserLocator.GITHUB, twitter_url)
        self.fill(UserLocator.DIRBBLE, twitter_url)
        self.click(UserLocator.SUBMIT_BTN)
        self.wait_for_load_page()

    def delete_user(self):
        self.click(UserLocator.DELETE_BUTTON)
        self.click(UserLocator.CONFIRM_DELETE)
        self.wait_for_load_page()
        self.wait_thread_sleep(2)

    def search_user(self, company_name : str):
        self.access_user()
        self.fill(UserLocator.SEARCH, company_name)
        self.wait_thread_sleep(4)