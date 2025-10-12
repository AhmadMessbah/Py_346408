from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tools import bank_validator
from model.entity.bank import Bank
from tools.bank_validator import name_validator, description_validator, balance_validator, account_validator
class BankGui:
    def __init__(self):
        self.window = Tk()
        self.window.title("Bank")
        self.window.geometry("400x500")
        self.window.configure("sky blue")
        self.bank_repository = BankRepository()

def to_tuple(self):
    return tuple(self.name,self.account,self.balance,self.description)


def reset_form():
    name.clear()
    account.clear()
    balance.clear()
    description.clear()


def save_click():
    try:

        name_validator(name.get())
        account_validator(account.get())
        balance_validator(balance.get())
        description_validator(description.get())

        bank = (name.get(), account.get(), balance.get(), description.get())

        table.insert(
            "",
            END,
            values=bank
        )

        messagebox.showinfo("Save", "Bank has been saved")
        reset_form()
    except Exception as e:
        messagebox.showerror("Error", f"{e}")
class LabelWithEntry:
    def __init__(self, master, label_text, x, y, distance_1=110,distance_2=30 ,data_type=IntVar):
        self.data_type = data_type
        self.variable = data_type()
        Label(master, text=label_text, fg="navy",font=("Arial", 16)).place(x=x, y=y)
        Entry(master, textvariable=self.variable, fg="navy",font=("Arial", 16)).place(x=x + distance_1, y=y+distance_2)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)

    def clear(self):
        if self.data_type == StringVar:
            self.variable.set("")
        else:
            raise ValueError("Invalid Type")


class Table:
    def __init__(self, window):
        self.table = ttk.Treeview(window, columns=[1, 2, 3, 4, 5], show="headings")
        self.table.place(x=300,y=20)
        self.set_column_headings()
        self.set_column_widths()

    def set_column_headings(self):
        headings = ["ID", "Name", "Account", "Balance", "Description"]
        for i, heading in enumerate(headings):
            self.table.heading(i, text=heading)

    def set_column_widths(self):
        widths = [40, 60, 70, 60, 90]
        for i, width in enumerate(widths):
            self.table.column(i, width=width)
