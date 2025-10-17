from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from view.component.lable_with_entry import LabelWithEntry
from controller.bank_controller import BankController

class BankView:
    def __init__(self):
        self.bank_controller= BankController()
        self.window = Tk()
        self.window.geometry("700x320")
        self.window.title("Bank")

        id = LabelWithEntry(self.window, "Id", 20,20, data_type=IntVar, state="readonly")
        self.bank_name= LabelWithEntry(self.window, "BankName", 20,60)
        self.account_name= LabelWithEntry(self.window, "AccountName", 20,100)
        self.balance = LabelWithEntry(self.window, "Balance", 20,140,data_type= IntVar)
        self.description= LabelWithEntry(self.window, "Description", 20,180)

        self.table = ttk.Treeview(self.window,columns=[1,2,3,4,5],show="headings", height=12)
        self.table.place(x=270,y=20)

        self.table.heading(1, text="ID")
        self.table.heading(2, text="BankName")
        self.table.heading(3, text="AccountName")
        self.table.heading(4, text="Balance")
        self.table.heading(5, text="Description")

        self.table.column(1, width=40)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=60)
        self.table.column(5, width=100)

        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20,y=260)
        Button(self.window, text="Edit", width=7).place(x=100,y=260)
        Button(self.window, text="Delete", width=7).place(x=180, y=260)

        self.window.mainloop()

def save_click(self):
    status, message= self.bank_controller.save(self.name.get(), self.account.get(), self.balance.get(), self.description.get())
    if status:
        messagebox.showinfo("Bank saved", message)
        status, bank_list = self.bank_controller.find_all()
        self.refresh_table(bank_list)
        self.reset_form()
    else:
        messagebox.showerror("Bank save error", message)
def edit_click(self):
    pass
def delete_click(self):
    pass
def reset_form(self):
    self.id.clear()
    self.name.clear()
    self.account.clear()
    self.balance.clear()
    self.description.clear()
def refresh_table(self, bank_list):
    for item in self.table.get_children():
        self.table.delete(item)
    for bank in bank_list():
        bank_tuple= tuple(bank.__dict__.values())
        self.table.insert("", END, values(bank_tuple))



