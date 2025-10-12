from model.entity.order_item import OrderItems
from model.service.order_item_service import OrderItemsService


class OrderItemController:

    def save(self, product_id, quantity, price, discount, description):
        try:
            order_item = OrderItem(None, product_id, quantity, price, discount, description)
            print("Save requested, ok")
            service = OrderItemService()
            service.save(order_item)
            return True, "Saved"
        except:
            return False, "Save Error"

    def update(self, order_item):
        pass

    def delete(self, id):
        pass

    def find_all(self):
        pass

    def find_by_id(self, id):
        pass