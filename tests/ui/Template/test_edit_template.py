from pages.login_page import LoginPage
from pages.template_page import TemplatePage

def test_edit_template(page, template_fixture):
    template_page = TemplatePage(page)
    # template_page.access_template()
    # template_page.create_template("Luis template_create", "100000", "15", "60")
    template_page.access_template()
    template_page.edit_template()
    # template_page.access_template()
    # template_page.delete_template()