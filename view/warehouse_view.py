from tkinter import *
from tkinter import ttk
from view.component.lable_with_entry import LabelWithEntry

window = Tk()
window.geometry("750x320")
window.title("Warehouse View")

id= LabelWithEntry(window, "ID", 20,20, data_type=IntVar)
product_id= LabelWithEntry(window, "Product_id", 20,60)
quantity= LabelWithEntry(window, "Quantity", 20,100)



table = ttk.Treeview(window,columns=[1,2,3],show="headings", height=12)
table.place(x=270,y=20)

table.heading(1, text="ID")
table.heading(2, text="Product_ID")
table.heading(3, text="Quantity")



table.column(1, width=30)
table.column(2, width=100)
table.column(3, width=100)



Button(window, text="Save", width=7).place(x=20,y=260)
Button(window, text="Edit", width=7).place(x=100,y=260)
Button(window, text="Delete", width=7).place(x=180, y=260)

window.mainloop()


