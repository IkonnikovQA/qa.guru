from demoqa_tests.application_manager import ApplicationManager
from demoqa_tests.data.users import User

user1 = User(name='Stepan Ivanov', email='nonexisting@reallynonexisting.com', current_address='Test str. 8',
             permanent_address='Prod str. 11')

user2 = User.with_mandatory_fields(email='mvp@mvp.com', current_address='Test1', permanent_address='Test2')

user3 = User.random_with_all_fields()
user4 = User.random_with_all_fields()

app = ApplicationManager()


def test_simplified_form_all_fields_filled_and_valid():
    app.left_panel.open_simplified_reg_form()
    app.simplified_reg_form.send_form(user1)
    app.simplified_reg_form.should_have_data_retrieved(user1)


def test_simplified_form_no_name():
    app.left_panel.open_simplified_reg_form()
    app.simplified_reg_form.send_form(user2)
    app.simplified_reg_form.should_have_data_retrieved(user2)


def test_simplified_form_random_all_fields():
    app.left_panel.open_simplified_reg_form()
    app.simplified_reg_form.send_form(user3)
    app.simplified_reg_form.should_have_data_retrieved(user3)