class FinancialTransaction:
    def __init__(self,id,transaction_type, customer_id , employee_id, amount, date_time,payment_id,description):
        self.id = id
        self.transaction_type = transaction_type        # فروش / خرید / هزینه / حقوق
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.amount = amount
        self.date_time = date_time
        self.payment_id = payment_id
        self.description = description

    def __repr__(self):
        return f"{self.__dict__}"
    def to_tuple(self):
        return tuple((self.id,self.transaction_type,self.customer_id,self.employee_id,self.amount,self.date_time,self.payment_id,self.description))