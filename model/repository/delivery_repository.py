import sqlite3
from model.entity.delivery import Delivery


class DeliveryRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, delivery):
        self.connect()
        self.cursor.execute(
                "insert into deliveries (id, first_name, last_name, address, description) values (?,?,?,?,?)",
                [delivery.id, delivery.first_name, delivery.last_name, delivery.address, delivery.description])
        self.connection.commit()
        self.disconnect()

    def update(self, delivery):
        self.connect()
        self.cursor.execute(
                "update deliveries set first_name=?, last_name=?, address=?, description=? where id=?",
                [delivery.first_name, delivery.last_name, delivery.address, delivery.description, delivery.id])
        self.connection.commit()
        self.disconnect()

    def delete(self, id):
        self.connect()
        self.cursor.execute("delete from deliveries where id=?", [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from deliveries")
        delivery_list = [Delivery(*delivery) for delivery in self.cursor.fetchall()]
        self.disconnect()
        return delivery_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from deliveries where id=?", [id])
        delivery_list = [Delivery(*delivery) for delivery in self.cursor.fetchall()]
        self.disconnect()
        return delivery_list
