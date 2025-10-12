from model.repository.warehouse_transaction_repository import  WarehouseTransactionRepository


class WarehouseTransactionService:
    def __init__(self):
        self.repository = WarehouseTransactionRepository()

    def save(self, warehouse_transaction):
        self.repository.save(warehouse_transaction)

    def update(self, warehouse_transaction):
        self.repository.update(warehouse_transaction)

    def delete(self, id):
        self.repository.delete(id)

    def find_all(self):
        self.repository.find_all()

    def find_by_id(self, id):
        return self.repository.find_by_id(id)