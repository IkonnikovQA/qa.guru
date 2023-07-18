from selene import browser

from demoqa_tests.models.components.panel import Panel
from demoqa_tests.models.pages.simplified_reg_form_page import SimplifiedRegistrationPage


class ApplicationManager:
    def __init__(self):
        self.simplified_reg_form = SimplifiedRegistrationPage()
        self.left_panel = Panel()

    def open(self):
        browser.open('/')
        return self