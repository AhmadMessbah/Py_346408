from model import Order, OrderService


class OrderController:
    def save(self, order_type, customer_id, employee_id, date_time,
                 payment_id, warehouse_transaction_id, tax, total_discount,
                 total_amount):
        try:
            order = Order(None, order_type, customer_id, employee_id, date_time,
                 payment_id, warehouse_transaction_id, tax, total_discount,
                 total_amount)
            order.validate()
            service = OrderService()
            service.save(order)
            return True, f"Order Saved Successfully \n{order}"
        except Exception as e:            
            return False, e

    def update(self, id, order_type, customer_id, employee_id,  date_time,
                 payment_id, warehouse_transaction_id, tax, total_discount,
                 total_amount):
        try:
            order = Order(id, order_type, customer_id, employee_id, date_time,
                 payment_id, warehouse_transaction_id, tax, total_discount,
                 total_amount)
            order.validate()
            service = OrderService()
            service.update(order)
            return True, f"Order Updated Successfully \n{order}"
        except Exception as e:            
            return False, e

    def delete(self, id):
        try:
            order = OrderService()
            order.delete(id)
            return True, f"Order with Id {id} Deleted Successfully"
        except Exception as e:            
            return False,e

    def find_all(self):
        try:
            service = OrderService()
            order_list = service.find_all()
            return True, order_list
        except Exception as e:            
            return False, e

    def find_by_id(self, id):
        try:
            service = OrderService()
            order_list = service.find_by_id(id)
            return True, order_list
        except Exception as e:            
            return False, e
        
    def find_by_order_type(self, order_type):
        try:
            service = OrderService()
            order_list = service.find_by_order_type(order_type)
            return True, order_list
        except Exception as e:
            return False, e
        
    def find_by_customer_id(self, customer_id):
        try:
            service = OrderService()
            order_list = service.find_by_customer_id(customer_id)
            return True, order_list
        except Exception as e:            
            return False, e
        
    def find_by_employee_id(self, employee_id):
        try:
            service = OrderService()
            order_list = service.find_by_employee_id(employee_id)
            return True, order_list
        except Exception as e:            
            return False, e
        
    def find_by_date_time_range(self, start_date_time, end_date_time):
        try:
            service = OrderService()
            order_list = service.find_by_date_time_range(start_date_time, end_date_time)
            return True, order_list
        except Exception as e:            
            return False, e
        
    def find_by_date_time_range_and_customer_id(self, start_date_time, end_date_time, customer_id):
        try:
            service = OrderService()
            order_list = service.find_by_date_time_range_and_customer_id(start_date_time, end_date_time, customer_id)
            return True, order_list
        except Exception as e:            
            return False, e
    