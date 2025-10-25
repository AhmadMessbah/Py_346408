from model import OrderItem, OrderItemService
from tools.logging import Logger


class OrderItemController:
    def __init__(self):
        self.order_item_service = OrderItemService()

    def save(self, order_id, product_id, quantity, price, discount, description):
        try:
            order_item = OrderItem(None, order_id, product_id, quantity, price, discount, description)
            order_item.validate()
            order_item = self.order_item_service.save(order_item)
            Logger.info(f"OrderItem {order_item} saved")
            return True, f"OrderItem Saved Successfully"
        except Exception as e:
            Logger.error(f"OrderItem Save Error: {e}")
            return False, e

    def update(self, order_item_id, order_id, product_id, quantity, price, discount, description):
        try:
            order_item = OrderItem(order_item_id, order_id, product_id, quantity, price, discount, description)
            order_item.validate()
            order_item = self.order_item_service.update(order_item)
            Logger.info(f"OrderItem {order_item} updated")
            return True, "OrderItem Updated Successfully"
        except Exception as e:
            Logger.error(f"OrderItem Update Error: {e}")
            return False, e

    def delete(self, order_item_id):
        try:
            order_item = self.order_item_service.delete(order_item_id)
            Logger.info(f"OrderItem {order_item} deleted")
            return True, f"OrderItem Deleted Successfully"
        except Exception as e:
            Logger.error(f"OrderItem Delete Error: {e}")
            return False, e

    def find_all(self):
        try:
            order_item_list = self.order_item_service.find_all()
            Logger.info("OrderItem FindAll")
            return True, order_item_list
        except Exception as e:
            Logger.error(f"OrderItem FindAll Error: {e}")
            return False, e

    def find_by_id(self, order_item_id):
        try:
            order_item = self.order_item_service.find_by_id(order_item_id)
            Logger.info(f"OrderItem FindById {order_item_id}")
            return True, order_item
        except Exception as e:
            Logger.error(f"OrderItem FindById Error: {e}")
            return False, e

    def find_by_order_id(self, order_id):
        try:
            order_item_list = self.order_item_service.find_by_order_id(order_id)
            Logger.info(f"OrderItem FindByOrderId {order_id}")
            return True, order_item_list
        except Exception as e:
            Logger.error(f"OrderItem FindByOrderId Error: {e}")
            return False, e

    def find_by_product_id(self, product_id):
        try:
            order_item_list = self.order_item_service.find_by_product_id(product_id)
            Logger.info(f"OrderItem FindByProductId {product_id}")
            return True, order_item_list
        except Exception as e:
            Logger.error(f"OrderItem FindByProductId Error: {e}")
            return False, e

    def find_by_quantity_less_than(self, quantity):
        try:
            order_item_list = self.order_item_service.find_by_quantity_less_than(quantity)
            Logger.info(f"OrderItem FindByQuantityLessThan {quantity}")
            return True, order_item_list
        except Exception as e:
            Logger.error(f"OrderItem FindByQuantityLessThan Error: {e}")
            return False, e
