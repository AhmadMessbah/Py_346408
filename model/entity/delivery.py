class Delivery:
    def __init__(self, id, first_name, last_name, address, description):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.description = description

    def __repr__(self):
        return f'{self.__dict__}'
    def to_tuple(self):
        return (self.id, self.first_name, self.last_name, self.address, self.description)
