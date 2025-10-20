from model.entity.warehouse_transaction import WarehouseTransaction
from model.service.warehouse_transaction_service import WarehouseTransactionService


class WarehouseTransactionController:
    def save(self, product_id, quantity, transaction_type, transaction_datetime, customer_id, employee_id):
        try:
            warehouse_transaction = WarehouseTransaction(None, product_id, quantity, transaction_type, transaction_datetime, customer_id, employee_id)
            service = WarehouseTransactionService()
            service.save(warehouse_transaction)
            return True, f"WarehouseTransaction saved {warehouse_transaction}"
        except Exception as e:
            return False, f"Save Error{e}"

    def update(self, id, product_id, quantity, transaction_type, transaction_datetime, customer_id, employee_id):
        try:
            warehouse_transaction = WarehouseTransaction(id, product_id, quantity, transaction_type, transaction_datetime, customer_id, employee_id)
            service = WarehouseTransactionService()
            service.update(warehouse_transaction)
            return True, f"Warehouse_transaction updated {warehouse_transaction}"
        except Exception as e:
            return False,f"Update Error{e}"

    def delete(self, id):
        try:
            service = WarehouseTransactionService()
            service.delete(id)
            return True, "Deleted"
        except Exception as e:
            return False, f"Delete Error {e}"

    def find_all(self):
        try:
            service = WarehouseTransactionService()

            return True,service.find_all()
        except:
            return False, "Find Al Error"

    def find_by_id(self, id):
        try:
            service = WarehouseTransactionService()

            return True,  service.find_by_id(id)
        except Exception as e:
            return False, f"Find by id Error{e}!"