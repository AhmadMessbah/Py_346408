import sqlite3
from model.entity.financial_transaction import FinancialTransaction

class FinancialTransactionRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, financial_transactions):
        self.connect()
        self.cursor.execute("""insert into financial_transactions 
            (id,transaction_type,customer_id,employee_id,amount,date_time,payment_id,description) values (?,?,?,?,?,?,?,?)""",
            [transaction.id, transaction.transaction_type, transaction.customer_id,
            transaction.employee_id, transaction.amount, transaction.date_time,
            transaction.payment_id, transaction.description])
        self.connection.commit()
        self.disconnect()

    def update(self, transaction: FinancialTransaction):
        self.connect()
        self.cursor.execute("""update selling
            set transaction_type=?,customer_id=?,employee_id=?,amount=?,date_time=?,payment_id=?,description=? where id=?""",
                            [financial_transactions.transaction_type, financial_transactions.customer_id,
                             financial_transactions.employee_id, financial_transactions.amount,
                             financial_transactions.date_time,
                             financial_transactions.payment_id, financial_transactions.description, financial_transactions.id])
        self.connection.commit()
        self.disconnect()

    def delete(self, id):
        self.connect()
        self.cursor.execute("delete from transactions where id=?", [transaction_id])
        self.connection.commit()
        self.disconnect()

    # def find_all(self):
    #     self.connect()
    #     self.cursor.execute("select * from financial_transactions")
    #     transactions = [FinancialTransaction(*row) for row in self.cursor.fetchall()]
    #     self.disconnect()
    #     return transactions
    def find_all(self):
        self.connect()
        self.cursor.execute("select * from financial_transactions")
        transaction_list =  [FinancialTransaction(*transaction) for transaction in self.cursor.fetchall()]
        self.disconnect()
        return transaction_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from selling where id=?", [id])
        transaction_list = [FinancialTransaction(*transaction) for transaction in self.cursor.fetchall()]
        self.disconnect()
        return transaction_list
