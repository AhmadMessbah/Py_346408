from model.entity.bank import Bank
from model.service.bank_service import BankService

bank = Bank(1, "melat", None, None, None)
sample_service = BankService()
sample_service.save(bank)
sample_service.update(bank)
sample_service.delete(id)
print(sample_service.find_all())
print(sample_service.find_by_id(id))