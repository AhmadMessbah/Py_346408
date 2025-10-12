from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox

from view.component.label_with_entry import LabelWithEntry

from tools.order_validator import *

def reset_form():
    id.clear()
    customer_id.clear()
    employee_id.clear()
    date_time.clear()
    payment_id.clear()
    warehouse_transaction_id.clear()
    tax.clear()
    total_discount.clear()
    total_amount.clear()

def save_click():
    try:
        date_validator(date_time.get())
        time_validator(date_time.get())

        order = (id.get(), customer_id.get(), employee_id.get(), date_time.get(),
                  payment_id.get(), warehouse_transaction_id.get(), tax.get(),
                  total_discount.get(), total_amount.get(), order_type.get())

        table.insert(
                "",
                END,
                values=order
                )

        messagebox.showinfo("Save", "Order has been saved")
        reset_form()
    except Exception as e:
        messagebox.showerror("Error", f"{e}")



win = Tk()
win.title("Order View")
win.geometry("1200x500")


# ID
id = LabelWithEntry(win, "ID", 20, 20)

# Customer ID
customer_id = LabelWithEntry(win, "Customer ID:", 20,60)

# Employee ID
employee_id = LabelWithEntry(win, "Employee ID:", 20,100)

# Date & Time
date_time = LabelWithEntry(win, "Date & Time:", 20,140, data_type=StringVar)

# Payment ID
payment_id = LabelWithEntry(win, "Payment ID:", 20,180)

# Warehouse Transaction ID
warehouse_transaction_id = LabelWithEntry(win, "Warehouse      \nTransaction ID:", 20,220)

# Tax
tax = LabelWithEntry(win, "Tax:", 20,270)

# Total Discount
total_discount = LabelWithEntry(win, "Total Discount:", 20,310)

# Total Amount
total_amount = LabelWithEntry(win, "Total Amount:", 20,350)

# Order Type
type_order = StringVar(value="Basket")
Label(win, text="Order Type:").place(x=20,y=390)
order_type = Combobox(win, values=["Basket","Income","Outcome"], textvariable=type_order, state="readonly")
order_type.place(x=110,y=390)

# Table
table = ttk.Treeview(win,columns=[1,2,3,4,5,6,7,8,9,10],show="headings")
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
table.column(7, width=60)
table.column(8, width=90)
table.column(9, width=90)
table.column(10, width=120)

Button(win, text="Save", width=12, command=save_click).place(x=80,y=440)



win.mainloop()