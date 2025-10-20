from tools.warehouse_validator import *

class Warehouse:
    def __init__(self, id, product_id, quantity):

        self.id = id
        self.product_id = product_id
        self.quantity = quantity

    def validate(self):
        product_id_validator(self.product_id)
        quantity_validator(self.quantity)

    def __repr__(self):
        return f'{self.__dict__}'

    def to_tuple(self):
        return tuple((self.id, self.product_id, self.quantity))




