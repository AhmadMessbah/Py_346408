import sqlite3

from model import Product


class ProductRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, product):
        self.connect()
        self.cursor.execute(
            "insert into products (name, brand, model, serial, category, unit, expiration_date) values (?,?,?,?,?,?,?)",
            [product.name, product.brand, product.model, product.serial, product.category, product.unit,
             product.expiration_date])
        self.connection.commit()
        self.disconnect()

    def update(self, product):
        self.connect()
        self.cursor.execute(
            "update products set name=?, brand=?, model=?, serial=?, category=?, unit=?, expiration_date=? where id=?",
            [product.name, product.brand, product.model, product.serial, product.category, product.unit,
             product.expiration_date, product.id])
        self.connection.commit()
        self.disconnect()

    def delete(self, id):
        self.connect()
        self.cursor.execute("delete from products where id=?",
                            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from products")
        product_list = [Product(*product) for product in self.cursor.fetchall()]
        self.disconnect()
        return product_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from products where id=?", [id])
        product_list = [Product(*product) for product in self.cursor.fetchall()]
        self.disconnect()
        return product_list
