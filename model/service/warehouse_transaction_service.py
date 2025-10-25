from model import WarehouseTransactionRepository


class WarehouseTransactionService:
    def __init__(self):
        self.repository = WarehouseTransactionRepository()

    def save(self, warehouse_transaction):
        return self.repository.save(warehouse_transaction)

    def update(self, warehouse_transaction):
        warehouse_transaction_result = self.repository.find_by_id(warehouse_transaction.id)
        if warehouse_transaction_result:
            self.repository.update(warehouse_transaction)
            return warehouse_transaction
        else:
            raise Exception("Warehouse Transaction Not Found !!!")

    def delete(self, warehouse_transaction_id):
        warehouse_transaction = self.repository.find_by_id(warehouse_transaction_id)
        if warehouse_transaction:
            self.repository.delete(warehouse_transaction_id)
            return warehouse_transaction
        else:
            raise Exception("Warehouse Transaction Not Found !!!")

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, warehouse_transaction_id):
        warehouse_transaction = self.repository.find_by_id(warehouse_transaction_id)
        if warehouse_transaction:
            return warehouse_transaction
        else:
            raise Exception("Warehouse Transaction Not Found !!!")

    def find_by_product_id(self, product_id):
        return self.repository.find_bye_product_id

    def find_by_transaction_type(self, transaction_type):
        return self.repository.find_by_transaction_type

    def find_by_customer_id(self, customer_id):
        return self.repository.find_by_customer_id(customer_id)

    def find_by_employee_id(self, employee_id):
        return self.repository.find_by_employee_id(employee_id)

    def find_by_date_time_range(self, start_date_time, end_date_time):
        pass

    def find_by_date_time_range_and_customer_id(self, start_date_time, end_date_time, customer_id):
        pass

    def find_by_date_time_range_and_employee_id(self, start_date_time, end_date_time, employee_id):
        pass
