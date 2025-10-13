from tkinter import *
from tkinter import ttk
from view.component.lable_with_entry import LabelWithEntry

window = Tk()
window.geometry("700x320")
window.title("Bank")

id = LabelWithEntry(window, "Id", 20,20, data_type=IntVar)
bank_name= LabelWithEntry(window, "BankName", 20,60)
account_name= LabelWithEntry(window, "AccountName", 20,100)
balance = LabelWithEntry(window, "Balance", 20,140,data_type= IntVar)
description= LabelWithEntry(window, "Description", 20,180)

table = ttk.Treeview(window,columns=[1,2,3,4,5],show="headings", height=12)
table.place(x=270,y=20)

table.heading(1, text="ID")
table.heading(2, text="Bank Name")
table.heading(3, text="Account Name")
table.heading(4, text="Balance")
table.heading(5, text="Description")

table.column(1, width=40)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=60)
table.column(5, width=100)

Button(window, text="Save", width=7).place(x=20,y=260)
Button(window, text="Edit", width=7).place(x=100,y=260)
Button(window, text="Delete", width=7).place(x=180, y=260)

window.mainloop()



