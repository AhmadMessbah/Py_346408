from model import Employee, EmployeeService

class EmployeeController:
    def save(self, first_name, last_name, salary, occupation, phone_number, username, password,role):
        try:
           employee = Employee(None, first_name, last_name, salary, occupation, phone_number, username, password,role)
           employee.validate()
           service = EmployeeService()
           service.save(employee)
           return True, f"Employee Saved Successfully \n{employee}"
        except Exception as e:
            return False, e

    def update(self, id, first_name, last_name, salary, occupation, phone_number, username, password,role):
        try:
            employee = Employee(id, first_name, last_name, salary, occupation, phone_number, username, password,role)
            employee.validate()
            service = EmployeeService()
            service.update(employee)
            return True, f"Employee updated Successfully \n{employee}"
        except Exception as e:
            return False, e

    def delete(self, id):
        try:
            service = EmployeeService()
            service.delete(id)
            return True, f"employee with Id {id} deleted successfully"
        except Exception as e:
            return False, e

    def find_all(self):
        try:
            service = EmployeeService()
            return True, service.find_all()
        except Exception as e:
            return False, e

    def find_by_id(self, id):
        try:
            service = EmployeeService()
            return True,service.find_by_id(id)
        except Exception as e:
            return False, e