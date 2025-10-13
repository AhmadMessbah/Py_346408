from tkinter import *
from tkinter import ttk
from view.component.lable_with_entry import *


window=Tk()
window.geometry("700x400")
window.title("Financial transaction")

id= LabelWithEntry(window, "ID:", 20,20)
transaction_type= LabelWithEntry(window, "transaction", 20,60)
customer_id= LabelWithEntry(window, "CustomerID", 20,100)
employee_id= LabelWithEntry(window, "EmployeeID", 20,140)
amount= LabelWithEntry(window, "Amount", 20,180)
date_and_time= LabelWithEntry(window, "Date&Time", 20,220)
payment_id= LabelWithEntry(window, "PaymentID", 20,260)
description= LabelWithEntry(window, "Description", 20,300)

table = ttk.Treeview(window,columns=[1,2,3,4,5,6,7,8],show="headings", height=12)
table.place(x=270,y=20)

table.heading(1, text="ID")
table.heading(2, text="")
table.heading(3, text="")
table.heading(4, text="")
table.heading(5, text="")
table.heading(6, text="")
table.heading(7, text="")
table.heading(8, text="Description")

table.column(1, width=40)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=60)
table.column(5, width=100)

Button(window, text="Save", width=7).place(x=20,y=260)
Button(window, text="Edit", width=7).place(x=100,y=260)
Button(window, text="Delete", width=7).place(x=180, y=260)

window.mainloop()
