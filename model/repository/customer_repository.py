import sqlite3

from model.entity.customer import Customer


class CustomerRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, customer):
        self.connect()
        self.cursor.execute(
            "insert into customers (id, first_name, last_name, phone_number, address) values (?,?,?,?,?)",
            [customer.first_name, customer.last_name, customer.phone_number, customer.address, customer.id])
        self.connection.commit()
        self.disconnect()

    def update(self, customer):
        self.connect()
        self.cursor.execute(
            "update customers set id=?, first_name=?, last_name=?, phone_number=?, address=? where id=?",
            [customer.first_name, customer.last_name, customer.phone_number, customer.address, customer.id])
        self.connection.commit()
        self.disconnect()

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

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from customers where id=?", [id])
        customer_list = [Customer(*customer) for customer in self.cursor.fetchall()]
        self.disconnect()
        return customer_list
