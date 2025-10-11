import sqlite3
from model.entity.financial_transaction import FinancialTransaction

class FinancialTransactionRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, selling):
        self.connect()
        self.cursor.execute("""insert into selling
            (id,transaction_type,customer_id,employee_id,amount,date_time,payment_id,description) values (?,?,?,?,?,?,?,?)""",
            [selling.id, selling.transaction_type, selling.customer_id,
            selling.employee_id, selling.amount, selling.date_time,
            selling.payment_id, selling.description])
        self.connection.commit()
        self.disconnect()

    def update(self, selling):
        self.connect()
        self.cursor.execute("""update selling
            set transaction_type=?,customer_id=?,employee_id=?,amount=?,date_time=?,payment_id=?,description=? where id=?""",
            [selling.transaction_type, selling.customer_id, selling.employee_id,
            selling.amount,selling.date_time, selling.payment_id,
            selling.description, selling.id])
        self.connection.commit()
        self.disconnect()

    def delete(self, transaction_id):
        self.connect()
        self.cursor.execute("delete from selling where id=?", [transaction_id])
        self.connection.commit()
        self.disconnect()

    # def find_all(self):
    #     self.connect()
    #     self.cursor.execute("select * from financial_transactions")
    #     transactions = [FinancialTransaction(*row) for row in self.cursor.fetchall()]
    #     self.disconnect()
    #     return transactions
    def find_all(self, selling):
        self.connect()
        self.cursor.execute("select * from selling")
        transaction_list =  [FinancialTransaction(*transaction) for transaction in self.cursor.fetchall()]
        self.disconnect()
        return transaction_list

    # def find_by_id(self, transaction_id):
    #     self.connect()
    #     self.cursor.execute("SELECT * FROM financial_transactions WHERE id=?", [transaction_id])
    #     transactions = [FinancialTransaction(*row) for row in self.cursor.fetchall()]
    #     self.disconnect()
    #     return transactions
    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from selling where id=?", [id])
        transaction_list = [FinancialTransaction(*transaction) for transaction in self.cursor.fetchall()]
        self.disconnect()
        return transaction_list
