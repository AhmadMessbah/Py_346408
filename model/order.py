from tools.order_validator import *

def _get_customer_service():
    from service import CustomerService
    return CustomerService()

class Order:
    def __init__(self, order_id, order_type, customer_id, employee_id, date_time,
                 payment_id, warehouse_transaction_id, tax=None, total_discount=None,
                 total_amount=None):

        self.order_id = order_id
        self.order_type = order_type
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.date_time = date_time
        self.payment_id = payment_id
        self.warehouse_transaction_id = warehouse_transaction_id
        self.tax = tax
        self.total_discount = total_discount
        self.total_amount = total_amount

    def validate(self):
        datetime_validator(self.date_time)
        tax_validator(self.tax)
        total_discount_validator(self.total_discount)
        total_amount_validator(self.total_amount)

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):

        customer_service = _get_customer_service()
        customer = customer_service.find_by_id(self.customer_id)

        # employee_service = EmployeeService()
        # employee = employee_service.find_by_id(self.employee_id)[0]

        return tuple((
            self.order_id,
            self.order_type,
            self.customer_id,
            self.employee_id,
            self.date_time,
            self.payment_id,
            self.warehouse_transaction_id,
            self.tax,
            self.total_discount,
            self.total_amount))
