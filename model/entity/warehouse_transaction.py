from tools.warehouse_transaction_validator import *

class WarehouseTransaction:
    def __init__(self, id, product_id, quantity, transaction_type, transaction_datetime, customer_id, employee_id):
        self.id = id
        self.product_id = product_id
        self.quantity = quantity
        self.transaction_type = transaction_type
        self.transaction_datetime = transaction_datetime
        self.customer_id = customer_id
        self.employee_id = employee_id

    def validate(self):
        product_id_validator(self.product_id)
        quantity_validator(self.quantity)
        transaction_type_validator(self.transaction_type)
        datetime_validator(self.transaction_datetime)
        customer_id_validator(self.customer_id)
        employee_id_validator(self.employee_id)

    def __repr__(self):
        return f'{self.__dict__}'

    def to_tuple(self):
        return tuple(self.id, self.product_id, self.quantity, self.transaction_type, self.transaction_datetime,self.customer_id, self.employee_id)