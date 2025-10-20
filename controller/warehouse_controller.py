from model.entity.warehouse import Warehouse
from model.service.warehouse_service import WarehouseService

class WarehouseController:
    def save(self, product_id, quantity):
        try:
            warehouse = Warehouse(None, product_id, quantity)
            service = WarehouseService()
            service.save(warehouse)
            return True, "Saved"
        except:
            return False, "Error"
        
    def update(self,id, product_id, quantity):
        try:
            warehouse = Warehouse(id,product_id,quantity)
            service = WarehouseService()
            service.update(warehouse)
            return True, "Updated"
        except:
            return False, "Error"
        
    def delete(self, id):
        try:
            service = WarehouseService()
            service.delete(id)
            return True, "Deleted"
        except:
            return False, "Error"
        
    def find_all(self):
        try:
            service = WarehouseService()
            return True, service.find_all()
        except:
            return False, "Error"

    def find_by_id(self, id):
        try:
            service = WarehouseService()
            return True, service.find_by_id(id)
        except:
            return False, "Error"