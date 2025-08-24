from pages.login_page import LoginPage
from pages.template_page import TemplatePage

def test_create_template(page):
    login_page = LoginPage(page)
    template_page = TemplatePage(page)

    login_page.login("admin@example.com","growcrm")

    template_page.access_template()
    template_page.create_template("Luis template_create", "100000", "15", "60")
    template_page.access_template()
    template_page.delete_template()