from model import PaymentRepository


class PaymentService:
    def __init__(self):
        self.repository = PaymentRepository()

    def save(self, payment):
        return self.repository.save(payment)

    def update(self, payment):
        payment_result = self.repository.find_by_id(payment.id)
        if payment_result:
            self.repository.update(payment)
            return payment
        else:
            raise Exception("Payment Not Found !!!")

    def delete(self, payment_id):
        payment = self.repository.find_by_id(payment_id)
        if payment:
            self.repository.delete(payment_id)
            return payment
        else:
            raise Exception("Payment Not Found !!!")

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, payment_id):
        payment = self.repository.find_by_id(payment_id)
        if payment:
            return payment
        else:
            raise Exception("Payment Not Found !!!")

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
