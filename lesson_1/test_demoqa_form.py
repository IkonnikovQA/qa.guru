from selene.core import command
from selene import browser, have

browser.config.window_width = 2000
browser.config.window_height = 1700
def test_demoqa_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.all('footer').perform(command.js.remove)
    browser.element("[id='firstName']").send_keys("Soska")
    browser.element("[id='lastName']").send_keys('Nerealka')
    browser.element('[id="userEmail"]').send_keys('onlyfans@gmail.com')
    browser.element('[for="gender-radio-3"]').click()
    browser.element("[id='userNumber']").send_keys("1231233423")
    browser.element("[id='dateOfBirthInput']").click()
    browser.element(".react-datepicker__month-select [value='2']").click()
    browser.element(".react-datepicker__year-select [value='1992']").click()
    browser.element('.react-datepicker [aria-label="Choose Saturday, March 21st, 1992"]').click()
    browser.element('[id="subjectsInput"]').send_keys("MMMMMM")
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('[id="uploadPicture"]').send_keys("C:/Users/atlet/PycharmProjects/pythonProject1/pythonProject/qa.guru/lesson_1/paint/WoWScrnShot_012423_172906.jpg")
    browser.element('[id="currentAddress"]').type('chikago john')
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('[id="react-select-3-option-1"]').click
    # browser.element('[id="city"]').click()
    # browser.element('[id="react-select-4-option-1"]').click()
    # browser.element('[id="submit"]').click()
    # browser.element('[id="closeLargeModal"]').click()