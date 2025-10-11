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
            (transaction_type,customer_id,employee_id,amount,date_time,payment_id,description) values (?,?,?,?,?,?,?)""",
            [financial_transactions.transaction_type, financial_transactions.customer_id,
            financial_transactions.employee_id, financial_transactions.amount, financial_transactions.date_time,
            financial_transactions.payment_id, financial_transactions.description])
        self.connection.commit()
        self.disconnect()

    def update(self,financial_transactions):
        self.connect()
        self.cursor.execute("""update financial_transactions
            set transaction_type=?,customer_id=?,employee_id=?,amount=?,date_time=?,payment_id=?,description=? where id=?""",
                            [financial_transactions.transaction_type, financial_transactions.customer_id,
                             financial_transactions.employee_id, financial_transactions.amount,
                             financial_transactions.date_time,
                             financial_transactions.payment_id, financial_transactions.description, financial_transactions.id])
        self.connection.commit()
        self.disconnect()

    def delete(self, id):
        self.connect()
        self.cursor.execute("delete from financial_transactions where id=?", [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from financial_transactions")
        transaction_list =  [FinancialTransaction(*financial_transactions) for financial_transactions in self.cursor.fetchall()]
        self.disconnect()
        return transaction_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from financial_transactions where id=?", [id])
        transaction_list = [FinancialTransaction(*transaction) for transaction in self.cursor.fetchall()]
        self.disconnect()
        return transaction_list
