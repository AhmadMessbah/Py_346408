import sqlite3
from model.entity.order_item import OrderItem


class OrderItemRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, order_item):
        self.connect()
        self.cursor.execute("insert into order_items (order_id, product_id , quantity, price, discount, description) values (?,?,?,?,?,?)" ,
                            [order_item.order_id, order_item.product_id, order_item.quantity, order_item.price, order_item.discount, order_item.description])
        self.connection.commit()
        self.disconnect()

    def update(self, order_item):
        self.connect()
        self.cursor.execute("update order_items set order_id=?, product_id=?, quantity=?, price=?, discount=?, description=? where id=?" ,
                            [order_item.order_id, order_item.product_id, order_item.quantity, order_item.price, order_item.discount, order_item.description, order_item.id])
        self.connection.commit()
        self.disconnect()

    def delete(self, id):
        self.connect()
        self.cursor.execute("delete from order_items where id=?", [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from order_items")
        order_item_list = [OrderItem(*order_item) for order_item in self.cursor.fetchall()]
        self.disconnect()
        return order_item_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from order_items where id=?", [id])
        order_item_list = [OrderItem(*order_item) for order_item in self.cursor.fetchall()]
        self.disconnect()
        return order_item_list

    def find_by_order_id(self, order_id):
        self.connect()
        self.cursor.execute("select * from order_items where order_id=?", [order_id])
        order_item_list = [OrderItem(*order_item) for order_item in self.cursor.fetchall()]
        self.disconnect()
        return order_item_list

