from model import Warehouse, WarehouseService


class WarehouseController:
    def save(self, product_id, quantity):
        try:
            warehouse = Warehouse(None, product_id, quantity)
            service = WarehouseService()
            service.save(warehouse)
            return True, f"Warehouse Saved {warehouse}"
        except Exception as e:
            return False, e

    def update(self, id, product_id, quantity):
        try:
            warehouse = Warehouse(id, product_id, quantity)
            service = WarehouseService()
            service.update(warehouse)
            return True, f" Warehouse Updated {warehouse}"
        except Exception as e:
            return False, e

    def delete(self, id):
        try:
            service = WarehouseService()
            service.delete(id)
            return True, f"Warehouse Deleted {id}"
        except Exception as e:
            return False, e

    def find_all(self):
        try:
            service = WarehouseService()
            return True, service.find_all()
        except Exception as e:
            return False, e

    def find_by_id(self, id):
        try:
            service = WarehouseService()
            return True, service.find_by_id(id)
        except Exception as e:
            return False, e