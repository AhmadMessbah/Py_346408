import sqlite3
from model.entity.warehouse import Warehouse


class WarehouseRepository:
    def connect(self):
        self.connection = sqlite3.connect("../db/selling_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, warehouse):
            self.connect()
            self.cursor.execute("""insert into warehouses (product_id,quantity) values (?,?)""", ([warehouse.product_id,warehouse.quantity]))
            self.connection.commit()
            self.disconnect()

    def update(self, warehouse):
            self.connect()
            self.cursor.execute("""update warehouses set product_id=?,quantity=? where id=?""", ([warehouse.product_id, warehouse.quantity, warehouse.id]))
            self.connection.commit()
            self.disconnect()

    def delete(self,id):
        self.connect()
        self.cursor.execute("delete from warehouses where id=?",[id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from warehouses")
        warehouse_list = [Warehouse(*warehouse) for warehouse in self.cursor.fetchall()]
        self.disconnect()
        return warehouse_list


    def find_by_id(self,id):
        self.connect()
        self.cursor.execute("select * from warehouses where id=?", [id])
        warehouse_list = [Warehouse(*warehouse) for warehouse in self.cursor.fetchall()]
        self.disconnect()
        return warehouse_list
