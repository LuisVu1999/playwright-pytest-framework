import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

STORAGE_FILE = "auth.json"

class AuthHelper:
    @staticmethod
    def ensure_logged_in():
        if not os.path.exists(STORAGE_FILE):
            AuthHelper.login_and_save_state()

    @staticmethod
    def login_and_save_state():
        with sync_playwright() as p:
            # Step 1: Mở browser và login bằng UI
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            page.goto("https://demo.growcrm.io/home")  # đổi link web của bạn

            # Nhập username + password (sửa selector cho đúng web bạn)
            page.fill("#email", "")
            page.fill("#email", "admin@example.com")
            page.fill("#password", "")
            page.fill("#password", "growcrm")
            page.click("#loginSubmitButton")
            #page.wait_for_selector("//*[@id='topnav-logo-container']/div/a/img[2]")
            page.wait_for_url("https://demo.growcrm.io/home", timeout=15000)

            # ✅ Lưu toàn bộ storage state (cookies + localStorage + sessionStorage)
            context.storage_state(path=STORAGE_FILE)
            print(f"✅ Saved to {STORAGE_FILE}")
            browser.close()

            # Step 3: Mở browser mới, dùng lại cookies để login không cần nhập pass
            # browser = p.chromium.launch(headless=False)
            # context = browser.new_context(storage_state="auth.json")
            # page = context.new_page()
            # page.goto("https://demo.growcrm.io/home")  # trang sau khi login
            # page.wait_for_selector("//*[@id='topnav-logo-container']/div/a/img[2]")
            # print("✅ Logged in using cookies")
            # time.sleep(3)  # để bạn thấy kết quả
            # browser.close()

    # if __name__ == "__main__":
    #     login_and_save_state()
