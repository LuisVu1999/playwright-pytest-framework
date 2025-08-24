from pages.base_page import BasePage

class ClientPage(BasePage):
    CUSTOMER = "//li[@data-modular-id='main_menu_team_clients']"
    CLIENT_PAGE = "#submenu_clients"

    # Create Client
    ADD_CLIENT = "//button[@data-modal-title='Add Client']"
    COMPANY_NAME = "//div[@class='col-sm-12 col-lg-9']//input[@id='client_company_name']"
    FIRST_NAME = "//div[@class='col-sm-12 col-lg-9']//input[@id='first_name']"
    LAST_NAME = "//div[@class='col-sm-12 col-lg-9']//input[@id='last_name']"
    EMAIL = "//div[@class='col-sm-12 col-lg-9']//input[@id='email']"
    CATEGORY = "//span[@aria-labelledby='select2-client_categoryid-container']"
    SELECT_CATEGORY = "//li[contains(text(),'App Development')]"
    SUBMIT = "#commonModalSubmitButton"

    # Search Client
    DASHBOARD = "//I[@class='ti-home']"
    SEARCH = "#search_query"

    # Delete Client
    CLICK_COMPANY_NAME = "//tbody//tr[1]//td[2]"
    DELETE_BUTTON = "//button[@data-confirm-title='Delete Item']"
    CONFIRM_DELETE = "//button[@class='btn btn-sm btn-outline-danger']"

    # View Client
    CLIENT_PAGE_TITLE = "//h3[@class='text-themecolor']"
    CLIENT_LOGO = "//div[contains(@class,'logo-text')]"
    CLIENT_NAME = "//div[@class='card']//div//div//h6[1]"
    ACCOUNT_OWNER = "//div[@class='card']//div//div//div//a"
    CATEGORY_VIEW = "//div[@class='card']//div//div[2]//span"
    ACCOUNT_STATUS = "//div[@class='card']//div//div[3]//span"

    # Edit Client
    EDIT_CLIENT_ICON = "//span[@class='dropdown']"
    EDIT_CLIENT_BUTTON = "//a[@data-modal-title='Edit Client']"
    SELECT_ANOTHER_CATEGORY = "//li[contains(text(),'Content Marketing')]"
    STATUS = "#select2-client_status-container"
    SELECT_ANOTHER_STATUS = "//li[contains(text(),'Suspended')]"

    def __init__(self, page):
        super().__init__(page)

    def access_client(self):
        self.click(self.DASHBOARD)
        self.click(self.CUSTOMER)
        self.click(self.CLIENT_PAGE)

    def create_client(self, company: str, first_name: str, last_name: str, email: str):
        self.click(self.ADD_CLIENT)
        self.fill(self.COMPANY_NAME, company)
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.EMAIL, email)
        self.click(self.CATEGORY)
        self.click(self.SELECT_CATEGORY)
        self.click(self.SUBMIT)

    def view_client(self, client_page_title: str, logo: str, client_name: str, account_owner: str, view_category: str, account_status: str):
        self.click(self.CLICK_COMPANY_NAME)
        self.assert_text(self.CLIENT_PAGE_TITLE, client_page_title, "view client title")
        self.assert_text(self.CLIENT_LOGO, logo, "view logo")
        self.assert_text(self.CLIENT_NAME, client_name, "view client name")
        self.assert_text(self.ACCOUNT_OWNER, account_owner, "view account owner")
        self.assert_text(self.CATEGORY_VIEW, view_category, "view category")
        self.assert_text(self.ACCOUNT_STATUS, account_status, "view account status")

    def delete_client(self):
        self.click(self.CLICK_COMPANY_NAME)
        self.click(self.DELETE_BUTTON)
        self.click(self.CONFIRM_DELETE)
        self.wait_thread_sleep(2)
        
    def edit_client(self, company_modified: str):
        self.click(self.CLICK_COMPANY_NAME)
        self.click(self.EDIT_CLIENT_ICON)
        self.click(self.EDIT_CLIENT_BUTTON)
        self.fill(self.COMPANY_NAME, company_modified)
        self.click(self.CATEGORY)
        self.click(self.SELECT_ANOTHER_CATEGORY)
        self.click(self.STATUS)
        self.click(self.SELECT_ANOTHER_STATUS)
        self.click(self.SUBMIT)

    def search_client(self, company_name: str):
        self.access_client()
        self.fill(self.SEARCH, company_name)
        self.wait_thread_sleep(2)
