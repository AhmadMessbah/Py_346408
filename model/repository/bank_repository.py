import sqlite3

class BankRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, bank):
        self.connect()

        self.disconnect()

    def update(self, bank):
        pass

    def delete(self, id):
        pass

    def find_all(self):
        pass

    def find_by_id(self, id):
        pass
