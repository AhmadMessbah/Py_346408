from model.entity.payment import Payment
from model.service.payment_service import PaymentService


class PaymentController:

    def save(self, transaction_type, payment_type, date_time, customer_id, total_amount, employee_id, description):
        try:
            payment = Payment(None, transaction_type, payment_type, date_time, customer_id, total_amount, employee_id,
                              description)
            print("zakhire shod, ok")
            service = PaymentService()
            service.save(payment)
            return True, "Saved"
        except:
            return False, "Save Error"

    def update(self, transaction_type, payment_type, date_time, customer_id, total_amount, employee_id, description):
        try:
            payment = Payment(None, transaction_type, payment_type, date_time, customer_id, total_amount, employee_id,
                              description)
            service = PaymentService()
            service.update(payment)
            return True, "updated"
        except:
            return False, "update Error"

    def delete(self, id):
        try:
            service = PaymentService()
            service.delete(id)
            return True, "Deleted"
        except:
            return False, "Delete Error"

    def find_all(self):
        try:
            service = PaymentService()
            service.find_all(self)
            return self, "Found"
        except:
            return False, "Find Error"

    def find_by_id(self, id):
        try:
            service = PaymentService()
            service.find_by_id(self, id)
            return self, "Has Been Find"
        except:
            return False, "Find Error"
