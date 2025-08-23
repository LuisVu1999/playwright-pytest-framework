from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        # Mở browser
        browser = p.chromium.launch(headless=False)  # headless=False để thấy trình duyệt chạy
        page = browser.new_page()

        # Truy cập trang login
        page.goto("https://demo.growcrm.io/login")