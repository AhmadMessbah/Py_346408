from view import *


from model.entity.employee import Employee
from controller.employee_controller import EmployeeController

class EmployeeView:
    def __init__(self):
        self.employee_controller = EmployeeController()
        self.window=Tk()
        self.window.title("Employee")
        self.window.geometry("1000x400")



        self.id= LabelWithEntry(self.window,"Id",20,20, data_type=IntVar)
        self.first_name= LabelWithEntry(self.window, "FirstName", 20,60)
        self.last_name= LabelWithEntry(self.window, "LastName", 20,100)
        self.salary = LabelWithEntry(self.window, "Salary", 20,140,data_type= IntVar)
        self.occupation= LabelWithEntry(self.window, "Occupation", 20,180)
        self.phone_number= LabelWithEntry(self.window, "PhoneNumber", 20,220)
        self.  username= LabelWithEntry(self.window, "Username", 20,260)
        self.password = LabelWithEntry(self.window, "Password", 20,300)



        self.table = ttk.Treeview(self.window,columns=[1,2,3,4,5,6,7,8],show="headings", height=16)
        self.table.place(x=270,y=20)

        self.table.heading(1, text="ID")
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

        Button(self.window, text="Save", width=8).place(x=20,y=340)
        Button(self.window, text="Edit", width=8).place(x=100,y=340)
        Button(self.window, text="Delete", width=8).place(x=180, y=340)
        self.reset_form()
        self.window.mainloop()






