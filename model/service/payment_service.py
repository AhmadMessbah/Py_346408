from model.repository.payment_repository import PaymentRepository


class PaymentService:
    def __init__(self):
        self.repository = PaymentRepository()

    def save(self, payment):
        self.repository.save(payment)

    def update(self, payment):
        self.repository.update(payment)

    def delete(self, payment_id):
        self.repository.delete(payment_id)

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, payment_id):
        return self.repository.find_by_id(payment_id)
