from model.repository.customer_repository import CustomerRepository

class CustomerService:
    def __init__(self):
        self.repository = CustomerRepository()

    def save(self, customer):
        if not customer.first_name or not customer.last_name:
            raise ValueError("First name and last name are required fields.")
        customer.id = None
        return self.repository.save(customer)

    def update(self,customer):
        if id is None:
            raise ValueError("ID must be provided for update operation.")
        existing_customer = self.repository.find_by_id(id)
        if not existing_customer:
            raise ValueError(f"Customer with ID {id} not found. Cannot update.")
        #
        return self.repository.update(customer)

    def delete(self, id):
        if id is None:
            raise ValueError("ID must be provided for deletion.")
        if not self.repository.find_by_id(id):
            raise ValueError(f"Customer with ID {id} not found for deletion.")
        return self.repository.delete(id)

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, id):
        customer = self.repository.find_by_id(id)
        return customer

