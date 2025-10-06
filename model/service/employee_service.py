from model.repository.employee_repository import EmployeeRepository


class EmployeeService:
    def __init__(self):
        self.repository = EmployeeRepository()

    def save(self, employee):
        self.repository.save(employee)

    def update(self, employee):
        self.repository.update(employee)

    def delete(self, employee_id):
        self.repository.delete(employee_id)

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, employee_id):
        return self.repository.find_by_id(employee_id)
