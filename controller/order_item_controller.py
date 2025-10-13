from model.entity.order_item import OrderItem
from model.service.order_item_service import OrderItemService

class OrderServiceController:
    def save(self, product_id, quantity, price, discount, description):
        try:
            order_item = OrderItem(None, product_id, quantity, price, discount, description)
            service = OrderItemService()
            service.save(order_item)
            return True, f"Customer Saved Successfully \n{order_item}"
        except:
            return False, "Save Error"

    def update(self, id, product_id, quantity, price, discount, description):
        try:
            order_item = OrderItem(id, product_id, quantity, price, discount, description)
            service = OrderItemService()
            service.update(order_item)
            return True, f"Customer Updated Successfully \n{order_item}"
        except:
            return False, "Update Error"

    def delete(self, id):
        try:
            service = OrderItemService()
            service.delete(id)
            return True, f"Customer With Id{id} Delete Successfully"
        except:
            return False, "Delete Error"

    def find_all(self):
        try:
            service = OrderItemService()
            order_list = service.find_all()
            return True, order_list
        except:
            return False, "Find All Error"

    def find_by_id(self, id):
        try:
            service = OrderItemService()
            order = service.find_by_id(id)
            return True, order
        except:
            return False, "Find By Id Error"