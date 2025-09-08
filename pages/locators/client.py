class ClientLocator:
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

    REQUEST_SUCCESSFULL_MESSAGE = "//div[@class='noty_message']"
    REQUEST_MESSAGE = "Request has been completed"