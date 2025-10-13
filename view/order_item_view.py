from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from view.component.win_table import LabelWithEntry,HeadingWithWidth

def reset_form():
    id.clear()
    order_id.clear()
    product_id.clear()
    quantity.clear()
    price.clear()
    discount.clear()
    description.clear()

def save_click():
    order_item = (id.get(), order_id.get(), product_id.get(), quantity.get(),
                  price.get(), discount.get(), description.get())

    table.insert(
        "",
        END,
        values=order_item
    )

    messagebox.showinfo("Save", "Order item has been saved")
    reset_form()

def update_click():
    pass

win = Tk()
win.title("Order Item View")
win.geometry("900x400")

# ID
id = LabelWithEntry(win, "ID:", 20,20)

# Order ID
order_id = LabelWithEntry(win, "Order ID:", 20,60)

# Product ID
product_id = LabelWithEntry(win, "Product ID:", 20,100)

# Quantity
quantity = LabelWithEntry(win, "Quantity:", 20,140)

# Price
price = LabelWithEntry(win, "Price:", 20,180)

# Discount
discount = LabelWithEntry(win, "Discount:", 20,220)

# Description
description = LabelWithEntry(win, "Description:", 20,260, data_type=StringVar)

# Table
table = ttk.Treeview(win,columns=[1,2,3,4,5,6,7],show="headings")
table.place(x=300,y=20)

table_id = HeadingWithWidth(table,1, "ID", 40)
table_order_id = HeadingWithWidth(table,2, "Order ID")
table_product_id = HeadingWithWidth(table,3, "Product ID", 70)
table_quantity = HeadingWithWidth(table,4, "Quantity")
table_price = HeadingWithWidth(table,5, "Price", 90)
table_discount = HeadingWithWidth(table,6, "Discount")
table_description = HeadingWithWidth(table,7, "Description", 140)

# table.heading(1, text="ID")
# table.heading(2, text="Order ID")
# table.heading(3, text="Product ID")
# table.heading(4, text="Quantity")
# table.heading(5, text="Price")
# table.heading(6, text="Discount")
# table.heading(7, text="Description")
#
# table.column(1, width=40)
# table.column(2, width=60)
# table.column(3, width=70)
# table.column(4, width=60)
# table.column(5, width=90)
# table.column(6, width=60)
# table.column(7, width=140)

Button(win, text="Save", width=12, command=save_click).place(x=80,y=300)
Button(win, text="Update", width=12, command=update_click).place(x=80,y=340)



win.mainloop()