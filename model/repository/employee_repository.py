import sqlite3

class EmployeeRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, employee):
        self.connect()
        self.cursor.execute("INSERT INTO employees (employee_id,first_name,last_name,salary,occupation,phone_number,username,password) VALUES(?,?)",
                           [ employee.employee_id, employee.first_name,employee.last_name,employee.salary,employee.occupation,employee.phone_number,employee.username,employee.password])
        self.connection.commit()
        self.disconnect()

    def update(self, employee):
        self.connect()
        self.cursor.execute("update employees set employee_id=?,first_name=?,last_name=?,salary=?,occuption=?,phone_number=?,username=?,password where id=?",
                            [employee.employee_id, employee.first_name, employee.last_name,employee.salary,employee.occupation,employee.phone_number,employee.username,employee.password])
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
        customer_list = [employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return customer_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from employees where id=?",[id])
        employee_list = [employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return employee_list
