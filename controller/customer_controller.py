from model import Customer, CustomerService


class CustomerController:
    def save(self, first_name, last_name, phone_number, address):
        try:
            customer = Customer(None, first_name, last_name, phone_number, address)
            customer.validate()
            service = CustomerService()
            service.save(customer)
            return True, f"Customer Saved Successfully \n{customer}"
        except Exception as e:
            return False, e

    def update(self, id, first_name, last_name, phone_number, address):
        try:
            customer = Customer(id, first_name, last_name, phone_number, address)
            customer.validate()
            service = CustomerService()
            service.update(customer)
            return True, f"Customer Updated Successfully \n{customer}"
        except Exception as e:
            return False, e

    def delete(self, id):
        try:
            service = CustomerService()
            service.delete(id)
            return True, f"Customer with Id {id} delete successfully"
        except Exception as e:
            return False, e

    def find_all(self):
        try:
            service = CustomerService()
            customer_list = service.find_all()
            return True, customer_list
        except Exception as e:
            return False, e

    def find_by_id(self, id):
        try:
            service = CustomerService()
            customer = service.find_by_id(id)
            return True, customer
        except Exception as e:
            return False, e
