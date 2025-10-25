from model import FinancialTransaction, FinancialTransactionService
from tools.logging import Logger


class FinancialTransactionController:
    def __init__(self):
        self.financial_transaction_service = FinancialTransactionService()

    def save(self, transaction_type, customer_id, employee_id, amount, date_time, payment_id, description):
        try:
            financial_transaction = FinancialTransaction(None, transaction_type, customer_id, employee_id, amount,
                                                         date_time, payment_id, description)
            financial_transaction = self.financial_transaction_service.save(financial_transaction)
            Logger.info(f"FinancialTransaction {financial_transaction} saved")
            return True, f"FinancialTransaction Saved Successfully"
        except Exception as e:
            Logger.error(f"FinancialTransaction Save Error: {e}")
            return False, e

    def update(self, financial_transaction_id, transaction_type, customer_id, employee_id, amount, date_time, payment_id, description):
        try:
            financial_transaction = FinancialTransaction(financial_transaction_id, transaction_type, customer_id, employee_id, amount,
                                                         date_time, payment_id, description)
            financial_transaction = self.financial_transaction_service.update(financial_transaction)
            Logger.info(f"FinancialTransaction {financial_transaction} updated")
            return True, "FinancialTransaction Updated Successfully"
        except Exception as e:
            Logger.error(f"FinancialTransaction Update Error: {e}")
            return False, e

    def delete(self, financial_transaction_id):
        try:
            financial_transaction = self.financial_transaction_service.delete(financial_transaction_id)
            Logger.info(f"FinancialTransaction {financial_transaction} deleted")
            return True, f"FinancialTransaction Deleted Successfully"
        except Exception as e:
            Logger.error(f"FinancialTransaction Delete Error: {e}")
            return False, e

    def find_all(self):
        try:
            financial_transaction_list = self.financial_transaction_service.find_all()
            Logger.info("FinancialTransaction FindAll")
            return True, financial_transaction_list
        except Exception as e:
            Logger.error(f"FinancialTransaction FindAll Error: {e}")
            return False, e

    def find_by_id(self, financial_transaction_id):
        try:
            financial_transaction = self.financial_transaction_service.find_by_id(financial_transaction_id)
            Logger.info(f"FinancialTransaction FindById {financial_transaction_id}")
            return True, financial_transaction
        except Exception as e:
            Logger.error(f"FinancialTransaction FindById Error: {e}")
            return False, e

    def find_by_transaction_type(self, transaction_type):
        try:
            financial_transaction_list = self.financial_transaction_service.find_by_transaction_type(transaction_type)
            Logger.info(f"FinancialTransaction FindByTransactionType {transaction_type}")
            return True, financial_transaction_list
        except Exception as e:
            Logger.error(f"FinancialTransaction FindByTransactionType Error: {e}")
            return False, e

    def find_by_customer_id(self, customer_id):
        try:
            financial_transaction_list = self.financial_transaction_service.find_by_customer_id(customer_id)
            Logger.info(f"FinancialTransaction FindByCustomerId {customer_id}")
            return True, financial_transaction_list
        except Exception as e:
            Logger.error(f"FinancialTransaction FindByCustomerId Error: {e}")
            return False, e

    def find_by_employee_id(self, employee_id):
        try:
            financial_transaction_list = self.financial_transaction_service.find_by_employee_id(employee_id)
            Logger.info(f"FinancialTransaction FindByEmployeeId {employee_id}")
            return True, financial_transaction_list
        except Exception as e:
            Logger.error(f"FinancialTransaction FindByEmployeeId Error: {e}")
            return False, e

    def find_by_payment_id(self, payment_id):
        try:
            financial_transaction_list = self.financial_transaction_service.find_by_payment_id(payment_id)
            Logger.info(f"FinancialTransaction FindByPaymentId {payment_id}")
            return True, financial_transaction_list
        except Exception as e:
            Logger.error(f"FinancialTransaction FindByPaymentId Error: {e}")
            return False, e

    def find_by_date_time_range(self, start_date_time, end_date_time):
        try:
            financial_transaction_list = self.financial_transaction_service.find_by_date_time_range(start_date_time, end_date_time)
            Logger.info(f"FinancialTransaction FindByDateTimeRange {start_date_time} to {end_date_time}")
            return True, financial_transaction_list
        except Exception as e:
            Logger.error(f"FinancialTransaction FindByDateTimeRange Error: {e}")
            return False, e

    def find_by_date_time_range_and_customer_id(self, start_date_time, end_date_time, customer_id):
        try:
            financial_transaction_list = self.financial_transaction_service.find_by_date_time_range_and_customer_id(start_date_time, end_date_time, customer_id)
            Logger.info(f"FinancialTransaction FindByDateTimeRangeAndCustomerId {start_date_time} to {end_date_time}, customer: {customer_id}")
            return True, financial_transaction_list
        except Exception as e:
            Logger.error(f"FinancialTransaction FindByDateTimeRangeAndCustomerId Error: {e}")
            return False, e
