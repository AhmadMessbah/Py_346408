from model.repository.bank_repository import BankRepository

class BankService:
    def __init__(self):
        self.repository = BankRepository()

    def save(self, bank):
        self.repository.save(bank)

    def update(self, bank):
        self.repository.update(bank)

    def delete(self, bank_id):
        self.repository.delete(bank_id)

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, bank_id):
        return self.repository.find_by_id(bank_id)
