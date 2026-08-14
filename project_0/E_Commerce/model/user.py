class User:
    def __init__(
        self,
        user_id,
        name,
        email,
        address=None,
        city=None,
        postal_code=None,
        country=None
    ):
        self._user_id = user_id
        self._name = name
        self._email = email
        self._address = address
        self._city = city
        self._postal_code = postal_code
        self._country = country

    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def address(self):
        return self._address

    @property
    def city(self):
        return self._city

    @property
    def postal_code(self):
        return self._postal_code

    @property
    def country(self):
        return self._country

    def get_full_name(self):
        return self._name

    def display_info(self):
        return {
            "user_id": self._user_id,
            "name": self._name,
            "Email": self._email,
            "Address": self._address,
            "City": self._city,
            "Postal Code": self._postal_code,
            "Country": self._country
        }


class Customer(User):

    def __init__(
        self,
        user_id,
        name,
        email,
        contact_name=None,
        address=None,
        city=None,
        postal_code=None,
        country=None
    ):
        super().__init__(
            user_id,
            name,
            email,
            address,
            city,
            postal_code,
            country
        )
        self._contact_name = contact_name

    @property
    def contact_name(self):
        return self._contact_name

    def get_role(self):
        return "CUSTOMER"

    def display_info(self):
        info = super().display_info()
        info["Contact Name"] = self._contact_name
        return info


class Admin(User):

    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)

    def get_role(self):
        return "ADMIN"