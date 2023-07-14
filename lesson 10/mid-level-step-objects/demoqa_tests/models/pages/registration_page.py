from selene import browser, have, command, be

from demoqa_test import resource


class RegistrationPage:

    def __init__(self):
        self.registered_user_data = browser.element('.table').all('td').even

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def fill_gender(self, value):
        browser.element(f'[name=gender][value={value}]+label').click()

    def fill_mobile_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').send_keys(year).click()
        browser.element('.react-datepicker__month-select').send_keys(month).click()
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_hobby(self, value):
        browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text(value)).click()

    def upload_picture(self, value):
        browser.element('#uploadPicture').send_keys(resource.path(value))

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def fill_state(self, value):
        browser.element('#state').perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()

    def fill_city(self, value):
        browser.element('#city').perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()

    def submit_form(self):
        browser.element('#submit').perform(command.js.click)

    def should_have_modal_with(self, title):
        browser.element('.modal-header').perform(command.js.scroll_into_view).should(have.exact_text(title))

    def should_have_registered_user_with(self, full_name, email, gender, mobile_number, date_of_birth,
                                         subjects, hobbies, picture, current_address, state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                mobile_number,
                date_of_birth,
                subjects,
                hobbies,
                picture,
                current_address,
                state_and_city
            )
        )

    def close_modal(self):
        browser.element('#closeLargeModal').perform(command.js.scroll_into_view).click()

    def should_not_have_modal(self):
        browser.element('.modal-dialog').should(be.absent)

    def should_be_cleared(self):
        browser.element('#firstName').should(be.blank)