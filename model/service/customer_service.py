from model.repository.customer_repository import CustomerRepository


class CustomerService:
    def __init__(self):
        self.repository = CustomerRepository()

    def save(self, customer):
        self.repository.save(customer)

    def update(self, customer):
        self.repository.update(customer)

    def delete(self, id):
        self.repository.delete(id)

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, id):
        return self.repository.find_by_id(id)
