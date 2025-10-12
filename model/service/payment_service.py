from model.repository.payment_repository import PaymentRepository


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
