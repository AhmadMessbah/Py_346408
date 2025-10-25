import sqlite3
from model import FinancialTransaction

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
            [financial_transactions.id, financial_transactions.transaction_type, financial_transactions.customer_id,
            financial_transactions.employee_id, financial_transactions.amount, financial_transactions.date_time,
            financial_transactions.payment_id, financial_transactions.description])
        self.connection.commit()
        self.disconnect()

    def update(self, financial_transactions):
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
        financial_transaction_list =  [FinancialTransaction(*transaction) for transaction in self.cursor.fetchall()]
        self.disconnect()
        return financial_transaction_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from financial_transactions where id=?", [id])
        financial_transaction_list = [FinancialTransaction(*transaction) for transaction in self.cursor.fetchall()]
        self.disconnect()
        return financial_transaction_list

    def find_by_transaction_type(self, transaction_type):
        self.connect()
        self.cursor.execute("select * from financial_transactions where transaction_type=?", [transaction_type])
        financial_transaction_list = [FinancialTransaction(*transaction) for transaction in self.cursor.fetchall()]
        self.disconnect()
        return financial_transaction_list

    def find_by_customer_id(self, customer_id):
        self.connect()
        self.cursor.execute("select * from financial_transactions where customer_id=?", [customer_id])
        financial_transaction_list = [FinancialTransaction(*transaction) for transaction in self.cursor.fetchall()]
        self.disconnect()
        return financial_transaction_list

    def find_by_employee_id(self, employee_id):
        self.connect()
        self.cursor.execute("select * from financial_transactions where employee_id=?", [employee_id])
        financial_transaction_list = [FinancialTransaction(*transaction) for transaction in self.cursor.fetchall()]
        self.disconnect()
        return financial_transaction_list

    def find_by_payment_id(self, payment_id):
        self.connect()
        self.cursor.execute("select * from financial_transactions where payment_id=?", [payment_id])
        financial_transaction_list = [FinancialTransaction(*transaction) for transaction in self.cursor.fetchall()]
        self.disconnect()
        return financial_transaction_list



    def find_by_date_time_range(self, start_date_time, end_date_time):
        self.connect()
        self.cursor.execute("select * from financial_transactions where date_time between ? and ?", [start_date_time, end_date_time])
        financial_transaction_list = [FinancialTransaction(*transaction) for transaction in self.cursor.fetchall()]
        self.disconnect()
        return financial_transaction_list

    def find_by_date_time_range_and_customer_id(self, start_date_time, end_date_time, customer_id):
        self.connect()
        self.cursor.execute("select * from financial_transactions where date_time between ? and ? and customer_id = ?",
                            [start_date_time, end_date_time, customer_id])
        financial_transaction_list = [FinancialTransaction(*transaction) for transaction in self.cursor.fetchall()]
        self.disconnect()
        return financial_transaction_list