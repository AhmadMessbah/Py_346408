from tools.book_validator import * #
from service import CustomerService, EmployeeService


class Book:
    def __init__(self, book_id, title, customer_id, employee_id, year,
                 payment, publisher, isbn, status, tax=None, total_discount=None,
                 total_amount=None):

        self.book_id = book_id
        self.title = title
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.year = year
        self.payment = payment
        self.publisher = publisher
        self.isbn = isbn
        self.status = status
        self.tax = tax
        self.total_discount = total_discount
        self.total_amount = total_amount


    def validate(self):
        datetime_validator(self.year)
        tax_validator(self.tax)
        total_discount_validator(self.total_discount)
        total_amount_validator(self.total_amount)

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        customer = CustomerService.find_by_id(self.customer_id)
        employee = EmployeeService.find_by_id(self.employee_id)

        return tuple((
            self.book_id,
            self.title,
            customer.full_name(),
            employee.full_name(),
            self.year,
            self.payment,
            self.publisher,
            self.isbn,
            self.status,
            self.tax,
            self.total_discount,
            self.total_amount,))
