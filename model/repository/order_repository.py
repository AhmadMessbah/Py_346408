import sqlite3
from model.entity.order import Order


class OrderRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, order):
        self.connect()
        self.cursor.execute("insert into orders (customer, employee, order_item_list, order_status, payment_method, payment_status, date_time)) values (?,?,?,?)" ,
                            [order.product, order.unit_price, order.quantity, order.total_price])
        self.connection.commit()
        self.disconnect()

    def update(self, order):
        self.connect()
        self.cursor.execute("update orders set unit_price = ? where id = ?" , [order.unit_price, order.id])
        self.connection.commit()
        self.disconnect()

    def delete(self,id):
        self.connect()
        self.cursor.execute("delete from orders  where id = ?", [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from orders")
        order_list = [Order(*order) for order in self.cursor.fetchall()]
        self.disconnect()
        return order_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from orders where id = ?", [id])
        found_id = Order(*self.cursor.fetchone())
        self.disconnect()
        return found_id
