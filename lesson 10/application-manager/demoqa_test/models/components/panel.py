from selene import browser, have


class Panel:
    def __init__(self):
        self.container = browser.element('.left-pannel')

    def open(self):
        browser.open('/interaction')
        return self

    def open_item(self, section, item):
        self.open()
        self.container.all('.element-group').element_by(have.text(section)).click()
        self.container.all('.text').element_by(have.exact_text(item)).click()
        return self

    def open_simplified_reg_form(self):
        self.open_item('Elements', 'Text Box')

    def open_full_reg_form(self):
        self.open_item('Forms', 'Practice Form')