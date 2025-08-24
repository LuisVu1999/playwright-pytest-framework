from playwright.sync_api import Page
import time

class BasePage:
    def __init__(self, page : Page):
        self.page = page
    
    def navigate(self, url : str):
        self.page.goto(url)
        
    def click(self, locator: str):
        self.page.click(locator)

    def fill(self, locator: str, text: str):
        self.page.fill(locator, text)

    def is_visible(self, locator: str) -> bool:
        return self.page.is_visible(locator)
    
    def wait_thread_sleep(self, seconds: float):
        time.sleep(seconds)

    def wait_for_load_page (self):
        self.page.wait_for_load_state("networkidle")

    def keyboard (self, key : str):
        self.page.keyboard.press(key)

    def assert_text (self, locator: str, expected_result: str, message = ""):
        actual_result = self.page.text_content(locator).strip()
        assert actual_result == expected_result, (message or f"Text mismatch. Expected: '{expected_result}', but got: '{actual_result}'")

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