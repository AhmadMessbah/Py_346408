import sqlite3

from model.entity.sample import Sample


class SampleRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, sample):
        self.connect()
        self.cursor.execute("insert into samples (name,description) values (?,?)",
                            [sample.name, sample.description])
        self.connection.commit()
        self.disconnect()

    def update(self, sample):
        self.connect()
        self.cursor.execute("update samples set name=?,description=? where id=?",
                            [sample.name, sample.description, sample.id])
        self.connection.commit()
        self.disconnect()

    def delete(self, id):
        self.connect()
        self.cursor.execute("delete from samples where id=?",
                            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from samples")
        sample_list =  [Sample(*sample) for sample in self.cursor.fetchall()]
        self.disconnect()
        return sample_list


    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from samples where id=?", [id])
        sample_list = [Sample(*sample) for sample in self.cursor.fetchall()]
        self.disconnect()
        return sample_list
