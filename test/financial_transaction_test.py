from model.entity.bank import Bank
from model.service.bank_service import BankService

financial_transaction=FinancialTransaction(1, "saderat", "15000", 2500, "tozih jadid")

service = FinancialTransactionService()

# test passed
# service.save(financial_transaction)

# test passed
# service.update(financial_transaction)

# test passed
# service.delete(id)

# test passed
# print(service.find_all())

# test passed
# print(service.find_by_id())