from model import Payment, PaymentService


class PaymentController:
    def save(self, transaction_type, payment_type, date_time, customer_id, total_amount, employee_id, description):
        try:
            payment = Payment(None, transaction_type, payment_type, date_time, customer_id, total_amount, employee_id,
                              description)
            service = PaymentService()
            service.save(payment)
            return True, f"Payment Saved Successfully \n{payment}"
        except Exception as e:
            return False, e

    def update(self, id, transaction_type, payment_type, date_time, customer_id, total_amount, employee_id,
               description):
        try:
            payment = Payment(id, transaction_type, payment_type, date_time, customer_id, total_amount, employee_id,
                              description)
            service = PaymentService()
            service.update(payment)
            return True, f"Payment Updated Successfully \n{payment}"
        except Exception as e:
            return False, e

    def delete(self, id):
        try:
            service = PaymentService()
            service.delete(id)
            return True, f"Payment with Id {id} delete successfully"
        except Exception as e:
            return False, e

    def find_all(self):
        try:
            service = PaymentService()
            payment_list = service.find_all()
            return True, payment_list
        except Exception as e:
            return False, e

    def find_by_id(self, id):
        try:
            service = PaymentService()
            payment = service.find_by_id(id)
            return True, payment
        except Exception as e:
            return False, e

    def find_by_transaction_type(self, transaction_type):
        try:
            service = PaymentService()
            return True, service.find_by_transaction_type(transaction_type)
        except Exception as e:
            return False, e

    def find_by_payment_type(self, payment_type):
        try:
            service = PaymentService()
            return True, service.find_by_payment_type(payment_type)
        except Exception as e:
            return False, e

    def find_by_date_time_range(self, start_date_time, end_date_time):
        try:
            service = PaymentService()
            return True, service.find_by_date_time_range(start_date_time, end_date_time)
        except Exception as e:
            return False, e

    def find_by_date_time_range_and_customer_id(self, start_date_time, end_date_time, customer_id):
        try:
            service = PaymentService()
            return True, service.find_by_date_time_range_and_customer_id(start_date_time, end_date_time, customer_id)
        except Exception as e:
            return False, e

    def find_by_date_time_range_and_employee_id(self, start_date_time, end_date_time, employee_id):
        try:
            service = PaymentService()
            return True, service.find_by_date_time_range_and_employee_id(start_date_time, end_date_time, employee_id)
        except Exception as e:
            return False, e
