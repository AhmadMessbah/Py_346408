from model import OrderRepository


class OrderService:
    def __init__(self):
        self.repository = OrderRepository()

    def save(self, order):
        return self.repository.save(order)

    def update(self, order):
        order_result = self.repository.find_by_id(order.id)
        if order_result:
            self.repository.update(order)
            return order
        else:
            raise Exception("Order Not Found !!!")

    def delete(self, order_id):
        order = self.repository.find_by_id(order_id)
        if order:
            self.repository.delete(order_id)
            return order
        else:
            raise Exception("Order Not Found !!!")

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, order_id):
        order = self.repository.find_by_id(order_id)
        if order:
            return order
        else:
            raise Exception("Order Not Found !!!")

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