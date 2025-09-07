# 1. Environment Config (môi trường chạy test)
class ConfigUrl:
    BASE_URL = "https://demo.growcrm.io"
    LOGIN_URL = BASE_URL + "/login"
    PROJECT_URL = BASE_URL + "/projects"
    CLIENT_URL = BASE_URL + "/clients"
    USER_URL = BASE_URL + "/contacts"
    TEMPLATE_URL = BASE_URL + "/templates/projects"
    TASK_URL = BASE_URL + "/tasks"

# 2. Credentials (account test cố định)
class Credentials:
    ADMIN_USER = "admin@example.com"
    ADMIN_PASSWORD = "growcrm"

# 3. Browser Settings
class BrowserConfig:
    HEADLESS = True
    DEFAULT_TIMEOUT = 60000
    VIEWPORT = {"width": 1920, "height": 1080}

# 4. API Config (nếu có test API)
class APIConfig:
    API_BASE_URL = "https://demo.growcrm.io/api"
    DEFAULT_HEADERS = {
        "Content-Type": "application/json"
    }

# 5. Other Constants (timeout, path, report)
class Paths:
    DOWNLOAD_DIR = "downloads/"
    REPORT_DIR = "reports/"
    STORAGE_FILE = "auth.json"

ENVIRONMENTS ={
        "dev":  {
            "url": "https://demo.growcrm.io",
            "username": "admin@example.com",
            "password": "growcrm"
        },
        "staging": {
            "url": "https://demo.growcrm.io",
            "username": "admin@example.com",
            "password": "growcrm"
        }, 
        "prod": {
            "url": "https://demo.growcrm.io",
            "username": "admin@example.com",
            "password": "growcrm"
        }
    }