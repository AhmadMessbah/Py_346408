from tkinter import *
from tkinter import ttk
from view.component.lable_with_entry import LabelWithEntry

window = Tk()
window.title("Order Item")
window.geometry("850x360")


id = LabelWithEntry(window, "ID", 20,20, data_type=IntVar)
order_id = LabelWithEntry(window, "Order ID", 20,60)
product_id = LabelWithEntry(window, "Product ID", 20,100)
quantity = LabelWithEntry(window, "Quantity", 20,140)
price = LabelWithEntry(window, "Price", 20,180)
discount = LabelWithEntry(window, "Discount", 20,220)
description = LabelWithEntry(window, "Description", 20,260)


table = ttk.Treeview(window,columns=[1,2,3,4,5,6,7],show="headings", height=14)
table.place(x=300,y=20)

table.heading(1, text="ID")
table.heading(2, text="Order ID")
table.heading(3, text="Product ID")
table.heading(4, text="Quantity")
table.heading(5, text="Price")
table.heading(6, text="Discount")
table.heading(7, text="Description")

table.column(1, width=40)
table.column(2, width=60)
table.column(3, width=70)
table.column(4, width=60)
table.column(5, width=90)
table.column(6, width=60)
table.column(7, width=140)

Button(window, text="Save", width=7).place(x=20,y=300)
Button(window, text="Edit", width=7).place(x=100,y=300)
Button(window, text="Delete", width=7).place(x=180,y=300)

window.mainloop()