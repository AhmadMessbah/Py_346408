from model.entity.bank import Bank
from model.service.bank_service import BankService
from view.bank_view import *

service = BankService()

# bank1 = Bank(1, "saderat", "saving", 2500, "tozih jadid")
# service.save(bank1)
#
bank2 = Bank(2, "mellat", "card", 2500, "tozih jadid")
service.save(bank2)

# bank3 = Bank(3, "melli", "card", 2500, "tozih jadid")
# service.save(bank3)

print(service.find_by_name("mellat"))
# print(service.find_by_account("saving2"))


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

