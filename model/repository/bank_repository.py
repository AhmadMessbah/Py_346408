import sqlite3
from model import Bank


class BankRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, bank):
        self.connect()
        self.cursor.execute("insert into banks (name,account,balance,description) values (?,?,?,?)",
                            [bank.name, bank.account, bank.balance, bank.description])
        self.connection.commit()
        self.disconnect()

    def update(self, bank):
        self.connect()
        self.cursor.execute("update banks set name=?,account=?, balance=?,description=? where id=?",
                            [bank.name, bank.account, bank.balance, bank.description, bank.id])
        self.connection.commit()
        self.disconnect()

    def delete(self, id):
        self.connect()
        self.cursor.execute("delete from banks where id=?",
                            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from banks")
        bank_list = [Bank(*bank) for bank in self.cursor.fetchall()]
        self.disconnect()
        return bank_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from banks where id=?", [id])
        bank_list = [Bank(*bank) for bank in self.cursor.fetchall()]
        self.disconnect()
        return bank_list

    def find_by_name(self, name):
        self.connect()
        self.cursor.execute("select * from banks where name=?", [name])
        bank_list = [Bank(*bank) for bank in self.cursor.fetchall()]
        self.disconnect()
        return bank_list


    def find_by_account(self, account):
        self.connect()
        self.cursor.execute("select * from banks where account=?", [account])
        bank_list = [Bank(*bank) for bank in self.cursor.fetchall()]
        self.disconnect()
        return bank_list