from model  import OrderItemRepository


class OrderItemService:
    def __init__(self):
        self.repository = OrderItemRepository()

    def save(self, order_item):
        return self.repository.save(order_item)

    def update(self, order_item):
        order_item_result = self.repository.find_by_id(order_item.id)
        if order_item_result:
            self.repository.update(order_item)
            return order_item
        else:
            raise Exception("Order Item Not Found !!!")

    def delete(self, order_item_id):
        order_item = self.repository.find_by_id(order_item_id)
        if order_item:
            self.repository.delete(order_item_id)
            return order_item
        else:
            raise Exception("Order Item Not Found !!!")

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, order_item_id):
        order_item = self.repository.find_by_id(order_item_id)
        if order_item:
            return order_item
        else:
            raise Exception("Order Item Not Found !!!")

    def find_by_order_id(self, order_id):
        return self.repository.find_by_order_id(order_id)

    def find_by_product_id(self, product_id):
        return self.repository.find_by_product_id(product_id)

    def find_by_quantity_less_than(self, quantity):
        return self.repository.find_by_quantity_less_than(quantity)