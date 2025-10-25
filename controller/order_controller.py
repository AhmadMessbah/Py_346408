from model import Order, OrderService
from tools.logging import Logger


class OrderController:
    def __init__(self):
        self.order_service = OrderService()

    def save(self, order_type, customer_id, employee_id, date_time,
             payment_id, warehouse_transaction_id, tax, total_discount,
             total_amount):
        try:
            order = Order(None, order_type, customer_id, employee_id, date_time,
                          payment_id, warehouse_transaction_id, tax, total_discount,
                          total_amount)
            order.validate()
            order = self.order_service.save(order)
            Logger.info(f"Order {order} saved")
            return True, f"Order Saved Successfully"
        except Exception as e:
            Logger.error(f"Order Save Error: {e}")
            return False, e

    def update(self, order_id, order_type, customer_id, employee_id, date_time,
               payment_id, warehouse_transaction_id, tax, total_discount,
               total_amount):
        try:
            order = Order(order_id, order_type, customer_id, employee_id, date_time,
                         payment_id, warehouse_transaction_id, tax, total_discount,
                         total_amount)
            order.validate()
            order = self.order_service.update(order)
            Logger.info(f"Order {order} updated")
            return True, "Order Updated Successfully"
        except Exception as e:
            Logger.error(f"Order Update Error: {e}")
            return False, e

    def delete(self, order_id):
        try:
            order = self.order_service.delete(order_id)
            Logger.info(f"Order {order} deleted")
            return True, f"Order Deleted Successfully"
        except Exception as e:
            Logger.error(f"Order Delete Error: {e}")
            return False, e

    def find_all(self):
        try:
            order_list = self.order_service.find_all()
            Logger.info("Order FindAll")
            return True, order_list
        except Exception as e:
            Logger.error(f"Order FindAll Error: {e}")
            return False, e

    def find_by_id(self, order_id):
        try:
            order = self.order_service.find_by_id(order_id)
            Logger.info(f"Order FindById {order_id}")
            return True, order
        except Exception as e:
            Logger.error(f"Order FindById Error: {e}")
            return False, e

    def find_by_order_type(self, order_type):
        try:
            order_list = self.order_service.find_by_order_type(order_type)
            Logger.info(f"Order FindByOrderType {order_type}")
            return True, order_list
        except Exception as e:
            Logger.error(f"Order FindByOrderType Error: {e}")
            return False, e

    def find_by_customer_id(self, customer_id):
        try:
            order_list = self.order_service.find_by_customer_id(customer_id)
            Logger.info(f"Order FindByCustomerId {customer_id}")
            return True, order_list
        except Exception as e:
            Logger.error(f"Order FindByCustomerId Error: {e}")
            return False, e

    def find_by_employee_id(self, employee_id):
        try:
            order_list = self.order_service.find_by_employee_id(employee_id)
            Logger.info(f"Order FindByEmployeeId {employee_id}")
            return True, order_list
        except Exception as e:
            Logger.error(f"Order FindByEmployeeId Error: {e}")
            return False, e

    def find_by_date_time_range(self, start_date_time, end_date_time):
        try:
            order_list = self.order_service.find_by_date_time_range(start_date_time, end_date_time)
            Logger.info(f"Order FindByDateTimeRange {start_date_time} to {end_date_time}")
            return True, order_list
        except Exception as e:
            Logger.error(f"Order FindByDateTimeRange Error: {e}")
            return False, e

    def find_by_date_time_range_and_customer_id(self, start_date_time, end_date_time, customer_id):
        try:
            order_list = self.order_service.find_by_date_time_range_and_customer_id(start_date_time, end_date_time, customer_id)
            Logger.info(f"Order FindByDateTimeRangeAndCustomerId {start_date_time} to {end_date_time}, customer: {customer_id}")
            return True, order_list
        except Exception as e:
            Logger.error(f"Order FindByDateTimeRangeAndCustomerId Error: {e}")
            return False, e
