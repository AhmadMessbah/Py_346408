import sqlite3
from model.entity.bank import Bank

class BankRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, bank):
        self.connect()
        self.cursor.execute("insert into bank () values (?,?)",
                            [bank., bank.])

        self.connection.commit()

        self.disconnect()

    def update(self, bank):
        self.connect()

        self.cursor.execute("update bank set name=?,description=? where id=?",
                            [bank., bank., bank.])
        self.connection.commit()

        self.disconnect()

    def delete(self, id):
        self.connect()

        self.cursor.execute("delete from bank where id=?",
                            [id])

        self.connection.commit()

        self.disconnect()

    def find_all(self):
        self.connect()
        bank_list = [Bank(*bank) for bank in self.cursor.fetchall()]
        self.connection.commit()
        self.disconnect()


    def find_by_id(self, id):
        self.connect()

        self.cursor.execute("select * from bank where id=?", [id])
        sample_list = [Bank(*bank) for bank in self.cursor.fetchall()]

        self.connection.commit()
        self.disconnect()
