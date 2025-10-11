class Order:

    def __init__(self, id, order_type, customer_id, employee_id, date_time,
                 payment_id, warehouse_transaction_id, tax=None, total_discount=None,
                 total_amount=None):

        self.id = id
        self.order_type = order_type
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.date_time = date_time
        self.payment_id = payment_id
        self.warehouse_transaction_id = warehouse_transaction_id
        self.tax = tax
        self.total_discount = total_discount
        self.total_amount = total_amount

    def __repr__(self):
        return f"{self.__dict__}"
