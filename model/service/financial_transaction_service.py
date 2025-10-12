from model.repository.financial_transaction_repository import FinancialTransactionRepository


class FinancialTransactionService:
    def __init__(self):
        self.repository = FinancialTransactionRepository()

    def save(self, financial_transaction):
        self.repository.save(financial_transaction)

    def update(self, financial_transaction):
        self.repository.update(financial_transaction)

    def delete(self, id):
        self.repository.delete(id)

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, id):
        return self.repository.find_by_id(id)