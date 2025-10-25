from model import Payment, PaymentService
from tools.logging import Logger


class PaymentController:
    def __init__(self):
        self.payment_service = PaymentService()

    def save(self, transaction_type, payment_type, date_time, customer_id, total_amount, employee_id, description):
        try:
            payment = Payment(None, transaction_type, payment_type, date_time, customer_id, total_amount, employee_id,
                              description)
            payment.validate()
            payment = self.payment_service.save(payment)
            Logger.info(f"Payment {payment} saved")
            return True, f"Payment Saved Successfully"
        except Exception as e:
            Logger.error(f"Payment Save Error: {e}")
            return False, e

    def update(self, payment_id, transaction_type, payment_type, date_time, customer_id, total_amount, employee_id,
               description):
        try:
            payment = Payment(payment_id, transaction_type, payment_type, date_time, customer_id, total_amount, employee_id,
                              description)
            payment.validate()
            payment = self.payment_service.update(payment)
            Logger.info(f"Payment {payment} updated")
            return True, "Payment Updated Successfully"
        except Exception as e:
            Logger.error(f"Payment Update Error: {e}")
            return False, e

    def delete(self, payment_id):
        try:
            payment = self.payment_service.delete(payment_id)
            Logger.info(f"Payment {payment} deleted")
            return True, f"Payment Deleted Successfully"
        except Exception as e:
            Logger.error(f"Payment Delete Error: {e}")
            return False, e

    def find_all(self):
        try:
            payment_list = self.payment_service.find_all()
            Logger.info("Payment FindAll")
            return True, payment_list
        except Exception as e:
            Logger.error(f"Payment FindAll Error: {e}")
            return False, e

    def find_by_id(self, payment_id):
        try:
            payment = self.payment_service.find_by_id(payment_id)
            Logger.info(f"Payment FindById {payment_id}")
            return True, payment
        except Exception as e:
            Logger.error(f"Payment FindById Error: {e}")
            return False, e

    def find_by_transaction_type(self, transaction_type):
        try:
            payment_list = self.payment_service.find_by_transaction_type(transaction_type)
            Logger.info(f"Payment FindByTransactionType {transaction_type}")
            return True, payment_list
        except Exception as e:
            Logger.error(f"Payment FindByTransactionType Error: {e}")
            return False, e

    def find_by_payment_type(self, payment_type):
        try:
            payment_list = self.payment_service.find_by_payment_type(payment_type)
            Logger.info(f"Payment FindByPaymentType {payment_type}")
            return True, payment_list
        except Exception as e:
            Logger.error(f"Payment FindByPaymentType Error: {e}")
            return False, e

    def find_by_date_time_range(self, start_date_time, end_date_time):
        try:
            payment_list = self.payment_service.find_by_date_time_range(start_date_time, end_date_time)
            Logger.info(f"Payment FindByDateTimeRange {start_date_time} to {end_date_time}")
            return True, payment_list
        except Exception as e:
            Logger.error(f"Payment FindByDateTimeRange Error: {e}")
            return False, e

    def find_by_date_time_range_and_customer_id(self, start_date_time, end_date_time, customer_id):
        try:
            payment_list = self.payment_service.find_by_date_time_range_and_customer_id(start_date_time, end_date_time, customer_id)
            Logger.info(f"Payment FindByDateTimeRangeAndCustomerId {start_date_time} to {end_date_time}, customer: {customer_id}")
            return True, payment_list
        except Exception as e:
            Logger.error(f"Payment FindByDateTimeRangeAndCustomerId Error: {e}")
            return False, e

    def find_by_date_time_range_and_employee_id(self, start_date_time, end_date_time, employee_id):
        try:
            payment_list = self.payment_service.find_by_date_time_range_and_employee_id(start_date_time, end_date_time, employee_id)
            Logger.info(f"Payment FindByDateTimeRangeAndEmployeeId {start_date_time} to {end_date_time}, employee: {employee_id}")
            return True, payment_list
        except Exception as e:
            Logger.error(f"Payment FindByDateTimeRangeAndEmployeeId Error: {e}")
            return False, e
