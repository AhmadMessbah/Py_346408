from model.entity.order_items import OrderItems
from model.service.order_items_service import OrderItemsService


class OrderItemsController:

    def save(self, product_id, quantity, price, discount, description):
        try:
            order_items = OrderItems(None, product_id, quantity, price, discount, description)
            print("Save requested, ok")
            service = OrderItemsService()
            service.save(order_items)
            return True, "Saved"
        except:
            return False, "Save Error"

    def update(self, order_items):
        pass

    def delete(self, id):
        pass

    def find_all(self):
        pass

    def find_by_id(self, id):
        pass