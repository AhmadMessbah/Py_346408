import sqlite3

from model import Customer


"""class CustomerRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/books_db.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, customer):
        self.connect()
        self.cursor.execute(
            "insert into customers (first_name, last_name, phone_number, address) values (?,?,?,?)",
            [customer.first_name, customer.last_name, customer.phone_number, customer.address])
        customer.customer_id = self.cursor.lastrowid
        self.connection.commit()
        return customer

    def update(self, customer):
        self.connect()
        self.cursor.execute(
            "update customers set first_name=?, last_name=?, phone_number=?, address=? where id=?",
            [customer.first_name, customer.last_name, customer.phone_number, customer.address, customer.id])
        self.connection.commit()
        self.disconnect()
        return customer

    def delete(self, id):
        self.connect()
        self.cursor.execute("delete from customers where id=?",
                            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from customers")
        customer_list = [Customer(*customer) for customer in self.cursor.fetchall()]
        self.disconnect()
        return customer_list

    def find_by_id(self, customer_id):
        self.connect()
        self.cursor.execute("select * from customers where id=?", [customer_id])
        customer = self.cursor.fetchone()
        self.disconnect()
        if customer:
            return Customer(*customer)
        return None

    def find_by_firstname_and_lastname(self,firstname, lastname):
        self.connect()
        self.cursor.execute("select * from customers where first_name=? and last_name=?", [firstname, lastname])
        customer_list = [Customer(*customer) for customer in self.cursor.fetchall()]
        self.disconnect()
        return customer_list

    def find_by_phone_number(self, phone_number):
        self.connect()
        self.cursor.execute("select * from customers where phone_number=? ", [phone_number])
        customer_list = [Customer(*customer) for customer in self.cursor.fetchall()]
        self.disconnect()
        return customer_list"""
import sqlite3
import os
from model import Customer

class CustomerRepository:
    def connect(self):
        # ایجاد پوشه db اگر وجود ندارد
        os.makedirs("./db", exist_ok=True)
        self.connection = sqlite3.connect("./db/books_db.db")
        self.cursor = self.connection.cursor()

        # ایجاد جدول اگر وجود ندارد
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                phone_number TEXT,
                address TEXT
            )
        ''')
        self.connection.commit()

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def save(self, customer):
        self.connect()
        self.cursor.execute(
            "INSERT INTO customers (first_name, last_name, phone_number, address) VALUES (?,?,?,?)",
            [customer.first_name, customer.last_name, customer.phone_number, customer.address])
        customer.customer_id = self.cursor.lastrowid
        self.connection.commit()
        self.disconnect()
        return customer

    def update(self, customer):
        self.connect()
        self.cursor.execute(
            "UPDATE customers SET first_name=?, last_name=?, phone_number=?, address=? WHERE customer_id=?",
            [customer.first_name, customer.last_name, customer.phone_number, customer.address, customer.customer_id])
        self.connection.commit()
        self.disconnect()
        return customer

    def delete(self, customer_id):
        self.connect()
        self.cursor.execute("DELETE FROM customers WHERE customer_id=?", [customer_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM customers")
        customer_list = [Customer(*customer) for customer in self.cursor.fetchall()]
        self.disconnect()
        return customer_list

    def find_by_id(self, customer_id):
        self.connect()
        self.cursor.execute("SELECT * FROM customers WHERE customer_id=?", [customer_id])
        customer = self.cursor.fetchone()
        self.disconnect()
        if customer:
            return Customer(*customer)
        return None

    def find_by_firstname_and_lastname(self, firstname, lastname):
        self.connect()
        self.cursor.execute("SELECT * FROM customers WHERE first_name=? AND last_name=?", [firstname, lastname])
        customer_list = [Customer(*customer) for customer in self.cursor.fetchall()]
        self.disconnect()
        return customer_list

    def find_by_phone_number(self, phone_number):
        self.connect()
        self.cursor.execute("SELECT * FROM customers WHERE phone_number=?", [phone_number])
        customer_list = [Customer(*customer) for customer in self.cursor.fetchall()]
        self.disconnect()
        return customer_list