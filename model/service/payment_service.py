from model import PaymentRepository


class PaymentService:
    def __init__(self):
        self.repository = PaymentRepository()

    def save(self, payment):
        self.repository.save(payment)

    def update(self, payment):
        self.repository.update(payment)

    def delete(self, id):
        self.repository.delete(id)

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, id):
        return self.repository.find_by_id(id)

    def find_by_transaction_type(self, transaction_type):
        return self.repository.find_by_transaction_type(transaction_type)

    def find_by_payment_type(self, payment_type):
        return self.repository.find_by_payment_type(payment_type)

    def find_by_date_time_range(self, start_date_time, end_date_time):
        return self.repository.find_by_date_time_range(start_date_time, end_date_time)

    def find_by_date_time_range_and_customer_id(self, start_date_time, end_date_time, customer_id):
        return self.find_by_date_time_range_and_customer_id(start_date_time, end_date_time, customer_id)

    def find_by_date_time_range_and_employee_id(self, start_date_time, end_date_time, employee_id):
        return self.find_by_date_time_range_and_employee_id(start_date_time, end_date_time, employee_id)
