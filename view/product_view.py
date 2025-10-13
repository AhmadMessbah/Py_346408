from tkinter import *
from tkinter import ttk
from view.component.lable_with_entry import LabelWithEntry

window = Tk()
window.geometry("1000x440")
window.title("product")

Id = LabelWithEntry(window, "Id", 20,20, data_type=IntVar)
Name= LabelWithEntry(window, "Name", 20,60)
Brand= LabelWithEntry(window, "Brand", 20,100)
Model = LabelWithEntry(window, "Model", 20,140,data_type= IntVar)
Serial= LabelWithEntry(window, "Serial", 20,180)
category = LabelWithEntry(window, "Category", 20,220)
Unit= LabelWithEntry(window, "Unit", 20,260)
ExpirationDate= LabelWithEntry(window, "ExpirationDate", 20,300)

table = ttk.Treeview(window,columns=[1,2,3,4,5,6,7,8,],show="headings", height=18)
table.place(x=270,y=20)

table.heading(1, text="Id")
table.heading(2, text="Name")
table.heading(3, text="Brand")
table.heading(4, text="Model")
table.heading(5, text="Serial")
table.heading(6, text="Category")
table.heading(7, text="Unit")
table.heading(8, text="ExpirationDate")

table.column(1, width=40)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=60)
table.column(5, width=100)
table.column(6, width=100)
table.column(7, width=100)
table.column(8, width=100)


Button(window, text="Save", width=7).place(x=20,y=380)
Button(window, text="Edit", width=7).place(x=100,y=380)
Button(window, text="Delete", width=7).place(x=180, y=380)

window.mainloop()