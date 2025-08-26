from pages.base_page import BasePage
from datetime import datetime

class UserPage(BasePage):
    CUSTOMER = "//li[@data-modular-id='main_menu_team_clients']"
    CLIENT = "//a[@href='/users']"
    DASHBOARD = "//I[@class='ti-home']"
    CREATE_USER = "//button[@data-modal-title='Create A New User']"
    CLICK_COMPANY = "//span[@aria-labelledby='select2-clientid-container']"
    SEARCH_COMPANY = "//span[@class='select2-search select2-search--dropdown']//input"
    SELECT_COMPANY = "//li[contains(text(),'Dellon Inc')]"
    FIRST_NAME = "//div[@class='col-sm-12 col-lg-9']//input[@id='first_name']"
    LAST_NAME = "//div[@class='col-sm-12 col-lg-9']//input[@id='last_name']"
    EMAIL = "//div[@class='col-sm-12 col-lg-9']//input[@id='email']"
    PHONE = "//div[@class='col-sm-12 col-lg-9']//input[@id='phone']"
    POSITION = "//div[@class='col-sm-12 col-lg-9']//input[@id='position']"
    TIMEZONE = "//span[@aria-labelledby='select2-timezone-container']"
    VIETNAM = "//li[contains(text(),'Asia/Ho_Chi_Minh')]"
    SUBMIT_BTN = "#commonModalSubmitButton"
    SEARCH = "#search_query"
    EDIT_BUTTON = "//button[@data-modal-title='Edit User']"
    BERLIN = "//li[contains(text(),'Europe/Berlin')]"
    ENABLE_PROFILE = "//span[@class='lever switch-col-light-blue']"
    TWITTER = "#social_twitter"
    FACEBOOK = "#social_facebook"
    LINKEDIN = "#social_linkedin"
    GITHUB = "#social_github"
    DIRBBLE = "#social_dribble"
    CLICK_USER = "//tbody[@id='contacts-td-container']//tr[1]//td[2]"
    VIEW_AVATAR = "//img[@class='img-circle']"
    VIEW_USER_NAME = "//h4[contains(@class,'card-title')]"
    VIEW_EMAIL = "//h6[@class='card-subtitle']"
    VIEW_USER_TEXT = "//span[@class='label label-outline-success']"
    VIEW_PHONE = "//div[@class='card-body p-t-0']//h6[1]"
    VIEW_JOB_TITLE = "//div[@class='card-body p-t-0']//h6[2]"
    VIEW_DATE = "//div[@class='card-body p-t-0']//h6[3]"
    VIEW_LAST_SEEN = "//div[@class='card-body p-t-0']//h6[4]"
    CLOSE_BUTTON = "#commonModalExtraCloseIcon"
    DELETE_BUTTON = "//button[@data-confirm-title='Delete User']"
    CONFIRM_DELETE = "//button[@class='btn btn-sm btn-outline-danger']"

    REQUEST_SUCCESSFULL_MESSAGE = "//div[@class='noty_message']"

    def __init__(self, page):
        super().__init__(page)

    def access_user(self):
        self.click(self.DASHBOARD)
        self.click(self.CUSTOMER)
        self.click(self.CLIENT)

    def create_user(self, company_name : str, first_name : str, last_name : str, 
                    user_email : str, user_phone : str, user_position : str, ):
        self.wait_for_load_page()
        self.click(self.CREATE_USER)
        self.click(self.CLICK_COMPANY)
        self.fill(self.SEARCH_COMPANY, company_name)
        self.click(self.SELECT_COMPANY)
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.EMAIL, user_email)
        self.fill(self.PHONE, user_phone)
        self.fill(self.POSITION, user_position)
        self.click(self.TIMEZONE)
        self.click(self.VIETNAM)
        self.click(self.SUBMIT_BTN)
        self.wait_for_element_visible(self.REQUEST_SUCCESSFULL_MESSAGE)
        self.wait_for_load_page()

    def view_user(self, expected_name: str, expected_email: str, expected_user_text: str, 
                  expected_phone: str, expected_job_title: str, expected_last_seen: str):
        self.click(self.CLICK_USER)
        self.wait_for_load_page()
        current_date = datetime.now().strftime("%m-%d-%Y")
        print(f"Expected: '{current_date}'")
        actual = self.page.locator(self.VIEW_LAST_SEEN).inner_text()
        print(f"Actual: '{actual}'")
        self.assert_visible(self.VIEW_AVATAR, "view avatar")
        self.assert_text(self.VIEW_USER_NAME, expected_name, "view user name")
        self.assert_text(self.VIEW_EMAIL, expected_email, "view email")
        self.assert_text(self.VIEW_USER_TEXT, expected_user_text, "view user text")
        self.assert_text(self.VIEW_PHONE, expected_phone, "view phone")
        self.assert_text(self.VIEW_JOB_TITLE, expected_job_title, "view job title")
        #self.assert_text(self.VIEW_DATE, expected_date, "view added date")
        self.assert_text(self.VIEW_LAST_SEEN, expected_last_seen, "view last seen")
        self.click(self.CLOSE_BUTTON)

    def edit_user(self, first_name_modified: str, last_name_modified: str, email_modified: str, 
                  phone_modified: str, position_modified: str, twitter_url: str):
        self.wait_for_load_page()
        self.click(self.EDIT_BUTTON)
        self.fill(self.FIRST_NAME, first_name_modified)
        self.fill(self.LAST_NAME, last_name_modified)
        self.fill(self.EMAIL, email_modified)
        self.fill(self.PHONE, phone_modified)
        self.fill(self.POSITION, position_modified)
        self.click(self.TIMEZONE)
        self.click(self.BERLIN)
        self.click(self.ENABLE_PROFILE)
        self.fill(self.TWITTER, twitter_url)
        self.fill(self.FACEBOOK, twitter_url)
        self.fill(self.LINKEDIN, twitter_url)
        self.fill(self.GITHUB, twitter_url)
        self.fill(self.DIRBBLE, twitter_url)
        self.click(self.SUBMIT_BTN)
        self.wait_for_load_page()

    def delete_user(self):
        self.wait_for_load_page()
        self.click(self.DELETE_BUTTON)
        self.click(self.CONFIRM_DELETE)
        self.wait_for_load_page()
        self.wait_thread_sleep(2)

    def search_user(self, company_name : str):
        self.wait_for_load_page()
        self.access_user()
        self.wait_for_load_page()
        self.fill(self.SEARCH, company_name)
        self.wait_thread_sleep(4)