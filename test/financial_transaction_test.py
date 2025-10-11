from model.entity.financial_transaction import FinancialTransaction
from model.service.financial_transaction_service import FinancialTransactionService

financial_transaction=FinancialTransaction()

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