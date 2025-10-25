from tools.financial_transaction_validator import *


class FinancialTransaction:
    def __init__(self, financial_transaction_id, transaction_type, customer_id , employee_id, amount, date_time, payment_id, description = ""):
        self.financial_transaction_id = financial_transaction_id
        self.transaction_type = transaction_type        # فروش / خرید / هزینه / حقوق
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.amount = amount
        self.date_time = date_time
        self.payment_id = payment_id
        self.description = description

    def validatte(self):
        transaction_type_validator(self.transaction_type)
        customer_id_validator(self.customer_id)
        employee_id_validator(self.employee_id)
        amount_validator(self.amount)
        date_time_validator(self.date_time)
        payment_id_validator(self.payment_id)
        description_validator(self.description)

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.financial_transaction_id,self.transaction_type,self.customer_id,self.employee_id,self.amount,self.date_time,self.payment_id,self.description))