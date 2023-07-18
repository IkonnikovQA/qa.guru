from selene import browser, be, have, command

from demoqa_tests.data.users import User


class SimplifiedRegistrationPage:

    def __init__(self):
        self.__full_name = browser.element('#userName')
        self.__email = browser.element('#userEmail')
        self.__current_address = browser.element('#currentAddress')
        self.__permanent_address = browser.element('#permanentAddress')
        self.__output_values = browser.element('#output')
        self.__output_name = self.__output_values.element('#name')

    def _fill_full_name(self, user: User):
        if user.name is not None:
            self.__full_name.type(user.name)

    def _fill_email(self, user: User):
        if user.email is not None:
            self.__email.type(user.email)

    def _fill_current_address(self, user: User):
        if user.current_address is not None:
            self.__current_address.type(user.current_address)

    def _fill_permanent_address(self, user: User):
        if user.permanent_address is not None:
            self.__permanent_address.type(user.permanent_address)

    def _submit_form(self):
        browser.element('#submit').perform(command.js.scroll_into_view).click()

    def _should_have_correct_name(self, user: User):
        if user.name is not None:
            self.__output_name.should(have.text(user.name))
        else:
            self.__output_name.should(be.absent)

    def send_form(self, user: User):
        self._fill_full_name(user)
        self._fill_email(user)
        self._fill_current_address(user)
        self._fill_permanent_address(user)
        self._submit_form()

    def should_have_data_retrieved(self, user: User):
        self.__output_values.perform(command.js.scroll_into_view).should(be.present)
        self._should_have_correct_name(user)
        self.__output_values.element('#email').should(have.text(user.email))
        self.__output_values.element('#currentAddress').should(have.text(user.current_address))
        self.__output_values.element('#permanentAddress').should(have.text(user.permanent_address))