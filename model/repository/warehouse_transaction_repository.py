import sqlite3
from model.entity.warehouse_transaction import WarehouseTransaction
from datetime import datetime

class WarehouseTransactionRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self,warehouse_transaction):
            self.connect()
            self.cursor.execute("""
                    insert into warehouse_transactions (product_id,quantity,transaction_type, transaction_datetime, customer_id, employee_id)
                     values (?,?,?,?,?,?)
            """, ([warehouse_transaction.product_id, warehouse_transaction.quantity, warehouse_transaction.transaction_type, warehouse_transaction.transaction_datetime,warehouse_transaction.customer_id, warehouse_transaction.employee_id]))
            self.connection.commit()
            self.disconnect()

    def update(self, warehouse_transaction):
            self.connect()
            self.cursor.execute("""update warehouse_transactions set product_id=?,quantity=?,transaction_type=?,transaction_datetime=?,customer_id=?,employee_id=? where id=?""", ([warehouse_transaction.product_id,warehouse_transaction.quantity,warehouse_transaction.transaction_type,warehouse_transaction.transaction_datetime,warehouse_transaction.customer_id,warehouse_transaction.employee_id, warehouse_transaction.id]))
            self.connection.commit()
            self.disconnect()

    def delete(self,id):
        self.connect()
        self.cursor.execute("delete from warehouse_transactions where id=?",
                            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from warehouse_transactions")
        warehouse_transaction_list = [WarehouseTransaction(*warehouse_transaction) for warehouse_transaction in self.cursor.fetchall()]
        self.disconnect()
        return warehouse_transaction_list


    def find_by_id(self,id):
        self.connect()
        self.cursor.execute("select * from warehouse_transactions where id=?", [id])
        warehouse_transaction_list = [WarehouseTransaction(*warehouse_transaction) for warehouse_transaction in
                                      self.cursor.fetchall()]
        self.disconnect()
        return warehouse_transaction_list
