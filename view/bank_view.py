from tools.bank_veiw_tools import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tools import bank_validator
from model.entity.bank import Bank
from model.repository.bank_repository import BankRepository
from tools.bank_validator import name_validator, description_validator, balance_validator, account_validator

window = BankGui()


# Bank Name
bank_name= LabelWithEntry(window, "Bank Name:", 50,30)

# Account Name
account_name= LabelWithEntry(window, "Account Name:", 50,100)

# Balance
balance = LabelWithEntry(window, "Balance:", 50,170)

# Description
description= LabelWithEntry(window, "Description:", 50,240, data_type=StringVar)

# Table
table = ttk.Treeview(window,columns=[1,2,3,4,5],show="headings")
table.place(x=300,y=20)

table.heading(1, text="ID")
table.heading(2, text="Bank Name")
table.heading(3, text="Account Name")
table.heading(4, text="Balance")
table.heading(5, text="Description")

table.column(1, width=40)
table.column(2, width=60)
table.column(3, width=70)
table.column(4, width=60)
table.column(5, width=90)


Button(window, text="Save", width=10, command=save_click, fg="navy", font=("Arial", 12)).place(x=100,y=320)
Button(window, text="Delete", width=10, command= reset_form, fg="navy", font=("Arial", 12)).place(x=200, y=320)

window.mainloop()




# class BankGui:
#     def __init__(self):
#         self.window = Tk()
#         self.window.title("Bank")
#         self.window.geometry("400x500")
#         self.window.configure("sky blue")
#         self.bank_repository = BankRepository()
#
#     def get_info(self):
#
#         Label(self.window, "bank name:", fg="navy", font=("Arial", 16)).place(x=50, y=30)
#         Entry(self.window, width=30, fg="navy", font=("Arial", 15)).place(x=160, y=60)
#
#         Label(self.window, text="account name:", fg="navy", font=("Arial", 16)).place(x=50, y=100)
#         Entry(self.window, width=30, fg="navy", font=("Arial", 15)).place(x=160, y=130)
#
#         Label(self.window, text="balance:", fg="navy", font=("Arial", 16)).place(x=50, y=170)
#         Entry(self.window, width=30, fg="navy", font=("Arial", 15),).place(x=160, y=200)
#
#         Label(self.window, text="description:", fg="navy", font=("Arial", 16)).place(x=50, y=240)
#         Entry(self.window, width=30, fg="nazy", font=("Arial", 15)).place(x=160, y=270)
#
#         Button(self.window, text="save", command=self.bank_repository.save,
#                 width=10, fg="navy", font=("Arial", 12)).place(x=100, y=320)



# from controller.bank_controller import BankController
#
# name = input("Enter name : ")
# account = input("Enter account number : ")
# balance = input("Enter balance : ")
# description = input("Enter description : ")
#
# bank_controller = BankController()
# bank_controller.save(name,balance ,account,description)

