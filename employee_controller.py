from model.entity.employee import Employee
from model.service.employee import EmployeeService

class EmployeeController:
    def save(self, first_name, last_name, salary, occupation, phone_number, username, password):
        try:
           employe = Sample(None, first_name, last_name, salary, occupation, phone_number, username, password)
           print("employee darkhaste zakhire kard, ok")
           service = EmployeeService()
           service.save(employe)
           return True, "Saved"
        except:
            return False, "Save Error"

    def update(self, id, first_name, last_name, salary, occupation, phone_number, username, password):
        try:
            #id None?
            employee = Employee(id, first_name, last_name, salary, occupation, phone_number, username, password)
            service = EmployeeService()
            service.update(employee)
            return True, "Updated Successfully"
        except:
            return False, "Update Error"

    def delete(self, id):
        try:
            service = EmployeeService()
            service.delete(id)
            return True, f"employee with ID {id} deleted successfully"
        except:
            return False, "Delete Error"

    def find_all(self):
        try:
            service = EmployeeService()
            employees = service.find_all()
            return True, employees
        except:
            return False, "Find All Error"

    def find_by_id(self, id):
        try:
            service = EmployeeService()
            employee = service.find_by_id(id)
            return True, employee
        except:
            return False, "Find By ID Error"