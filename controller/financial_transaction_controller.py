from model.entity.financial_transaction import FinancialTransaction
from model.service.financial_transaction_service import FinancialTransactionService

class FinancialTransactionController:
    def save(self,transaction_type, customer_id , employee_id, amount, date_time,payment_id,description):
        try:
           financial_transaction = FinancialTransaction(None,transaction_type, customer_id , employee_id, amount, date_time,payment_id,description)
           #print(" financial_transaction added, ok")
           service = FinancialTransactionService()
           service.save(financial_transaction)
           return True, "Saved"
        except:
            return False, "Save Error"
    def update(self,id, transaction_type, customer_id , employee_id, amount, date_time,payment_id,description):
            try:
                financial_transaction = FinancialTransaction(None, transaction_type, customer_id, employee_id, amount,
                                                             date_time, payment_id, description)
                # print(" financial_transaction added, ok")
                service = FinancialTransactionService()
                service.update(financial_transaction)
                return True, "update Successfully"
            except:
                return False, "update Error"


    def delete(self, id):

            try:
                service = FinancialTransactionService()
                service.delete(id)
                return True, f"Customer with Id {id} delete successfully"
            except:
                return False, "delete Error"


    def find_all(self):
         try:
             service = FinancialTransactionService()
             financial_transaction = service.find_all()
             return True, financial_transaction

         except:
              return False, "Find All Error"


    def find_by_id(self, id):
        try:
             service = FinancialTransactionService()
             financial_transaction_list = service.find_by_id(id)
             return True, financial_transaction_list
        except:
              return False, "Find By ID Error"
