from dataclasses import dataclass
from mimesis import Person, Address
from mimesis.locales import Locale

person = Person(Locale.EN)
address = Address(Locale.EN)
address2 = Address(Locale.EN)


@dataclass
class User:
    name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None

    @staticmethod
    def with_mandatory_fields(email, current_address, permanent_address):
        return User(email=email, current_address=current_address, permanent_address=permanent_address)

    @staticmethod
    def random_with_all_fields():
        return User(name=person.full_name(), email=person.email(), current_address=address.address(),
                    permanent_address=address2.address())