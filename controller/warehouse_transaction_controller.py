from model.entity.warehouse_transaction import WarehouseTransaction
from model.service.warehouse_transaction_service import WarehouseTransactionService


class WarehouseController:
    def save(self, product_id, quantity, transaction_type, transaction_datetime, customer_id, employee_id):
        try:
            warehouse_transacton = WarehouseTransaction(None, product_id, quantity, transaction_type, transaction_datetime, customer_id, employee_id)
            print("WarehouseTransaction save request [OK]")
            service = WarehouseTransactionService()
            service.save(warehouse_transacton)
            return True, "Saved"
        except:
            return False, "Error"

    def update(self, product_id, quantity):
        try:
            warehouse = WarehouseTransaction(None, product_id, quantity)
            print("Warehouse update request [OK]")
            service = WarehouseTransactionService()
            service.update(warehouse)
            return True, "Updated"
        except:
            return False, "Error"

    def delete(self, id):
        try:
            service = WarehouseTransactionService()
            service.delete(id)
            print("Warehouse delete request [OK]")
            return True, "Deleted"
        except:
            return False, "Error"

    def find_all(self):
        try:
            service = WarehouseTransactionService()
            service.find_all()
            print("Warehouse find all request [OK]")
            return True, "Found"
        except:
            return False, "Error"

    def find_by_id(self, id):
        try:
            service = WarehouseTransactionService()
            service.find_by_id(id)
            print("Warehouse find by id request [OK]")
            return True, "Found"
        except:
            return False, "Error"