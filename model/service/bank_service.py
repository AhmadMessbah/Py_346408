from model import BankRepository


class BankService:
    def __init__(self):
        self.repository = BankRepository()

    def save(self, bank):
        return self.repository.save(bank)

    def update(self, bank):
        bank = self.repository.find_by_id(bank.id)
        if bank:
            self.repository.update(bank)
            return bank
        else:
            raise Exception("Bank Not Found !!!")

    def delete(self, bank_id):
        bank = self.repository.find_by_id(bank_id)
        if bank:
            self.repository.delete(bank_id)
            return bank
        else:
            raise Exception("Bank Not Found !!!")

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, bank_id):
        bank = self.repository.find_by_id(bank_id)
        if bank:
            return bank
        else:
            raise Exception("Bank Not Found !!!")

    def find_by_name(self, name):
        return self.repository.find_by_name(name)

    def find_by_account(self, account):
        return self.repository.find_by_account(account)
