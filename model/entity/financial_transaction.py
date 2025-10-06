class FinancialTransaction:
    def __init__(self, customer , employee, amount, date,description,transaction_type):
        self.customer = customer
        self.employee = employee
        self.amount = amount
        self.date = date
        self.description = description
        self.transaction_type = transaction_type

    def __repr__(self):
        return f"{self.__dict__}"