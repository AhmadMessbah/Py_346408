from view import *

from model.entity.employee import Employee
from controller.employee_controller import EmployeeController

class EmployeeView:
    def __init__(self):
        self.employee_controller = EmployeeController()
        self.window=Tk()
        self.window.title("Employee")
        self.window.geometry("1000x400")

        self.id = LabelWithEntry(self.window,"Id",20,20, data_type=IntVar)
        self.first_name = LabelWithEntry(self.window,"FirstName",20,60)
        self.last_name = LabelWithEntry(self.window,"LastName",20,100)
        self.salary = LabelWithEntry(self.window,"Salary",20,140,data_type=IntVar)
        self.occupation = LabelWithEntry(self.window,"Occupation",20,180)
        self.phone_number = LabelWithEntry(self.window,"PhoneNumber",20,220)
        self.username = LabelWithEntry(self.window,"Username",20,260)
        self.password = LabelWithEntry(self.window,"Password",20,300)

        self.table = ttk.Treeview(self.window,columns=[1,2,3,4,5,6,7,8],show="headings", height=16)
        self.table.place(x=270,y=20)

        self.table.heading(1, text="Id")
        self.table.heading(2, text="FirstName")
        self.table.heading(3, text="LastName")
        self.table.heading(4, text="Salary")
        self.table.heading(5, text="Occupation")
        self.table.heading(6, text="PhoneNumber")
        self.table.heading(7, text="Username")
        self.table.heading(8, text="Password")

        self.table.column(1, width=40)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=60)
        self.table.column(5, width=100)
        self.table.column(6, width=100)
        self.table.column(7, width=100)
        self.table.column(8, width=100)

        self.table.bind("<<TreeviewSelect>>", self.select_from_table)

        Button(self.window, text="Save", width=8, command=self.save_click).place(x=20, y=340)
        Button(self.window, text="Edit", width=8, command=self.edit_click).place(x=100, y=340)
        Button(self.window, text="Delete", width=8, command=self.delete_click).place(x=180, y=340)
        self.reset_form()
        self.window.mainloop()


    def save_click(self):
        status, message = self.employee_controller.save(self.first_name.get(), self.last_name.get(), self.salary.get(), self.occupation.get(),
                                                        self.phone_number.get(), self.username.get(), self.password.get())
        if status:
            messagebox.showinfo("Employee Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Employee Save Error", message)


    def edit_click(self):
        status, message = self.employee_controller.update(self.id.get(), self.first_name.get(), self.last_name.get(), self.salary.get(),
                                                        self.occupation.get(), self.phone_number.get(), self.username.get(),self.password.get())
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
        status, employee_list = self.employee_controller.find_all()
        self.refresh_table(employee_list)

    def refresh_table(self, employee_list):
        for item in self.table.get_children():
            self.table.delete(item)

        for employee in employee_list:
            employee_tuple = tuple(employee.__dict__.values())
            self.table.insert("", END, values=employee_tuple)

    def select_from_table(self, event):
                selected_employee = self.table.item(self.table.focus())["values"]
                if selected_employee:
                    employee = Employee(*selected_employee)
                    self.id.set(employee.id)
                    self.first_name.set(employee.first_name)
                    self.last_name.set(employee.last_name)
                    self.salary.set(employee.salary)
                    self.occupation.set(employee.occupation)
                    self.phone_number.set(employee.phone_number)
                    self.username.set(employee.username)
                    self.password.set(employee.password)







