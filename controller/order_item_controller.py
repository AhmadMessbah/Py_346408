from model.entity.order_item import OrderItem
from model.service.order_item_service import OrderItemService


class OrderItemController:
    def save(self, order_id, product_id, quantity, price, discount, description):
        try:
            order_item = OrderItem(None, order_id, product_id, quantity, price, discount, description)
            service = OrderItemService()
            service.save(order_item)
            return True, f"Order Item Saved Successfully \n{order_item}"
        except:
            return False, "Save Error"

    def update(self, id, order_id, product_id, quantity, price, discount, description):
        try:
            order_item = OrderItem(id, order_id, product_id, quantity, price, discount, description)
            service = OrderItemService()
            service.update(order_item)
            return True, f"Order Item Updated Successfully \n{order_item}"
        except:
            return False, "Update Error"

    def delete(self, id):
        try:
            service = OrderItemService()
            service.delete(id)
            return True, f"Order Item with Id{id} Deleted Successfully"
        except:
            return False, "Delete Error"

    def find_all(self):
        try:
            service = OrderItemService()
            order_item_list = service.find_all()
            return True, order_item_list
        except:
            return False, "Find All Error"

    def find_by_id(self, id):
        try:
            service = OrderItemService()
            order_item = service.find_by_id(id)
            return True, order_item
        except:
            return False, "Find By Id Error"

    def find_by_order_id(self, order_id):
        try:
            service = OrderItemService()
            order_item = service.find_by_order_id(order_id)
            return True, order_item
        except:
            return False, "Find By Order Id Error"