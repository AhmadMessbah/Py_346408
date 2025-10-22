from view import *

from model import Employee
from controller import EmployeeController

class EmployeeView:
    def __init__(self):
        self.employee_controller = EmployeeController()
        self.window=Tk()
        self.window.title("Employee")
        self.window.geometry("1060x400")
        self.id = LabelWithEntry(self.window,"Id",20,20, data_type=IntVar, state="readonly")
        self.first_name = LabelWithEntry(self.window,"FirstName",20,60)
        self.last_name = LabelWithEntry(self.window,"LastName",20,100)
        self.salary = LabelWithEntry(self.window,"Salary",20,140,data_type=IntVar)
        self.occupation = LabelWithEntry(self.window,"Occupation",20,180)
        self.phone_number = LabelWithEntry(self.window,"PhoneNumber",20,220)
        self.username = LabelWithEntry(self.window,"Username",20,260)
        self.password = LabelWithEntry(self.window,"Password",20,300)
        self.role=LabelWithEntry(self.window,"Role",20,340)
        
        self.table=Table(self.window,
            ["Id", "FirstName","LastName","Salary","Occupation","PhoneNumber","Username","Password","Role"],
            [40,100,100,60,100,100,100,100,60],
            270,20,
            16,
            self.select_from_table)
    

        Button(self.window, text="Save", width=8, command=self.save_click).place(x=20, y=340)
        Button(self.window, text="Edit", width=8, command=self.edit_click).place(x=100, y=340)
        Button(self.window, text="Delete", width=8, command=self.delete_click).place(x=180, y=340)
        self.reset_form()
        self.window.mainloop()


    def save_click(self):
        status, message = self.employee_controller.save(self.first_name.get(), self.last_name.get(), self.salary.get(), self.occupation.get(),
                                                        self.phone_number.get(), self.username.get(), self.password.get(),self.role.get())
        if status:
            messagebox.showinfo("Employee Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Employee Save Error", message)


    def edit_click(self):
        status, message = self.employee_controller.update(self.id.get(), self.first_name.get(), self.last_name.get(), self.salary.get(),
                                                        self.occupation.get(), self.phone_number.get(), self.username.get(),self.password.get(),self.role.get())
        if status:
            messagebox.showinfo("Employee update", message)
            self.reset_form()
        else:
            messagebox.showerror("Employee update Error", message)

    def delete_click(self):
        status, message = self.employee_controller.delete(self.id.get())
        if status:
            messagebox.showinfo("Employee Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("Employee Delete Error", message)

    def reset_form(self):
        self.id.clear()
        self.first_name.clear()
        self.last_name.clear()
        self.salary.clear()
        self.occupation.clear()
        self.phone_number.clear()
        self.username.clear()
        self.password.clear()
        self.role.clear()
        status, employee_list = self.employee_controller.find_all()
        self.table.refresh_table(employee_list)

    
    def select_from_table(self,selected_employee):
                if selected_employee:
                   status,employee=self.employee_controller.find_by_id(selected_employee[0])
                   if status:
                    employee = Employee(*selected_employee)
                    self.id.set(employee.id)
                    self.first_name.set(employee.first_name)
                    self.last_name.set(employee.last_name)
                    self.salary.set(employee.salary)
                    self.occupation.set(employee.occupation)
                    self.phone_number.set(employee.phone_number)
                    self.username.set(employee.username)
                    self.password.set(employee.password)
                    self.role.set(employee.role)






