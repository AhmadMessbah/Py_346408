from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from view.component.heading_with_width import HeadingWithWidth
from view.component.lable_with_entry import LabelWithEntry
from tools.order_validator import datetime_validator,datetime_parser


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
        datetime_validator(date_time.get())
        # datetime_parser(date_time.get())

        order = (id.get(), customer_id.get(), employee_id.get(), date_time.get(),
                  payment_id.get(), warehouse_transaction_id.get(), tax.get(),
                  total_discount.get(), total_amount.get(), order_type.get())

# todo *** نباید آبجکت ساخته بشه؟؟ *** الان تاپل است

        table.insert(
                "",
                END,
                values = order,
                tags = order_type.get()
                )

        messagebox.showinfo("Save", "Order has been saved")
        reset_form()
        order_type.set("Basket")
    except Exception as e:
        messagebox.showerror("Error", f"{e}")

# todo *** اتصال به دیتابیس و سیو شی


win = Tk()
win.title("Order View")
win.geometry("1200x500")


# ID
id = LabelWithEntry(win, "ID:", 20, 20)

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
order_type_list=["Basket","Income","Outgoing"]
order_type = StringVar(value="Basket")
Label(win, text="Order Type:").place(x=20,y=390)
Combobox(
    win,
    values=order_type_list,
    width=17, state="readonly"
).place(x=110,y=390)


# Table
table = ttk.Treeview(win,columns=[1,2,3,4,5,6,7,8,9,10],show="headings")
table.place(x=280,y=20)

table_id = HeadingWithWidth(table,1,"ID", 40)
table_customer_id = HeadingWithWidth(table,2,"Customer ID", 90)
table_employee_id = HeadingWithWidth(table,3,"Employee ID", 90)
table_date_time = HeadingWithWidth(table,4,"Date & Time", 140)
table_payment_id = HeadingWithWidth(table,5,"Payment ID", 90)
table_ware_trans_id = HeadingWithWidth(table,6,"Ware Trans ID", 90)
table_tax = HeadingWithWidth(table,7,"Tax")
table_total_discount = HeadingWithWidth(table,8,"Total Discount", 90)
table_total_amount = HeadingWithWidth(table,9,"Total Amount", 90)
table_order_type = HeadingWithWidth(table,10,"Order Type", 120)

# tags
table.tag_configure("Basket", background="yellow")
table.tag_configure("Income", background="light green")
table.tag_configure("Outgoing", background="light red" )


Button(win, text="Save", width=12, command=save_click).place(x=80,y=440)

win.mainloop()