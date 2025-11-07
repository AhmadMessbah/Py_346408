import sqlite3
from model import Book


class BookRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/books_db.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, book):
        self.connect()
        self.cursor.execute(
            "insert into books (title, customer_id, employee_id, year, payment, publisher, isbn, status, tax, total_discount, total_amount) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [book.title, book.customer_id, book.employee_id, book.year, book.payment, book.publisher, book.isbn,
             book.status, book.tax, book.total_discount, book.total_amount])
        book.book_id = self.cursor.lastrowid
        self.connection.commit()
        self.disconnect()
        return book

    def update(self, book):
        self.connect()
        self.cursor.execute(
            "update books set title=?, customer_id=?, employee_id=?, year=?, payment=?, publisher=?, isbn=?, status=?, tax=?, total_discount=?, total_amount=? where id=?",
            [book.title, book.customer_id, book.employee_id, book.year, book.payment, book.publisher, book.isbn,
             book.status, book.tax, book.total_discount, book.total_amount, book.book_id])
        self.connection.commit()
        self.disconnect()
        return book

    def delete(self, id):
        self.connect()
        self.cursor.execute("delete from books where id=?", [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from books")
        book_list = [Book(*book) for book in self.cursor.fetchall()]
        self.disconnect()
        return book_list

    def find_by_id(self, book_id):
        self.connect()
        self.cursor.execute("select * from books where id=?", [book_id])
        book = self.cursor.fetchone()
        self.disconnect()
        if book:
            return Book(*book)
        return None

    def find_by_title(self, title):
        self.connect()
        self.cursor.execute("select * from books where title=?", [title])
        book_list = [Book(*book) for book in self.cursor.fetchall()]
        self.disconnect()
        return book_list

    def find_by_customer_id(self, customer_id):
        self.connect()
        self.cursor.execute("select * from books where customer_id=?", [customer_id])
        book_list = [Book(*book) for book in self.cursor.fetchall()]
        self.disconnect()
        return book_list

    def find_by_employee_id(self, employee_id):
        self.connect()
        self.cursor.execute("select * from books where employee_id=?", [employee_id])
        book_list = [Book(*book) for book in self.cursor.fetchall()]
        self.disconnect()
        return book_list

    def find_by_date_time_range(self, start_date_time, end_date_time):
        self.connect()
        self.cursor.execute("select * from books where date_time between ? and ?",
                            [start_date_time, end_date_time])
        book_list = [Book(*book) for book in self.cursor.fetchall()]
        self.disconnect()
        return book_list

    def find_by_date_time_range_and_customer_id(self, start_date_time, end_date_time, customer_id):
        self.connect()
        self.cursor.execute("select * from books where date_time between ? and ? and customer_id=?",
                            [start_date_time, end_date_time, customer_id])
        book_list = [Book(*book) for book in self.cursor.fetchall()]
        self.disconnect()
        return book_list


"""def initialize_database():
    books_db = "../db/books_db.db"
    create_table_sql =
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    customer_id INTEGER,
    employee_id INTEGER,
    year INTEGER,
    payment INTEGER,
    publisher TEXT,
    isbn INTEGER,
    status TEXT,
    tax INTEGER,
    total_discount INTEGER,
    total_amount INTEGER
);


    conn = None
    try:
        conn = sqlite3.connect(books_db)
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()
        print(f"Database '{books_db}' and table 'books' created successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    initialize_database()"""