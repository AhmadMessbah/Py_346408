from model import EmployeeRepository


class EmployeeService:
    def __init__(self):
        self.repository = EmployeeRepository()

    def save(self, employee):
        return self.repository.save(employee)

    def update(self, employee):
        employee_result = self.repository.find_by_id(employee.id)
        if employee_result:
            self.repository.update(employee)
            return employee
        else:
            raise Exception("Employee Not Found !!!")

    def delete(self, employee_id):
        employee = self.repository.find_by_id(employee_id)
        if employee:
            self.repository.delete(employee_id)
            return employee
        else:
            raise Exception("Employee Not Found !!!")

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, employee_id):
        employee = self.repository.find_by_id(employee_id)
        if employee:
            return employee
        else:
            raise Exception("Employee Not Found !!!")

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
