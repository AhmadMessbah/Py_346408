from model import Bank, BankService
from tools.logging import Logger


class BankController:
    def save(self, name, account, balance, description):
        try:
           bank = Bank(None, name, account, balance, description)
           bank.validate()
           service = BankService()
           service.save(bank)
           return True,f"Bank Saved Successfully \n{bank}"
        except Exception as e:
            return False, e

    def update(self ,id, name, account, balance, description):
        try:
            bank = Bank(id, name, account, balance, description)
            bank.validate()
            service = BankService()
            service.update(bank)
            return True, "Updated Successfully"
        except Exception as e:
            return False, e


    def delete(self, id):
        try:
            service = BankService()
            service.delete(id)
            return True, f"Bank_id with Id {id} deleted successfully"
        except Exception as e:
            return False, e


    def find_all(self):
        try:
            service = BankService()
            bank = service.find_all()
            return True, bank
        except Exception as e:
            return False, e


    def find_by_id(self, id):
        try:
            service = BankService()
            bank = service.find_by_id(id)
            return True, bank
        except Exception as e:
            return False, e
