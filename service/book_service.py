from repository import BookRepository #


class BookService:
    book_repository = BookRepository()

    @classmethod
    def save(cls, book):
        return cls.book_repository.save(book)

    @classmethod
    def update(cls, book):
        book_result = cls.book_repository.find_by_id(book.book_id)
        if book_result:
            return cls.book_repository.update(book)
        else:
            raise Exception("Book Not Found !!!")

    @classmethod
    def delete(cls, book_id):
        book = cls.book_repository.find_by_id(book_id)
        if book:
            cls.book_repository.delete(book_id)
            return book
        else:
            raise Exception("Book Not Found !!!")

    @classmethod
    def find_all(cls):
        return cls.book_repository.find_all()

    @classmethod
    def find_by_id(cls, book_id):
        book = cls.book_repository.find_by_id(book_id)
        if book:
            return book
        else:
            raise Exception("Book Not Found !!!")

    @classmethod
    def find_by_title(cls, title):
        return cls.book_repository.find_by_title(title)

    @classmethod
    def find_by_customer_id(cls, customer_id):
        return cls.book_repository.find_by_customer_id(customer_id)

    @classmethod
    def find_by_employee_id(cls, employee_id):
        return cls.book_repository.find_by_employee_id(employee_id)

