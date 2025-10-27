from tools.book_validator import * #

class Book:
    def __init__(self, book_id, title, customer_id, employee_id, year,
                 payment, publisher, isbn, status, tax=None, total_discount=None,
                 total_amount=None ):

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
        year_validator(self.year)
        tax_validator(self.tax)
        total_discount_validator(self.total_discount)
        total_amount_validator(self.total_amount)
        isbn_validator(self.isbn)

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        from service.customer_service import CustomerService
        from service.employee_service import EmployeeService

        try:
            customer = CustomerService.find_by_id(self.customer_id)
            customer_name = f"{customer.first_name} {customer.last_name}" if customer else "Unknown"
        except:
            customer_name = "Unknown"

        try:
            employee = EmployeeService.find_by_id(self.employee_id)
            employee_name = f"{employee.first_name} {employee.last_name}" if employee else "Unknown"
        except:
            employee_name = "Unknown"



        return (
            self.book_id,
            self.title,
            customer_name,
            employee_name,
            self.year,
            self.payment,
            self.publisher,
            self.isbn,
            self.status,
            self.tax,
            self.total_discount,
            self.total_amount
        )