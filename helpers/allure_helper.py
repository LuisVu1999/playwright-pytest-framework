import allure

class AllureHelper():
    @staticmethod
    def attach_screenshot(page, name = "screenshot"):
        allure.attach(
            page.screenshot(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    @staticmethod
    def attach_text(name, content):
        allure.attach(
            content,
            name=name,
            attachment_type=allure.attachment_type.TEXT
        )
        