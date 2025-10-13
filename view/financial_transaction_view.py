from tkinter import *
from tkinter import ttk
from view.component.lable_with_entry import *


window=Tk()
id= LabelWithEntry(window, "ID:", 20,20)

transaction_type= LabelWithEntry(window, "transaction", 20,60)

customer_id= LabelWithEntry(window, "CustomerID", 20,100)

employee_id= LabelWithEntry(window, "EmployeeID", 20,140)

amount= LabelWithEntry(window, "Amount", 20,180)


date_and_time= LabelWithEntry(window, "Date&Time", 20,220)


payment_id= LabelWithEntry(window, "PaymentID", 20,260)


description= LabelWithEntry(window, "Description", 20,300)

Button(window, text="Save", width=12).place(x=50, y=350)

Button(window, text="Delete", width=12).place(x=350, y=350)
window.mainioop()