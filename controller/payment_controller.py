from model.entity.payment import Payment
from model.service.payment_service import PaymentService


class PaymentController:
    def save(self,transaction_type,payment_type,date_time,customer_id,total_amount,employee_id,description):
        try:
            payment = Payment(None,transaction_type,payment_type,date_time,customer_id,total_amount,employee_id,description)
            print("Ali darkhaste zakhire kard, ok")
            service = PaymentService()
            service.save(payment)
            return True, "Saved"
        except:
            return False, "Save Error"

    def update(self,id,transaction_type,payment_type,date_time,customer_id,total_amount,employee_id,description):
        try:
            payment = Payment(None,transaction_type,payment_type,date_time,customer_id,total_amount,employee_id,description)
            service = PaymentService()
            service.update(payment)
            return True, "Updated successfully"
        except:
            return False, "Update Error"

    def delete(self, id):
        try:
            service = PaymentService()
            service.delete(id)
            return True, f"payment with ID {id} delete successfully"
        except:
            return False, "delete Error"

    def find_all(self):
        try:
            service = PaymentService()
            payments = service.find_all()
            return True, payments
        except:
            return False, "Find All Error"

    def find_by_id(self, id):
        try:
            service = PaymentService()
            payment = service.find_by_id(id)
            return True, payment
        except:
            return False, "Find By ID Error"