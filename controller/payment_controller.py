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

    def update(self, payment):
        pass

    def delete(self, id):
        pass

    def find_all(self):
        pass

    def find_by_id(self, id):
        pass
