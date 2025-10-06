import sqlite3
from model.entity.order_item import OrderItems


class OrderItemsRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/bank.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, order_items):
        self.connect()
        self.cursor.execute("insert into order_items (id) values (?)" , [order_items.id])
        self.connection.commit()
        self.disconnect()

    def update(self, order_items):
        self.connect()
        self.cursor.execute("update orders set price = ? where id = ?" , [order_items.price, order_items.id])
        self.connection.commit()
        self.disconnect()

    def delete(self,id):
        self.connect()
        self.cursor.execute("delete from order_items  where id = ?", [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from orders")
        order_items_list = [OrderItems(*order_items) for order_items in self.cursor.fetchall()]
        self.disconnect()
        return order_items_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from orders where id = ?", [id])
        order_items_list = [OrderItems(*order_items) for order_items in self.cursor.fetchall()]
        self.disconnect()
        return order_items_list
