class Warehouse:
    def __init__(self, id, product_id, quantity):
        self.id = id
        self.product_id = product_id
        self.quantity = quantity

    def __repr__(self):
        return f'{self.__dict__}'
