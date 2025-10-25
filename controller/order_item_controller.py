from model import OrderItem, OrderItemService


class OrderItemController:
    def save(self, order_id, product_id, quantity, price, discount, description):
        try:
            order_item = OrderItem(None, order_id, product_id, quantity, price, discount, description)
            order_item.validate()
            service = OrderItemService()
            service.save(order_item)
            return True, f"OrderItem Saved Successfully \n{order_item}"
        except Exception as e:
            return False, e

    def update(self, id, order_id, product_id, quantity, price, discount, description):
        try:
            order_item = OrderItem(id, order_id, product_id, quantity, price, discount, description)
            order_item.validate()
            service = OrderItemService()
            service.update(order_item)
            return True, f"OrderItem Updated Successfully \n{order_item}"
        except Exception as e:
            return False, e

    def delete(self, id):
        try:
            service = OrderItemService()
            service.delete(id)
            return True, f"OrderItem With Id {id} Deleted Successfully"
        except Exception as e:
            return False, e

    def find_all(self):
        try:
            service = OrderItemService()
            order_item_list = service.find_all()
            return True, order_item_list
        except Exception as e:
            return False, e

    def find_by_id(self, id):
        try:
            service = OrderItemService()
            order_item_list = service.find_by_id(id)
            return True, order_item_list
        except Exception as e:
            return False, e

    def find_by_order_id(self, order_id):
        try:
            service = OrderItemService()
            order_item_list = service.find_by_order_id(order_id)
            return True, order_item_list
        except Exception as e:
            return False, e

    def find_by_product_id(self, product_id):
        try:
            service = OrderItemService()
            order_item_list = service.find_by_product_id(product_id)
            return True, order_item_list
        except Exception as e:
            return False, e

    def find_by_quantity_less_than(self, quantity):
        try:
            service = OrderItemService()
            order_item_list = service.find_by_quantity_less_than(quantity)
            return True, order_item_list
        except Exception as e:
            return False, e
