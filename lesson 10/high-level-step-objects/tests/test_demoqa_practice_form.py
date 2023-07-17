from demoqa_tests.models.pages.registration_page import RegistrationPage
from demoqa_tests.data.users import User, Gender, DateOfBirth, Hobby

user1 = User(first_name='Stepan', last_name='Ivanov', mobile_number='1234567890',
             email='nonexisting@reallynonexisting.nono', gender=Gender.male, date_of_birth=DateOfBirth('08 Aug 1991'),
             hobbies=[Hobby.sports, Hobby.reading], picture='test.jpeg', current_address='Test str. 8',
             subjects='Computer Science, Maths',
             state='NCR', city='Delhi')


def test_high():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register(user1)
    registration_page.should_have_registered(user1)

# user2 = User(first_name='Stepan', last_name='Ivanov', mobile_number='1234567890',
#              email='nonexisting@reallynonexisting.nono', gender=Gender.male, date_of_birth=DateOfBirth('08 Aug 1991'),
#              hobbies=[Hobby.sports], current_address='Test str. 8', subjects='Computer Science, Maths', state='NCR',
#              city='Delhi')
#
# user3 = User(first_name='Stepan', last_name='Ivanov', mobile_number='1234567890',
#              email='nonexisting@reallynonexisting.nono', gender=Gender.male, date_of_birth=DateOfBirth('08 Aug 1991'),
#              hobbies=[Hobby.sports], subjects='Computer Science, Maths', state='NCR',
#              city='Delhi', picture='test.jpeg')
#
# def test_high_no_picture():
#     registration_page = RegistrationPage()
#     registration_page.open()
#     registration_page.register(user2)
#     registration_page.should_have_registered(user2)
#
# def test_high_no_address():
#     registration_page = RegistrationPage()
#     registration_page.open()
#     registration_page.register(user3)
#     registration_page.should_have_registered(user3)