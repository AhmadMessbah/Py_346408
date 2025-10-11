import sqlite3
from model.entity.bank import Bank

class BankRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/bank.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, bank):
        self.connect()
        self.cursor.execute("insert into bank (name,account,balance,decription) values (?,?,?,?)",
                            [bank.name,bank.account,bank.balance,bank.description])
        self.connection.commit()
        self.disconnect()

    def update(self, bank):
        self.connect()
        self.cursor.execute("update bank set name=?,account=?, balance=?,description=? where id=?",
                            [bank.name,bank.account,bank.balance,bank.description])
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
        self.cursor.execute("select * from bank")
        bank_list =  [Bank(*bank) for bank in self.cursor.fetchall()]
        self.disconnect()
        return bank_list


    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from bank where id=?", [id])
        bank_list = [Bank(*bank) for bank in self.cursor.fetchall()]
        self.disconnect()
        return bank_list
