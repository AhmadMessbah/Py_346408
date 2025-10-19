class Payment:
    def __init__(self, id, transaction_type, payment_type, date_time, customer_id, total_amount, employee_id, description):
        self.id = id
        self.transaction_type = transaction_type
        self.payment_type = payment_type
        self.date_time = date_time
        self.customer_id = customer_id
        self.total_amount = total_amount
        self.employee_id = employee_id
        self.description = description

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(
            (self.id, self.transaction_type, self.payment_type,
             self.date_time, self.customer_id, self.total_amount, self.employee_id, self.description))
