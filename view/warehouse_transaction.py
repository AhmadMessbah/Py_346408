from tkinter import *
from tkinter import ttk
from view.component.lable_with_entry import LabelWithEntry

window = Tk()
window.geometry("1000x320")
window.title("Warehouse Transaction")

id = LabelWithEntry(window, "Id", 20,20, data_type=IntVar)
pid = LabelWithEntry(window, "product Id", 20,40, data_type=IntVar)
quantity= LabelWithEntry(window, "quantity", 20,60,data_type=IntVar)
transaction_type = LabelWithEntry(window, "transaction type", 20,100)
transaction_datetime = LabelWithEntry(window, "transaction datetime", 20,140,data_type=StringVar)
customer_id = LabelWithEntry(window, "customer_id", 20,180,data_type=IntVar)
employee_id = LabelWithEntry(window, "employee_id", 20,220,data_type=IntVar)

table = ttk.Treeview(window,columns=[1,2,3,4,5,6,7],show="headings", height=12)
table.place(x=270,y=20)

table.heading(1, text="ID")
table.heading(2, text="Product Id")
table.heading(3, text="Quantity")
table.heading(4, text="Transaction Type")
table.heading(5, text="Transaction Date")
table.heading(6, text="Customer ID")
table.heading(7, text="Employee ID")

table.column(1, width=40)
table.column(2, width=80)
table.column(3, width=60)
table.column(4, width=100)
table.column(5, width=100)
table.column(6, width=90)
table.column(7, width=90)

Button(window, text="Save", width=7).place(x=20,y=260)
Button(window, text="Edit", width=7).place(x=100,y=260)
Button(window, text="Delete", width=7).place(x=180, y=260)

window.mainloop()



