# total_amount    discount     tax    final_amount    payment_method    payment_status    order_status
# delivery_date     delivery_address    notes     (customer_id , employee_id)

class Order:
    def __init__(self, id, customer,employee, order_item_list, date_time):
        self.id = id
        self.customer = customer
        self.employee = employee
        self.order_item_list = order_item_list
        self.date_time = date_time

    def __repr__(self):
        return f"{self.__dict__}"