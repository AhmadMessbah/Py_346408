class WarehouseTransaction:
    def __init__(self, id, product_id, quantity, transaction_type, transaction_datetime, customer_id, employee_id):
        self.id = id
        self.product_id = product_id
        self.quantity = quantity
        self.transaction_type = transaction_type
        self.transaction_datetime = transaction_datetime
        self.customer_id = customer_id
        self.employee_id = employee_id

    def __repr__(self):
        return f'{self.__dict__}'
