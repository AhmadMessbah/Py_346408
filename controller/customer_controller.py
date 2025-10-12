from model.entity.customer import Customer
from model.service.customer_service import CustomerService


class CustomerController:
    def save(self,first_name,last_name,phone_number,address):
        try:
            customer = Customer(None, first_name,last_name,phone_number,address)
            print("customer darkhaste zakhire kard, ok")
            service = CustomerService()
            service.save(customer)
            return True, "Saved"
        except:
            return False, "Save Error"


    def update(self,id,first_name,last_name,phone_number,address):
        try:
            customer = Customer(None, first_name,last_name,phone_number,address)
            service = CustomerService()
            service.update(customer)
            return True, "Updated successfully"
        except:
            return False, "Update Error"

    def delete(self, id):
        try:
            service = CustomerService()
            service.delete(id)
            return True, f"Customer with ID {id} delete successfully"
        except:
            return False, "delete Error"

    def find_all(self):
        try:
            service = CustomerService()
            customers = service.find_all()
            return True, customers
        except:
            return False, "Find All Error"

    def find_by_id(self, id):
        try:
            service = CustomerService()
            customer = service.find_by_id(id)
            return True, customer
        except:
            return False, "Find By ID Error"

