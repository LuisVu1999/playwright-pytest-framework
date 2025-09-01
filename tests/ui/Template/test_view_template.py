from pages.login_page import LoginPage
from pages.template_page import TemplatePage

def test_view_template(page):
    template_page = TemplatePage(page)
    template_page.access_template()
    template_page.view_template("Details", "Tasks", "Milestones", "Testing", "Development", "Planning", "Design", "Uncategorised", "Files")