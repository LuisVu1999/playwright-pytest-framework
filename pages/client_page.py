from pages.base_page import BasePage
from pages.locators.client import ClientLocator

class ClientPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def access_client(self):
        self.click(ClientLocator.DASHBOARD)
        self.click(ClientLocator.CUSTOMER)
        self.click(ClientLocator.CLIENT_PAGE)

    def create_client(self, company: str, first_name: str, last_name: str, email: str):
        self.click(ClientLocator.ADD_CLIENT)
        self.fill(ClientLocator.COMPANY_NAME, company)
        self.fill(ClientLocator.FIRST_NAME, first_name)
        self.fill(ClientLocator.LAST_NAME, last_name)
        self.fill(ClientLocator.EMAIL, email)
        self.click(ClientLocator.CATEGORY)
        self.click(ClientLocator.SELECT_CATEGORY)
        self.click(ClientLocator.SUBMIT)
        self.wait_for_load_page()

    def view_client(self, client_page_title: str, logo: str, client_name: str, account_owner: str, view_category: str, account_status: str):
        self.click(ClientLocator.CLICK_COMPANY_NAME)
        self.assert_text(ClientLocator.CLIENT_PAGE_TITLE, client_page_title, "view client title")
        self.assert_text(ClientLocator.CLIENT_LOGO, logo, "view logo")
        self.assert_text(ClientLocator.CLIENT_NAME, client_name, "view client name")
        self.assert_text(ClientLocator.ACCOUNT_OWNER, account_owner, "view account owner")
        self.assert_text(ClientLocator.CATEGORY_VIEW, view_category, "view category")
        self.assert_text(ClientLocator.ACCOUNT_STATUS, account_status, "view account status")

    def delete_client(self):
        self.click(ClientLocator.CLICK_COMPANY_NAME)
        self.click(ClientLocator.DELETE_BUTTON)
        self.click(ClientLocator.CONFIRM_DELETE)
        self.wait_for_load_page()
        self.wait_thread_sleep(2)
        
    def edit_client(self, company_modified: str, successful_message = "Request has been completed"):
        self.click(ClientLocator.CLICK_COMPANY_NAME)
        self.click(ClientLocator.EDIT_CLIENT_ICON)
        self.click(ClientLocator.EDIT_CLIENT_BUTTON)
        self.fill(ClientLocator.COMPANY_NAME, company_modified)
        self.click(ClientLocator.CATEGORY)
        self.click(ClientLocator.SELECT_ANOTHER_CATEGORY)
        self.click(ClientLocator.STATUS)
        self.click(ClientLocator.SELECT_ANOTHER_STATUS)
        self.click(ClientLocator.SUBMIT)
        self.wait_for_load_page()
        self.assert_text_contain(ClientLocator.REQUEST_SUCCESSFULL_MESSAGE, successful_message)

    def search_client(self, company_name: str):
        self.access_client()
        self.fill(ClientLocator.SEARCH, company_name)
        self.wait_thread_sleep(4)
