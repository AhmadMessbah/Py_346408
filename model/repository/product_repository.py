import sqlite3

class ProductRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, product):
        self.connect()
        self.cursor.execute("INSERT INTO products (product_id,product_name,product_type,expiration_date,warehouse_code,unit_price,stock_quantity) VALUES(?,?)",
                           [ product.product_id, product.product_name, product.product_type,product.expiration_date, product.warehouse_code, product.unit_price, product.stock_quantity ])
        self.connection.commit()
        self.disconnect()


    def update(self, product):
        self.connect()
        self.cursor.execute("update products set product_id=?,product_name=?,product_type=?,expiration_date=?,warehouse_code=?,unit_price=?,stock_quantity=? where id=?",
                            [product.product_id, product.product_name, product.type, product.expiration_date, product.warehouse_code, product.unit_price, product.stock_quantity])
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
        product_list = [product(*product) for product in self.cursor.fetchall()]
        self.disconnect()
        return product_list

    def find_by_id(self, id):
        def find_by_id(self, id):
            self.connect()
            self.cursor.execute("select * from product where id=?", [id])
            product_list = [product(*product) for product in self.cursor.fetchall()]
            self.disconnect()
            return product_list
