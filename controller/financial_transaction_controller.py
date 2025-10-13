from model.entity.financial_transaction import FinancialTransaction
from model.service.financial_transaction_service import FinancialTransactionService

class FinancialTransactionController:
    def save(self,transaction_type, customer_id , employee_id, amount, date_time,payment_id,description):
        try:
            financial_transaction = FinancialTransaction(None,transaction_type, customer_id , employee_id, amount, date_time,payment_id,description)
           print(" financial_transaction added, ok")
           service = FinancialTransactionService()
           service.save(financial_transaction)
           return True, "Saved"
        except:
            return False, "Save Error"
    def update(self,transaction_type, customer_id , employee_id, amount, date_time,payment_id,description):
        try:
            #id
             financial_transaction = FinancialTransaction(None, transaction_type, customer_id, employee_id, amount, date_time, payment_id,
                                 description)
             service = FinancialTransactionService()
             service.update(financial_transaction)

             return True, "Updated Successfully"
        except:
             return False, "Update Error"


    def delete(self, id):
         try:
             service =FinancialTransactionService()
             service.delete(id)
             return True, f"FinancialTransaction_id with ID {id} deleted successfully"
        except:
              return False, "Delete Error"


    def find_all(self):
         try:
             service = FinancialTransactionService()
             bank = service.find_all()
         return True, financial_transaction

         except:
              return False, "Find All Error"


    def find_by_id(self, id):
        try:
             service = FinancialTransactionService()
             financial_transaction = service.find_by_id(id)
             return True, financialtransaction
        except:
              return False, "Find By ID Error"
