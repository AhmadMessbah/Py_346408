from tkinter import *
from tkinter import ttk
from view.component.lable_with_entry import LabelWithEntry

window = Tk()
window.geometry("1050x420")
window.title("Payment")

id = LabelWithEntry(window, "Id", 20,20, data_type=IntVar)
transaction_type= LabelWithEntry(window, "TransactionType", 20,60)
payment_type= LabelWithEntry(window, "PaymentType", 20,100)
date_time = LabelWithEntry(window, "DateTime", 20,140)
customer_id= LabelWithEntry(window, "CustomerId", 20,180, data_type=IntVar)
total_amount = LabelWithEntry(window, "TotalAmount", 20,220, data_type=IntVar)
employee_id = LabelWithEntry(window, "EmployeeId", 20,260, data_type=IntVar)
description= LabelWithEntry(window, "Description", 20,300)

table = ttk.Treeview(window,columns=[1,2,3,4,5,6,7,8],show="headings", height=17)
table.place(x=270,y=20)

table.heading(1, text="ID")
table.heading(2, text="Transaction Type")
table.heading(3, text="Payment Type")
table.heading(4, text="Date Time")
table.heading(5, text="Customer Id")
table.heading(6, text="Total Amount")
table.heading(7, text="Employee Id")
table.heading(8, text="Description")

table.column(1, width=40)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)
table.column(5, width=100)
table.column(6, width=100)
table.column(7, width=100)
table.column(8, width=100)

Button(window, text="Save", width=7).place(x=20,y=360)
Button(window, text="Edit", width=7).place(x=100,y=360)
Button(window, text="Delete", width=7).place(x=180, y=360)

window.mainloop()
