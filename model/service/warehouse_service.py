from model.repository.warehouse_repository import WarehouseRepository

class WarehouseService:
    def __init__(self):
        self.repository = WarehouseRepository()

    def save(self, warehouse):
        self.repository.save(warehouse)
        return print("save was succesfull")
    
    def update(self, warehouse):
        self.repository.update(warehouse)
    
    def delete(self, id):
        self.repository.delete(id)

    def find_all(self):
        self.repository.find_all()

    def find_by_id(self, id):
        return self.repository.find_by_id(id)