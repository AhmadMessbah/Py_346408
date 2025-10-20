from model import FinancialTransaction, FinancialTransactionService

class FinancialTransactionController:
    def save(self, transaction_type, customer_id, employee_id, amount, date_time, payment_id, description):
        try:
            financial_transaction = FinancialTransaction(None, transaction_type, customer_id, employee_id, amount,
                                                         date_time, payment_id, description)
            service = FinancialTransactionService()
            service.save(financial_transaction)
            return True, "Saved"
        except Exception as e:
            return False, "Save Error"

    def update(self, id, transaction_type, customer_id, employee_id, amount, date_time, payment_id, description):
        try:
            financial_transaction = FinancialTransaction(id, transaction_type, customer_id, employee_id, amount,
                                                         date_time, payment_id, description)
            service = FinancialTransactionService()
            service.update(financial_transaction)
            return True, "update Successfully"
        except Exception as e:
            return False, e

    def delete(self, id):

        try:
            service = FinancialTransactionService()
            service.delete(id)
            return True, f"Customer with Id {id} delete successfully"
        except Exception as e:
            return False, "delete Error"

    def find_all(self):
        try:
            service = FinancialTransactionService()
            financial_transaction = service.find_all()
            return True, financial_transaction

        except Exception as e:
            return False, "Find All Error"

    def find_by_id(self, id):
        try:
            service = FinancialTransactionService()
            financial_transaction_list = service.find_by_id(id)
            return True, financial_transaction_list
        except Exception as e:
            return False, "Find By Id Error"
