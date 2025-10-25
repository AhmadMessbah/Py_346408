from model import Bank, BankService
from tools.logging import Logger


class BankController:
    bank_service = BankService()

    @classmethod
    def save(cls, name, account, balance, description):
        try:
            bank = Bank(None, name, account, balance, description)
            bank.validate()
            bank = cls.bank_service.save(bank)
            Logger.info(f"Bank {bank} saved")
            return True, f"Bank Saved Successfully"
        except Exception as e:
            Logger.error(f"Bank Saved Error: {e}")
            return False, e

    @classmethod
    def update(cls, bank_id, name, account, balance, description):
        try:
            bank = Bank(bank_id, name, account, balance, description)
            bank.validate()
            bank = cls.bank_service.update(bank)
            Logger.info(f"Bank {bank} updated")
            return True, "Bank Updated Successfully"
        except Exception as e:
            Logger.error(f"Bank Updated Error: {e}")
            return False, e

    @classmethod
    def delete(cls, bank_id):
        try:
            bank = cls.bank_service.delete(bank_id)
            Logger.info(f"Bank {bank} deleted")
            return True, f"Bank Deleted Successfully"
        except Exception as e:
            Logger.error(f"Bank Delete Error: {e}")
            return False, e

    @classmethod
    def find_all(cls):
        try:
            bank_list = cls.bank_service.find_all()
            Logger.info("Bank FindAll")
            return True, bank_list
        except Exception as e:
            Logger.error(f"Bank FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, bank_id):
        try:
            bank = cls.bank_service.find_by_id(bank_id)
            Logger.info(f"Bank FindById {bank_id}")
            return True, bank
        except Exception as e:
            Logger.error(f"Bank FindById Error: {e}")
            return False, e

    @classmethod
    def find_by_name(cls, name):
        try:
            bank_list = cls.bank_service.find_by_name(name)
            Logger.info(f"Bank FindByName {name}")
            return True, bank_list
        except Exception as e:
            Logger.error(f"Bank FindByName Error: {e}")
            return False, e

    @classmethod
    def find_by_account(cls, account):
        try:
            bank_list = cls.bank_service.find_by_account(account)
            Logger.info(f"Bank FindByAccount {account}")
            return True, bank_list
        except Exception as e:
            Logger.error(f"Bank FindByAccount Error: {e}")
            return False, e
