from demoqa_tests.models.pages.registration_page import RegistrationPage


def test_new_user_all_fields_all_valid():
    # GIVEN
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Stepan')
    registration_page.fill_last_name('Ivanov')
    registration_page.fill_email('nonexisting@reallynonexisting.nono')
    registration_page.fill_gender('Male')
    registration_page.fill_mobile_number('1234567890')
    registration_page.fill_date_of_birth('1991', 'August', '08')

    registration_page.fill_subject('Computer Science')
    registration_page.fill_hobby('Sports')
    registration_page.upload_picture('WoWScrnShot_012423_172906.jpg')

    registration_page.fill_current_address('Test str. 8')
    registration_page.fill_state('NCR')
    registration_page.fill_city('Delhi')

    registration_page.submit_form()

    # THEN
    registration_page.should_have_modal_with('Thanks for submitting the form')
    registration_page.should_have_registered_user_with(
        'Stepan Ivanov',
        'nonexisting@reallynonexisting.nono',
        'Male',
        '1234567890',
        '08 August,1991',
        'Computer Science',
        'Sports',
        'WoWScrnShot_012423_172906.jpg',
        'Test str. 8',
        'NCR Delhi')

    # WHEN
    registration_page.close_modal()

    # THEN
    registration_page.should_not_have_modal()
    registration_page.should_be_cleared()