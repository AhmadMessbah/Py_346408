import sqlite3
from model.entity.financial_transaction import FinancialTransaction

class FinancialTransactionRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, transaction: FinancialTransaction):
        self.connect()
        self.cursor.execute("""
            INSERT INTO financial_transactions
            (id, transaction_type, customer_id, employee_id, amount, date_time, payment_id, description)
            VALUES (?,?,?,?,?,?,?,?)
        """, [transaction.id, transaction.transaction_type, transaction.customer_id,
              transaction.employee_id, transaction.amount, transaction.date_time,
              transaction.payment_id, transaction.description])
        self.connection.commit()
        self.disconnect()

    def update(self, transaction: FinancialTransaction):
        self.connect()
        self.cursor.execute("""
            UPDATE financial_transactions
            SET transaction_type=?, customer_id=?, employee_id=?, amount=?, date_time=?, payment_id=?, description=?
            WHERE id=?
        """, [transaction.transaction_type, transaction.customer_id, transaction.employee_id,
              transaction.amount, transaction.date_time, transaction.payment_id,
              transaction.description, transaction.id])
        self.connection.commit()
        self.disconnect()

    def delete(self, transaction_id):
        self.connect()
        self.cursor.execute("DELETE FROM financial_transactions WHERE id=?", [transaction_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM financial_transactions")
        transactions = [FinancialTransaction(*row) for row in self.cursor.fetchall()]
        self.disconnect()
        return transactions

    def find_by_id(self, transaction_id):
        self.connect()
        self.cursor.execute("SELECT * FROM financial_transactions WHERE id=?", [transaction_id])
        transactions = [FinancialTransaction(*row) for row in self.cursor.fetchall()]
        self.disconnect()
        return transactions
