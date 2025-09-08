class TemplateLocator:
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
    CLICK_CUSTOM_TEMPLATE_CREATE = "//a[contains(text(),'Luis_template_create')]"
    # CLICK_CUSTOM_TEMPLATE_DELETE = "//a[contains(text(),'Luis_template_view')]"
    CLICK_CUSTOM_TEMPLATE_EDIT = "//a[contains(text(),'Luis template_create')]"
    DELETE_BUTTON = "//button[@data-confirm-title='Delete Template']"
    CONFIRM_DELETE = "//button[@class='btn btn-sm btn-outline-danger']"

    DASHBOARD = "//i[@class='ti-home']"

    REQUEST_SUCCESSFULL_MESSAGE = "//div[@class='noty_message']"