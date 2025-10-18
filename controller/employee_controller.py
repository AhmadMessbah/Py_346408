from model.entity.employee import Employee
from model.service.employee_service import EmployeeService

class EmployeeController:
    def save(self, first_name, last_name, salary, occupation, phone_number, username, password):
        try:
           employee = Employee(None, first_name, last_name, salary, occupation, phone_number, username, password)
           service = EmployeeService()
           service.save(employee)
           return True, f"Employee Saved Successfully \n{employee}"
        except:
            return False, "Save Error"

    def update(self, id, first_name, last_name, salary, occupation, phone_number, username, password):
        try:
            employee = Employee(id, first_name, last_name, salary, occupation, phone_number, username, password)
            service = EmployeeService()
            service.update(employee)
            return True, f"Employee updated Successfully \n{employee}"
        except Exception as e:
            e.with_traceback()
            return False, "Update Error"

    def delete(self, id):
        try:
            service = EmployeeService()
            service.delete(id)
            return True, f"employee with Id {id} deleted successfully"
        except:
            return False, "Delete Error"

    def find_all(self):
        try:
            service = EmployeeService()
            employee_list = service.find_all()
            return True, employee_list
        except:
            return False, "Find All Error"

    def find_by_id(self, id):
        try:
            service = EmployeeService()
            employee = service.find_by_id(id)
            return True, employee
        except:
            return False, "Find By Id Error"