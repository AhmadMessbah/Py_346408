from model.entity.bank import Bank
from model.service.bank_service import BankService

class BankController:
    def save(self, name, account, balance, description):
        try:
           bank = Bank(None, name, account, balance, description)
           print("bank added, ok")
           service = BankService()
           service.save(bank)
           return True, "Saved"
        except:
            return False, "Save Error"

    def update(self , name, account, balance, description):
        try:
            #id
            bank = Bank( name, account, balance, description)
            service = BankService()
            service.update(bank)
            return True, "Updated Successfully"
        except:
            return False, "Update Error"


    def delete(self, id):
        try:
            service = BankService()
            service.delete(id)
            return True, f"Bank_id with ID {id} deleted successfully"
        except:
            return False, "Delete Error"


    def find_all(self):
        try:
            service = BankService()
            bank = service.find_all()
            return True, bank
        except:
            return False, "Find All Error"


    def find_by_id(self, id):
        try:
            service = BankService()
            bank = service.find_by_id(id)
            return True, bank
        except:
            return False, "Find By ID Error"
