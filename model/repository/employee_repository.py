import sqlite3
from model import Employee


class EmployeeRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, employee):
        self.connect()
        self.cursor.execute(
            "insert into employees (first_name, last_name, salary, occupation, phone_number, username, password, role) values (?,?,?,?,?,?,?,?)",
            [employee.first_name, employee.last_name, employee.salary, employee.occupation, employee.phone_number,
             employee.username, employee.password, employee.role])
        self.connection.commit()
        self.disconnect()

    def update(self, employee):
        self.connect()
        self.cursor.execute(
            "update employees set first_name=?, last_name=?, salary=?, occupation=?, phone_number=?, username=?, password=?, role=? where id=?",
            [employee.first_name, employee.last_name, employee.salary, employee.occupation, employee.phone_number,
             employee.username, employee.password,employee.role, employee.id])
        self.connection.commit()
        self.disconnect()

    def delete(self, id):
        self.connect()
        self.cursor.execute("delete from employees where id=?",
                            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from employees")
        customer_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return customer_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from employees where id=?", [id])
        employee_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return employee_list
    
   
    def find_by_firstname_and_lastname(self,firstname, lastname):
        self.connect()
        self.cursor.execute("select * from employees where firstname=?  lastname=? ", [firstname, lastname])
        employee_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return employee_list
    
    def find_by_phone_number(self, phone_number):
        self.connect()
        self.cursor.execute("select * from employees where phone_number=?", [phone_number])
        employee_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return employee_list
    
    
    
    def find_by_username(self, username):
        self.connect()
        self.cursor.execute("select * from employees where username=?", [username])
        employee_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return employee_list
    
    
    
    def find_by_username_and_password(self, username,password):
        self.connect()
        self.cursor.execute("select * from employees where iusername=? password=?", [username,password])
        employee_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return employee_list
    
    
    
    def find_by_role(self, role):
        self.connect()
        self.cursor.execute("select * from employees where role=?", [role])
        employee_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return employee_list