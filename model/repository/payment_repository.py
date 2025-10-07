import sqlite3


class PaymentRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, payment):
        self.connect()
        self.cursor.execute("INSERT INTO peyments (id, "
                            "transaction_type, "
                            "payment_type, "
                            "date_time, "
                            "customer_id, "
                            "total_amount,"
                            "employee_id,"
                            "description) VALUES(?,?,?,?,?,?,?,?)",
                            [payment.id,
                             payment.transaction_type,
                             payment.payment_type,
                             payment.date_time,
                             payment.customer_id,
                             payment.total_amount,
                             payment.employee_id,
                             payment.description])
        self.connection.commit()
        self.disconnect()

    def update(self, payment):
        self.connect()
        self.cursor.execute("update payments set id=?,"
                            "transaction_type=?,"
                            "payment_type=?,"
                            "date_time=?,"
                            "customer_id=?,"
                            "total_amount=?,"
                            "employee_id=?,"
                            "description=? where id=?",
                            [payment.id,
                             payment.transaction_type,
                             payment.payment_type,
                             payment.date_time,
                             payment.customer_id,
                             payment.total_amount,
                             payment.employee_id,
                             payment.description])
        self.connection.commit()
        self.disconnect()

    def delete(self, id):
        self.connect()
        self.cursor.execute("delete from payments where id=?",
                            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from payments")
        customer_list = [payment(*payment) for payment in self.cursor.fetchall()]
        self.disconnect()
        return customer_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from payment where id=?", [id])
        payment_list = [payment(*payment) for payment in self.cursor.fetchall()]
        self.disconnect()
        return payment_list
