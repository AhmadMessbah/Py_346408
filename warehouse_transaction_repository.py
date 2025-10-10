import sqlite3
from model.entity.warehouse_transaction import WarehouseTransaction
from datetime import datetime

class WarehouseTransactionRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self,product_name,warehouse_id,quantity,transaction_type,sender,receiver):
            self.connect()
            self.cursor.execute("""
                    insert into warehouse_transactions (product_name,warehouse_id,quantity,transaction_type,sender,receiver)
                     values (?,?,?,?,?,?,?)
            """, ([product_name,warehouse_id,quantity,datetime.now(),transaction_type,sender,receiver]))
            self.connection.commit()
            self.disconnect()

    def update(self,quantity,transaction_type):
            self.connect()
            self.cursor.execute("""
                    insert into warehouse_transactions (quantity,transaction_type)
                    values (?,?)
            """,[(quantity,transaction_type)])
            self.connection.commit()
            self.disconnect()

    def delete(self,transaction_id):
        self.connect()
        self.cursor.execute("delete from warehouse_transactions where id=?",
                            (transaction_id,))
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from warehouse_transactions")


    def find_by_id(self,transaction_id):
        self.connect()
