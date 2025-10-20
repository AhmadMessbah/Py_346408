from model import WarehouseRepository

class WarehouseService:
    def __init__(self):
        self.repository = WarehouseRepository()

    def save(self, warehouse):
        self.repository.save(warehouse)
    
    def update(self, warehouse):
        self.repository.update(warehouse)
    
    def delete(self, id):
        self.repository.delete(id)

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, id):
        return self.repository.find_by_id(id)

    def find_by_product_id(self, product_id):
        pass

    def find_by_quantity_less_than(self, quantity):
        pass

    def find_by_quantity_more_than(self, quantity):
        pass