from model import EmployeeRepository


class EmployeeService:
    def __init__(self):
        self.repository = EmployeeRepository()

    def save(self, employee):
        self.repository.save(employee)

    def update(self, employee):
        self.repository.update(employee)

    def delete(self, id):
        self.repository.delete(id)

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, id):
        return self.repository.find_by_id(id)

    def find_by_firstname_and_lastname(self, firstname, lastname):
        return self.repository.find_by_firstname_and_lastname(firstname, lastname)

    def find_by_phone_number(self, phone_number):
        return self.repository.find_by_phone_number(phone_number)

    def find_by_username(self, username):
        return self.repository.find_by_username(username)

    def find_by_username_and_password(self,username, password):
        return self.repository.find_by_username_and_password(username,password)

    def find_by_role(self, role):
        return self.repository.find_by_role(role)
