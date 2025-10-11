from model.entity.bank import Bank
from model.service.bank_service import BankService

financial_transaction=FinancialTransaction("debtor",20,10,1000,"20/10/1404",1,"episode")

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