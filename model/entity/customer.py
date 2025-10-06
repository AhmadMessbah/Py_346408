class Customer:
    def __init__(self, id, first_name, last_name, phone_number, address):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address

    def __repr__(self):
        return f"{self.__dict__}"