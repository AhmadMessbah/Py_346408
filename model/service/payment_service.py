from model.repository.payment_repository import PaymentRepository


class PaymentService:
    def __init__(self):
        self.repository = PaymentRepository()

    def save(self, payment_id,
             document_type,
             transaction_type,
             date_time,
             customer_id,
             total_amount,
             items_list,
             description):
        self.repository.save(payment_id,
                             document_type,
                             transaction_type,
                             date_time,
                             customer_id,
                             total_amount,
                             items_list,
                             description)

    def update(self,
               payment_id,
               document_type,
               transaction_type,
               date_time,
               customer_id,
               total_amount,
               items_list,
               description):
        self.repository.update(payment_id,
                               document_type,
                               transaction_type,
                               date_time,
                               customer_id,
                               total_amount,
                               items_list,
                               description)

    def delete(self, payment_id):
        self.repository.delete(payment_id)

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, payment_id):
        return self.repository.find_by_id(payment_id)
