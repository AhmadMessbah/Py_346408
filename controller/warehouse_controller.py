from model.entity.warehouse import Warehouse
from model.service.warehouse_service import WarehouseService

class WarehouseController:
    def save(self, product_id, quantity):
        try:
            warehouse = Warehouse(None, product_id, quantity)
            print("Warehouse save request [OK]")
            service = WarehouseService()
            service.save(warehouse)
            return True, "Saved"
        except:
            return False, "Error"
        
    def update(self, product_id, quantity):
        try:
            warehouse = Warehouse(None, product_id, quantity)
            print("Warehouse update request [OK]")
            service = WarehouseService()
            service.update(warehouse)
            return True, "Updated"
        except:
            return False, "Error"
        
    def delete(self, id):
        try:
            service = WarehouseService()
            service.delete(id)
            print("Warehouse delete request [OK]")
            return True, "Deleted"
        except:
            return False, "Error"
        
    def find_all(self):
        try:
            service = WarehouseService()
            service.find_all()
            print("Warehouse find all request [OK]")
            return True, "Found"
        except:
            return False, "Error"

    def find_by_id(self, id):
        try:
            service = WarehouseService()
            service.find_by_id(id)
            print("Warehouse find by id request [OK]")
            return True, "Found"
        except:
            return False, "Error"