from model import WarehouseRepository

class WarehouseService:
    def __init__(self):
        self.repository = WarehouseRepository()

    def save(self, warehouse):
        return self.repository.save(warehouse)
    
    def update(self, warehouse):
        warehouse_result = self.repository.find_by_id(warehouse.id)
        if warehouse_result:
            self.repository.update(warehouse)
            return warehouse
        else:
            raise Exception("Warehouse Not Found !!!")
    
    def delete(self, warehouse_id):
        warehouse = self.repository.find_by_id(warehouse_id)
        if warehouse:
            self.repository.delete(warehouse_id)
            return warehouse
        else:
            raise Exception("Warehouse Not Found !!!")

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, warehouse_id):
        warehouse = self.repository.find_by_id(warehouse_id)
        if warehouse:
            return warehouse
        else:
            raise Exception("Warehouse Not Found !!!")

    def find_by_product_id(self, product_id):
        return self.repository.find_by_product_id(product_id)

    def find_by_quantity_less_than(self, quantity):
        return self.repository.find_by_quantity_less_than(quantity)

    def find_by_quantity_more_than(self, quantity):
        return self.repository.find_by_quantity_more_than(quantity)