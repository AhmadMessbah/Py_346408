from model.entity.bank import Bank
from model.service.bank_service import BankService

bank = Bank(1, "saderat", "15000", 2500, "tozih jadid")

service = BankService()

# test passed
# service.save(bank)

# test passed
# service.update(bank)

# test passed
# service.delete(id)

# test passed
# print(service.find_all())

# test passed
# print(service.find_by_id())