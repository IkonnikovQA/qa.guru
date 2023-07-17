from selene import browser, be, have, command
from demoqa_tests.data.users import User
from demoqa_tests import resource


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def register(self, user: User):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.all('#genterWrapper .custom-control').element_by(have.exact_text(user.gender.value)).click()
        browser.element('#userNumber').type(user.mobile_number)

        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').send_keys(user.date_of_birth.raw_date.year).click()
        browser.element('.react-datepicker__month-select').send_keys(user.date_of_birth.month_formatted).click()
        browser.element(
            f'.react-datepicker__day--0{user.date_of_birth.day_formatted}:not(.react-datepicker__day--outside-month)').click()

        for subject in user.subjects:
            browser.element('#subjectsInput').type(subject.value).press_enter()

        for hobby in user.hobbies:
            browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text(hobby.value)).click()

        browser.element('#currentAddress').type(user.current_address)
        browser.element('#uploadPicture').send_keys(resource.path(user.picture))
        # if user.picture != '':
        #     browser.element('#uploadPicture').send_keys(resource.path(user.picture))
        #
        # if user.current_address is not None:
        #     browser.element('#currentAddress').type(user.current_address)

        browser.element('#state').perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user.state)).click()

        browser.element('#city').perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user.city)).click()

        browser.element('#submit').perform(command.js.click)

    def should_have_registered(self, user: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender.value,
                user.mobile_number,
                user.date_of_birth.value_in_modal,
                f'{", ".join([subject.value for subject in user.subjects])}',
                f'{", ".join([hobby.value for hobby in user.hobbies])}',
                user.picture,
                user.current_address,
                f'{user.state} {user.city}'
            )
        )