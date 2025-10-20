from model import WarehouseTransaction, WarehouseTransactionService


class WarehouseTransactionController:
    def save(self, product_id, quantity, transaction_type, transaction_datetime, customer_id, employee_id):
        try:
            warehouse_transaction = WarehouseTransaction(None, product_id, quantity, transaction_type,
                                                         transaction_datetime, customer_id, employee_id)
            service = WarehouseTransactionService()
            service.save(warehouse_transaction)
            return True, f"WarehouseTransaction saved {warehouse_transaction}"
        except Exception as e:
            return False, f"Save Error{e}"

    def update(self, id, product_id, quantity, transaction_type, transaction_datetime, customer_id, employee_id):
        try:
            warehouse_transaction = WarehouseTransaction(id, product_id, quantity, transaction_type,
                                                         transaction_datetime, customer_id, employee_id)
            service = WarehouseTransactionService()
            service.update(warehouse_transaction)
            return True, f"Warehouse_transaction updated {warehouse_transaction}"
        except Exception as e:
            return False, e

    def delete(self, id):
        try:
            service = WarehouseTransactionService()
            service.delete(id)
            return True, "Deleted"
        except Exception as e:
            return False, e

    def find_all(self):
        try:
            service = WarehouseTransactionService()

            return True, service.find_all()
        except Exception as e:
            return False, e

    def find_by_id(self, id):
        try:
            service = WarehouseTransactionService()
            return True, service.find_by_id(id)
        except Exception as e:
            return False, f"Find by id Error{e}!"
