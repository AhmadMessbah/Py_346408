from model.entity.employee import Employee
from model.service.employee_service import EmployeeService

employee = Employee( 1 , "ali" , "mohammadi" , 3 , "foroosh" , 9121946381 , "alimo" , "ali123_4")

service = EmployeeService()
service.save(employee)
