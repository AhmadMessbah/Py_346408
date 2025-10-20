from model.repository.order_item_repository  import OrderItemRepository


class OrderItemService:
    def __init__(self):
        self.repository = OrderItemRepository()

    def save(self, order_item):
        self.repository.save(order_item)

    def update(self, order_item):
        self.repository.update(order_item)

    def delete(self, id):
        self.repository.delete(id)

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, id):
        return self.repository.find_by_id(id)

    def find_by_order_id(self, order_id):
        return self.repository.find_by_order_id(order_id)