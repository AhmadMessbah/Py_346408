from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from view.component.lable_with_entry import LabelWithEntry


window = Tk()
window.title("Order View")
window.geometry("1250x510")


id = LabelWithEntry(window, "ID", 20, 20, data_type=IntVar)
customer_id = LabelWithEntry(window, "Customer ID", 20,60, data_type=IntVar)
employee_id = LabelWithEntry(window, "Employee ID", 20,100, data_type=IntVar)
date_time = LabelWithEntry(window, "Date & Time", 20,140)
payment_id = LabelWithEntry(window, "Payment ID", 20,180, data_type=IntVar)
warehouse_transaction_id = LabelWithEntry(window, "WarehouseID", 20,225, data_type=IntVar)
tax = LabelWithEntry(window, "Tax", 20,270, data_type=IntVar)
total_discount = LabelWithEntry(window, "Total Discount", 20,310, data_type=IntVar)
total_amount = LabelWithEntry(window, "Total Amount", 20,350, data_type=IntVar)


# Order Type
order_type_list=["Basket","Sell","Buy"]
order_type = StringVar(value="Basket")
Label(window, text="Order Type").place(x=20,y=390)
Combobox(
    window,
    values=order_type_list,
    textvariable=order_type,
    width=17,
    state="readonly"
).place(x=110,y=390)


# Table
table = ttk.Treeview(window,columns=[1,2,3,4,5,6,7,8,9,10],show="headings", height=21)
table.place(x=280,y=20)

table.heading(1, text="ID")
table.heading(2, text="Customer ID")
table.heading(3, text="Employee ID")
table.heading(4, text="Date & Time")
table.heading(5, text="Payment ID")
table.heading(6, text="Ware Trans ID")
table.heading(7, text="Tax")
table.heading(8, text="Total Discount")
table.heading(9, text="Total Amount")
table.heading(10, text="Order Type")

table.column(1, width=40)
table.column(2, width=90)
table.column(3, width=90)
table.column(4, width=140)
table.column(5, width=90)
table.column(6, width=90)
table.column(7, width=90)
table.column(8, width=90)
table.column(9, width=90)
table.column(10, width=120)


Button(window, text="Save", width=7).place(x=20,y=440)
Button(window, text="Edit", width=7).place(x=90,y=440)
Button(window, text="Delete", width=7).place(x=160,y=440)


window.mainloop()