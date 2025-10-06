class Payment:
    def __init__(self, payment_id, document_type, transaction_type,date_time, customer_id, total_amount, items_list,description):
        self.payment_id = payment_id
        self.document_type = document_type
        self.Transaction_type = transaction_type
        self.date_time = date_time
        self.customer_id = customer_id
        self.total_amount = total_amount
        self.items_list = items_list
        self.description = description

    def __repr__(self):
        return f"{self.__dict__}"