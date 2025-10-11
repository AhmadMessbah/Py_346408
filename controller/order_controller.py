from model.entity.order import Order
from model.service.order_service import OrderService


class OrderController:

    def save(self, order_type, customer_id, employee_id, order_item_list, date_time,
                 payment_id, warehouse_transaction_id, tax=None, total_discount=None,
                 total_amount=None):
        try:
            order = Order(None, order_type, customer_id, employee_id, order_item_list, date_time,
                 payment_id, warehouse_transaction_id, tax=None, total_discount=None,
                 total_amount=None)
            print("Save Requested, ok")
            service = OrderService()
            service.save(order)
            return True, "Saved"
        except:
            return False, "Save Error"

    def update(self, order):
        pass

    def delete(self, id):
        pass

    def find_all(self):
        pass

    def find_by_id(self, id):
        pass