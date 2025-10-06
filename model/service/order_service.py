from model.repository.order_repository import OrderRepository


class OrderService:
    def __init__(self):
        self.repository = OrderRepository()

    def save(self, order):
        self.repository.save(order)

    def update(self, order):
        self.repository.update(order)

    def delete(self,id):
        self.repository.delete(id)

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, id):
        return self.repository.find_by_id(id)