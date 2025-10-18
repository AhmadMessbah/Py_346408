from controller.financial_transaction_controller import FinancialTransactionController
from model.entity.financial_transaction import FinancialTransaction
from model.service.financial_transaction_service import FinancialTransactionService

# financial_transaction=FinancialTransaction("debtor",20,10,1000,"20/10/1404",1,"episode")
#
# service = FinancialTransactionService()

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


controller = FinancialTransactionController()
# print(controller.save(1, 2, 3, 4, 5, 7, 7))
print(controller.update(1, 100, 200, 300, 400, 500, 600, 700))