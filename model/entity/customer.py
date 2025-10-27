from tools.customer_validator import first_name_validator, last_name_validator, phone_number_validator, \
    address_validator #


class Customer:
    def __init__(self, id, first_name, last_name, phone_number, address):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address


    def validate(self):
        first_name_validator(self.first_name)
        last_name_validator(self.last_name)
        phone_number_validator(self.phone_number)
        address_validator(self.address)

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(
            (self.id, self.first_name, self.last_name, self.phone_number, self.address))
