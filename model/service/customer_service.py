from model import CustomerRepository


class CustomerService:
    def __init__(self):
        self.repository = CustomerRepository()

    def save(self, customer):
        return self.repository.save(customer)

    def update(self, customer):
        customer_result = self.repository.find_by_id(customer.id)
        if customer_result:
            self.repository.update(customer)
            return customer
        else:
            raise Exception("Customer Not Found !!!")

    def delete(self, customer_id):
        customer = self.repository.find_by_id(customer_id)
        if customer:
            self.repository.delete(customer_id)
            return customer
        else:
            raise Exception("Customer Not Found !!!")

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, customer_id):
        customer = self.repository.find_by_id(customer_id)
        if customer:
            return customer
        else:
            raise Exception("Customer Not Found !!!")

    def find_by_firstname_and_lastname(self, firstname, lastname):
        return self.repository.find_by_firstname_and_lastname(firstname, lastname)

    def find_by_phone_number(self, phone_number):
        return self.repository.find_by_phone_number(phone_number)