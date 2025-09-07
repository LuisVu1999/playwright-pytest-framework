from playwright.sync_api import Page, expect
import time
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

class BasePage:
    def __init__(self, page : Page):
        self.page = page
    
    def navigate(self, url : str):
        self.page.goto(url)
        
    def click(self, locator: str, timeout: int = 60000, retries : int = 5, delay : int = 500):  # Thoi gian doi max: 5s, so lan doi la 5, thoi gian nghi la 500ms
        attempt = 0
        while attempt < retries:  #Lap cho den khi den het so lan retry
            try:
                self.page.wait_for_selector(locator, state="visible", timeout=timeout) # Doi cho den khi element hien, neu qua thoi gian timeout thi -> raise timeout error
                element = self.page.locator(locator)
                element.click()  # Neu thanh cong thi in ra 
                print(f"Click successfully {locator}")
                return  #Thoat vi da click thanh cong
            except PlaywrightTimeoutError:
                print(f"Timeout: Cannot find {locator}, retry {retries+1}/{retries} ")  #Neu khong tin thay element trong tgian timeout -> in ra log
            except Exception as e:
                print(f"Failed for click {locator} : {e}, retry {retries+1}/{retries}") #Bat cac loi khac (ví dụ element bị che, detached, …) va in ra log

            attempt +=1  #Tang so lan len 1 sau moi lan thu
            time.sleep(delay/1000.0)  #Cho khoang 1s
        raise Exception (f"Cannot click {locator} after retry {retries} times") #Neu het so lan retry ma van loi thi in ra loi

    def fill(self, locator: str, text: str, timeout: int = 60000, retries: int = 5, delay: int = 500):
        attempt = 0
        while attempt < retries:
            try:
                self.page.wait_for_selector(locator, state="visible", timeout=timeout)
                element = self.page.locator(locator)
                element.fill(text)
                print(f"Fill successfully {locator}")
                return
            except PlaywrightTimeoutError:
                print(f"Timeout: Cannot find {locator}, retry {retries+1}/{retries} ")
            except Exception as e:
                print(f"Failed for fill {locator} : {e}, retry {retries+1}/{retries}")

            attempt += 1
            time.sleep(delay/1000.0)
        raise Exception(f"Cannot fill {locator} after retry {retries} times")

    def is_visible(self, locator: str) -> bool:
        return self.page.is_visible(locator)
    
    def wait_thread_sleep(self, seconds: float):
        time.sleep(seconds)

    def wait_for_load_page (self):
        self.page.wait_for_load_state("networkidle")

    def wait_for_element_visible(self, locator: str):
        self.page.wait_for_selector(locator)

    # def wait_for_element_enable(self, locator: str):
    #     self.page.locator(locator).wait_for(state="enable")

    def keyboard (self, key : str):
        self.page.keyboard.press(key)

    def assert_text (self, locator: str, expected_result: str, message = ""):
        self.page.wait_for_selector(locator)
        actual_result = self.page.text_content(locator).strip()
        assert actual_result == expected_result, (message or f"Text mismatch. Expected: '{expected_result}', but got: '{actual_result}'")

    def assert_have_text(self, locator: str, message: str = None):
        element = self.page.locator(locator)
        text = element.inner_text().strip()
        assert text is not None and text != "", message or f"Element '{locator}' has no text"
        # return text

    def assert_text_contain(self, locator: str, expected_substring: str, message = ""):
        actual_result = self.page.text_content(locator).strip()
        assert actual_result and expected_substring in actual_result, (message or f"Text mismatch. Expected: '{expected_substring}', but got: '{actual_result}'")

    def assert_attribute(self, locator: str, name: str, expected_value: str, message = ""):
        actual_value = self.page.locator(locator).get_attribute(name)
        assert actual_value == expected_value, (message or f"Value mismatch. Expected: '{expected_value}', but got: '{actual_value}")

    def assert_visible(self, locator: str, message = ""):
        assert self.page.is_visible(locator), message or f"Element '{locator}' not visible"
        # assert self.page.is

    # def drag_slide_to_value(self, locator: str, target_value: int, max_value: int = 100):
    #     slider = self.page.locator(locator)  #Tim element cua slider
    #     box = slider.bounding_box()   #tra ve kick thuoc duoi dang x, y : chieu rong va chieu cao
    #     if not box:  #Kiem tra xem slider co ton tai k, neu k thi nem loi
    #         raise Exception("Cannot find slider")
        
    #     start_x = box["x"] + box["width"] / 2    #Tinh toa do trung tam cua slide, keo tu trung tam
    #     start_y = box["y"] + box["height"] / 2

    #     # Tính offset theo tỷ lệ phần trăm
    #     offset_x = (target_value / max_value) * box["width"]  #Tinh pixel can keo sang phai
    #     self.page.mouse.move(start_x, start_y)  #di chuyen chuot tu phia trung tam ->
    #     self.page.mouse.down()  #nhan chuot cbi keo
    #     self.page.mouse.move(start_x + offset_x, start_y, steps = 15) #keo den vi tri target, lam keo muojt hon thanh 15 steps
    #     self.page.mouse.up()  #nha chuot

    def drag_slider_with_keys(self, handle_locator: str, target_value: int, attribute_name: str = "aria-valuenow"):
        handle = self.page.locator(handle_locator)
        handle.click()

        # Lấy giá trị hiện tại từ attribute
        current_value = int(float(handle.get_attribute(attribute_name) or 0))

        # Nếu nhỏ hơn target → nhấn ArrowRight cho đến khi đạt target
        while current_value < target_value:
            handle.press("ArrowRight")
            current_value = int(float(handle.get_attribute(attribute_name) or 0))

        # Nếu lớn hơn target → nhấn ArrowLeft cho đến khi đạt target
        while current_value > target_value:
            handle.press("ArrowLeft")
            current_value = int(float(handle.get_attribute(attribute_name) or 0))

    def type_text(self, locator: str, text: str, delay: float = 0.1, clear: bool = True,):
        element = self.page.locator(locator)
        element.click()
        if clear:
            element.fill("")
        for char in text:
            element.type(char, delay = delay)

    def hover_mouse_over(self, locator: str):
        self.page.hover(locator)

    def fill_iframe(self, frame_locator: str, element_insider_iframe: str, text: str):
        self.wait_for_element_visible(frame_locator)
        frame = self.page.frame_locator(frame_locator)
        frame.locator(element_insider_iframe).fill(text)

    #Click sau 0,5s
    def click_after_duration(self, locator):
        self.page.locator(locator).wait_for(state="visible")
        self.page.wait_for_timeout(500)
        self.click(locator)

    def test_debug(self):  #Chen ngay truoc dong loi
        self.page.pause()

    def expect_url(self, url: str):
        expect(self.page).to_have_url(url)

    def expect_title(self, title: str):
        expect(self.page).to_have_title(title)

    # --- Locator level assertions ---
    def expect_visible(self, locator: str):
        expect(self.page.locator(locator)).to_be_visible()

    def expect_have_css(self, locator: str, property: str, value: str):
        expect(self.page.locator(locator)).to_have_css(property, value)

    def expect_have_class(self, locator: str, value: str):
        expect(self.page.locator(locator)).to_have_class(value)

    def expect_have_attribute(self, locator: str, attribute_name: str, value: str):
        expect(self.page.locator(locator)).to_have_attribute(attribute_name, value)

    def expect_have_text(self, locator: str, text: str):
        expect(self.page.locator(locator)).to_have_text(text)



