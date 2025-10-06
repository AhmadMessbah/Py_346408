from model.repository.employee_repository import EmployeeRepository


class EmployeeService:
    def __init__(self):
        self.repository = EmployeeRepository()

    def save(self, employee_id,
             first_name,
             last_name,
             salary,
             occupation,
             phone_number,
             username,
             password):
        self.repository.save(employee_id,
                             first_name,
                             last_name,
                             salary,
                             occupation,
                             phone_number,
                             username,
                             password)

    def update(self,
               employee_id,
               first_name,
               last_name,
               salary,
               occupation,
               phone_number,
               username,
               password):
        self.repository.update(employee_id,
                               first_name,
                               last_name,
                               salary,
                               occupation,
                               phone_number,
                               username,
                               password)

    def delete(self, employee_id):
        self.repository.delete(employee_id)

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, employee_id):
        return self.repository.find_by_id(employee_id)
