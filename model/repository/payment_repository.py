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
        self.cursor.execute("INSERT INTO peyments (peyment_id,document_type,transaction_type,date_time,customer_id,total_amount,items_list,description) VALUES(?,?)",
                           [ payment.peyment_id, payment.document_type, payment.transaction_type, payment.date_time, payment.customer_id, payment.total_amount, payment.items_list, payment.description])
        self.connection.commit()
        self.disconnect()

    def update(self, payment):
        self.connect()
        self.cursor.execute("update payments set peyment_id=?,document_type=?,transaction_type=?,date_time=?,customer_id=?,total_amount=?,items_list=?,description=? where id=?",
                            [payment.payment_id, payment.document_type, payment.transaction_type, payment.date_time, payment.customer_id, payment.total_amount, payment.items_list, payment.description])
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
        self.cursor.execute("select * from payment where id=?",[id])
        payment_list = [payment(*payment) for payment in self.cursor.fetchall()]
        self.disconnect()
        return payment_list