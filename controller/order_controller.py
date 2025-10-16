from model.entity.order import Order
from model.service.order_service import OrderService


class OrderController:
    def save(self, order_type, customer_id, employee_id, date_time, payment_id,
             warehouse_transaction_id, tax=None, total_discount=None, total_amount=None):
        try:
            order = Order(None, order_type, customer_id, employee_id, date_time,
                 payment_id, warehouse_transaction_id, tax, total_discount, total_amount)
            service = OrderService()
            service.save(order)
            return True, f"order Saved Successfully \n{order}"
        except:
            return False, "Save Error"

    def update(self, id, order_type, customer_id, employee_id, date_time, payment_id,
               warehouse_transaction_id, tax=None, total_discount=None, total_amount=None):
        try:
            order = Order(id, order_type, customer_id,employee_id, date_time,
                 payment_id, warehouse_transaction_id, tax, total_discount, total_amount)
            service = OrderService()
            service.update(order)
            return True, f"order Updated Successfully \n{order}"
        except:
            return False, "Update Error"

    def delete(self, id):
        try:
            order = OrderService()
            order.delete(id)
            return True, f"order with Id {id} Deleted Successfully"
        except:
            return False, "Delete Error"

    def find_all(self):
        try:
            service = OrderService()
            order_list = service.find_all()
            return True, order_list
        except:
            return False, "Find All Error"

    def find_by_id(self, id):
        try:
            service = OrderService()
            order = service.find_by_id(id)
            return True, order
        except:
            return False, "Find By Id Error"