from model.entity.bank import Bank
from model.service.bank_service import BankService

bank = Bank(1, "melat", None, None, None)
service = BankService()
service.save(bank)
service.update(bank)
service.delete(id)
print(service.find_all())
print(service.find_by_id(id))