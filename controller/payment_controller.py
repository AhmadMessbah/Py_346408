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
            return False, "Save Error"

    def update(self, id, transaction_type, payment_type, date_time, customer_id, total_amount, employee_id,
               description):
        try:
            payment = Payment(id, transaction_type, payment_type, date_time, customer_id, total_amount, employee_id,
                              description)
            service = PaymentService()
            service.update(payment)
            return True, f"Payment Updated Successfully \n{payment}"
        except Exception as e:
            return False, "Update Error"

    def delete(self, id):
        try:
            service = PaymentService()
            service.delete(id)
            return True, f"Payment with Id {id} delete successfully"
        except Exception as e:
            return False, "delete Error"

    def find_all(self):
        try:
            service = PaymentService()
            payment_list = service.find_all()
            return True, payment_list
        except Exception as e:
            return False, "Find All Error"

    def find_by_id(self, id):
        try:
            service = PaymentService()
            payment = service.find_by_id(id)
            return True, payment
        except Exception as e:
            return False, "Find By Id Error"
