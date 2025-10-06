from model.repository.customer_repository import CustomerRepository


class CustomerService:
    def __init__(self):
        self.repository = CustomerRepository()

    def save(self, customer_id,
             first_name,
             last_name,
             phone_number,
             address):
        self.repository.save(customer_id,
                             first_name,
                             last_name,
                             phone_number,
                             address)

    def update(self,
               customer_id,
               first_name,
               last_name,
               phone_number,
               address):
        self.repository.update(customer_id,
                               first_name,
                               last_name,
                               phone_number,
                               address)

    def delete(self, customer_id):
        self.repository.delete(customer_id)

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, customer_id):
        return self.repository.find_by_id(customer_id)
