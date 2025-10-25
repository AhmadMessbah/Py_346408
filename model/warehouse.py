from tools.warehouse_validator import *

class Warehouse:
    def __init__(self, warehouse_id, product_id, quantity):

        self.warehouse_id = warehouse_id
        self.product_id = product_id
        self.quantity = quantity

    def validate(self):
        product_id_validator(self.product_id)
        quantity_validator(self.quantity)

    def __repr__(self):
        return f'{self.__dict__}'

    def to_tuple(self):
        return tuple((self.warehouse_id, self.product_id, self.quantity))




