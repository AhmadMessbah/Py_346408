from model import Book
from service import BookService
from tools.logging import Logger


class BookController:
    @classmethod
    def save(cls, title, customer_id, employee_id, year,
             payment, publisher, isbn, status, tax=0, total_discount=0,
             total_amount=0):
        try:
            book = Book(None, title, customer_id, employee_id, year,
                          payment, publisher, isbn, status, tax, total_discount,
                          total_amount)
            book.validate()
            book = BookService.save(book)
            Logger.info(f"Book {book} saved")
            return True, f"Book Saved Successfully"
        except Exception as e:
            Logger.error(f"Book Save Error: {e}")
            return False, str(e)

    @classmethod
    def update(cls, book_id, title, customer_id, employee_id, year,
               payment, publisher, isbn, status, tax, total_discount,
               total_amount):
        try:
            book = Book(book_id, title, customer_id, employee_id, year,
                         payment, publisher, isbn, status, tax, total_discount,
                         total_amount)
            book.validate()
            book = BookService.update(book)
            Logger.info(f"Book {book} updated")
            return True, "Book Updated Successfully"
        except Exception as e:
            Logger.error(f"Book Update Error: {e}")
            return False, str(e)

    @classmethod
    def delete(cls, book_id):
        try:
            book = BookService.delete(book_id)
            Logger.info(f"Book {book_id} deleted")
            return True, f"Book Deleted Successfully"
        except Exception as e:
            Logger.error(f"Book Delete Error: {e}")
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            book_list = BookService.find_all()
            Logger.info("Book FindAll")
            return True, book_list
        except Exception as e:
            Logger.error(f"Book FindAll Error: {e}")
            return False, str(e)

    @classmethod
    def find_by_id(cls, book_id):
        try:
            book = BookService.find_by_id(book_id)
            Logger.info(f"Book FindById {book_id}")
            return True, book
        except Exception as e:
            Logger.error(f"{e} With Id {book_id}")
            return False, str(e)

    @classmethod
    def find_by_title(cls, title):
        try:
            book_list = BookService.find_by_title(title)
            Logger.info(f"Book FindByTitle {title}")
            return True, book_list
        except Exception as e:
            Logger.error(f"Book FindByTitle Error: {e}")
            return False, str(e)

    @classmethod
    def find_by_customer_id(cls, customer_id):
        try:
            book_list = BookService.find_by_customer_id(customer_id)
            Logger.info(f"Book FindByCustomerId {customer_id}")
            return True, book_list
        except Exception as e:
            Logger.error(f"Book FindByCustomerId Error: {e}")
            return False, str(e)

    @classmethod
    def find_by_employee_id(cls, employee_id):
        try:
            book_list = BookService.find_by_employee_id(employee_id)
            Logger.info(f"Book FindByEmployeeId {employee_id}")
            return True, book_list
        except Exception as e:
            Logger.error(f"Book FindByEmployeeId Error: {e}")
            return False, str(e)




