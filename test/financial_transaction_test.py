from model import FinancialTransaction
from model import FinancialTransactionService


financial_transaction1=FinancialTransaction(1,"cash",10,10,50000,"20/10/1404",14)
service = FinancialTransactionService()

financial_transaction2=FinancialTransaction(2,"credit",14,11,150000,"20/11/1404",15)
service = FinancialTransactionService()

financial_transaction3=FinancialTransaction(3,"internal",18,12,785000,"20/12/1404",17)
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

# test
print(service.find_by_transaction_type("internal"))

#test
#print(service.find_by_customer_id(18))

#test
#print(service.find_by_employee_id(12))

#test
#print(service.find_by_payment_id(17))

#test
#print(service.find_by_date_time_range())

#test
#service.find_by_date_time_range_and_customer_id()

#




#controller = FinancialTransactionController()
# print(controller.save(1, 2, 3, 4, 5, 7, 7))
#print(controller.update(1, 100, 200, 300, 400, 500, 600, 700))