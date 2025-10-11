# model/service/bank_service.py

from model.repository.bank_repository import BankRepository

class BankService:
    def __init__(self):
        self.repository = BankRepository()

    def save(self, bank):
        self.repository.add_bank(bank)

    def update(self, bank):
        self.repository.update_bank(bank)

    def delete(self, bank_id):
        self.repository.delete_bank(bank_id)

    def find_all(self):
        return self.repository.list_banks()

    def find_by_id(self, bank_id):
        return self.repository.get_bank_by_id(bank_id)
