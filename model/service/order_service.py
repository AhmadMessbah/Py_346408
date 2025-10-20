from model import OrderRepository


class OrderService:
    def __init__(self):
        self.repository = OrderRepository()

    def save(self, order):
        self.repository.save(order)

    def update(self, order):
        self.repository.update(order)

    def delete(self, id):
        self.repository.delete(id)

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, id):
        return self.repository.find_by_id(id)

    def find_by_order_type(self, order_type):
        return self.repository.find_by_order_type(order_type)

    def find_by_customer_id(self, customer_id):
        return self.repository.find_by_customer_id(customer_id)

    def find_by_employee_id(self, employee_id):
        return self.repository.find_by_employee_id(employee_id)

    def find_by_date_time_range(self, start_date_time, end_date_time):
        return self.repository.find_by_date_time_range(start_date_time, end_date_time)

    def find_by_date_time_range_and_customer_id(self, start_date_time, end_date_time, customer_id):
        return self.repository.find_by_date_time_range_and_customer_id(start_date_time, end_date_time, customer_id)
