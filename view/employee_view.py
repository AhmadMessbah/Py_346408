from tkinter import *
from tkinter import ttk
from view.component.lable_with_entry import LabelWithEntry


window=Tk()
window.title("Employee")
window.geometry("1000x400")


#functions

def save():
    pass
def update():
    pass
def delete():
    pass

    


#id        master, label_text, x, y, distance=90, data_type=StringVa


id= LabelWithEntry(window,"Id",20,20, data_type=IntVar)
first_name= LabelWithEntry(window, "FirstName", 20,60)
last_name= LabelWithEntry(window, "LastName", 20,100)
salary = LabelWithEntry(window, "Salary", 20,140,data_type= IntVar)
occupation= LabelWithEntry(window, "Occupation", 20,180)
phone_number= LabelWithEntry(window, "PhoneNumber", 20,220)
username= LabelWithEntry(window, "Username", 20,260)
password = LabelWithEntry(window, "Password", 20,300)



table = ttk.Treeview(window,columns=[1,2,3,4,5,6,7,8],show="headings", height=16)
table.place(x=270,y=20)

table.heading(1, text="ID")
table.heading(2, text="FirstName")
table.heading(3, text="LastName")
table.heading(4, text="Salary")
table.heading(5, text="Occupation")
table.heading(6, text="PhoneNumber")
table.heading(7, text="Username")
table.heading(8, text="Password")

table.column(1, width=40)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=60)
table.column(5, width=100)
table.column(6, width=100)
table.column(7, width=100)
table.column(8, width=100)

Button(window, text="Save", width=8).place(x=20,y=340)
Button(window, text="Edit", width=8).place(x=100,y=340)
Button(window, text="Delete", width=8).place(x=180, y=340)






window.mainloop()