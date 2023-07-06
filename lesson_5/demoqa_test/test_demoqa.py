import os
from selene import browser, command
import match

def test_cpmplete_todo():
    browser.open('/')
    browser.element('#firstName').type('Viktor')
    browser.element('#lastName').type('Coy')
    browser.element('#userEmail').type('Coy@gmail.com')
    browser.element('.custom-control-label[for="gender-radio-1"]').click()
    browser.element('#userNumber').type(2340823094)
    browser.element('#dateOfBirthInput').click()
    browser.element(".react-datepicker__year-select [value='1988']").click()
    browser.element(".react-datepicker__month-select [value='3']").click()
    browser.element('.react-datepicker__day--013').click()
    browser.element('#subjectsInput').type('Arts').press_enter()
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('label[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('img/WoWScrnShot_012423_172906.jpg'))
    browser.element('#currentAddress').type('Moscow newer sleep')
    browser.element('#state').click()
    browser.all("#state div").element_by(match.exact_text("Uttar Pradesh")).click()
    browser.element('#city').click()
    browser.all('#city div').element_by(match.exact_text("Lucknow")).click()
    browser.element('#submit').perform(command.js.click)


    # browser.element('.modal-header').should(match.exact_text('Thanks for submitting the form'))
    # browser.all('.modal-body tr td')[1].should(match.exact_text('Viktor Coy'))
    # browser.all('.modal-body tr td')[3].should(match.exact_text('Coy@gmail.com'))
    # browser.all('.modal-body tr td')[5].should(match.exact_text('Male'))
    # browser.all('.modal-body tr td')[7].should(match.exact_text('2340823094'))
    # browser.all('.modal-body tr td')[9].should(match.exact_text('13 April,1988'))
    # browser.all('.modal-body tr td')[11].should(match.exact_text('Arts'))
    # browser.all('.modal-body tr td')[13].should(match.exact_text('Sports, Reading, Music'))
    # browser.all('.modal-body tr td')[15].should(match.exact_text('WoWScrnShot_012423_172906.jpg'))
    # browser.all('.modal-body tr td')[17].should(match.exact_text('Moscow newer sleep'))
    # browser.all('.modal-body tr td')[19].should(match.exact_text('Uttar Pradesh Lucknow'))
    # browser.element('#closeLargeModal').click()

    browser.element('.table').all('td').even.should(
        match.exact_texts(
            'Viktor Coy',
            'Coy@gmail.com',
            'Male',
            '2340823094',
            '13 April,1988',
            'Arts',
            'Sports, Reading, Music',
            'WoWScrnShot_012423_172906.jpg',
            'Moscow newer sleep',
            'Uttar Pradesh Lucknow',
        )
    )