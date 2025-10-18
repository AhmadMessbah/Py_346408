from model.entity.warehouse_transaction import WarehouseTransaction
from model.service.warehouse_transaction_service import WarehouseTransactionService


class WarehouseTransactionController:
    def save(self, product_id, quantity, transaction_type, transaction_datetime, customer_id, employee_id):
        try:
            warehouse_transaction = WarehouseTransaction(None, product_id, quantity, transaction_type, transaction_datetime, customer_id, employee_id)
            service = WarehouseTransactionService()
            service.save(warehouse_transaction)
            return True, "WarehouseTransaction save request [OK]"
        except:
            return False, "Save Error"

    def update(self, id, product_id, quantity, transaction_type, transaction_datetime, customer_id, employee_id):
        try:
            warehouse = WarehouseTransaction(id, product_id, quantity, transaction_type, transaction_datetime, customer_id, employee_id)
            service = WarehouseTransactionService()
            service.update(warehouse)
            return True, "Warehouse update request [OK]"
        except:
            return False, "Update Error"

    def delete(self, id):
        try:
            service = WarehouseTransactionService()
            service.delete(id)
            return True, "Deleted"
        except:
            return False, f"product with Id {id} was deleted successfully"

    def find_all(self):
        try:
            service = WarehouseTransactionService()
            product_list = service.find_all()
            return True, product_list
        except:
            return False, "Find Al Error"

    def find_by_id(self, id):
        try:
            service = WarehouseTransactionService()
            product = service.find_by_id(id)
            return True, product
        except:
            return False, "Find by id Error!"