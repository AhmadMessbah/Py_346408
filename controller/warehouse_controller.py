from model import Warehouse, WarehouseService
from tools.logging import Logger


class WarehouseController:
    warehouse_service = WarehouseService()

    @classmethod
    def save(cls, product_id, quantity):
        try:
            warehouse = Warehouse(None, product_id, quantity)
            warehouse.validate()
            warehouse = cls.warehouse_service.save(warehouse)
            Logger.info(f"Warehouse {warehouse} saved")
            return True, f"Warehouse Saved Successfully"
        except Exception as e:
            Logger.error(f"Warehouse Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, warehouse_id, product_id, quantity):
        try:
            warehouse = Warehouse(warehouse_id, product_id, quantity)
            warehouse.validate()
            warehouse = cls.warehouse_service.update(warehouse)
            Logger.info(f"Warehouse {warehouse} updated")
            return True, "Warehouse Updated Successfully"
        except Exception as e:
            Logger.error(f"Warehouse Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, warehouse_id):
        try:
            warehouse = cls.warehouse_service.delete(warehouse_id)
            Logger.info(f"Warehouse {warehouse} deleted")
            return True, f"Warehouse Deleted Successfully"
        except Exception as e:
            Logger.error(f"Warehouse Delete Error: {e}")
            return False, e

    def find_all(self):
        try:
            warehouse_list = cls.warehouse_service.find_all()
            Logger.info("Warehouse FindAll")
            return True, warehouse_list
        except Exception as e:
            Logger.error(f"Warehouse FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, warehouse_id):
        try:
            warehouse = cls.warehouse_service.find_by_id(warehouse_id)
            Logger.info(f"Warehouse FindById {warehouse_id}")
            return True, warehouse
        except Exception as e:
            Logger.error(f"Warehouse FindById Error: {e}")
            return False, e

    @classmethod
    def find_by_product_id(cls, product_id):
        try:
            warehouse_list = cls.warehouse_service.find_by_product_id(product_id)
            Logger.info(f"Warehouse FindByProductId {product_id}")
            return True, warehouse_list
        except Exception as e:
            Logger.error(f"Warehouse FindByProductId Error: {e}")
            return False, e

    @classmethod
    def find_by_quantity_less_than(cls, quantity):
        try:
            warehouse_list = cls.warehouse_service.find_by_quantity_less_than(quantity)
            Logger.info(f"Warehouse FindByQuantityLessThan {quantity}")
            return True, warehouse_list
        except Exception as e:
            Logger.error(f"Warehouse FindByQuantityLessThan Error: {e}")
            return False, e

    @classmethod
    def find_by_quantity_more_than(cls, quantity):
        try:
            warehouse_list = cls.warehouse_service.find_by_quantity_more_than(quantity)
            Logger.info(f"Warehouse FindByQuantityMoreThan {quantity}")
            return True, warehouse_list
        except Exception as e:
            Logger.error(f"Warehouse FindByQuantityMoreThan Error: {e}")
            return False, e
