from view import *

from model.entity.bank import Bank
from controller.bank_controller import BankController

class BankView:
    def __init__(self):
        self.bank_controller= BankController()
        self.window = Tk()
        self.window.geometry("700x320")
        self.window.title("Bank")

        self.id = LabelWithEntry(self.window, "Id", 20,20, data_type=IntVar, state="readonly")
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

        self.table.bind("<<TreeviewSelect>>", self.select_from_table)

        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20,y=260)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100,y=260)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=260)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message= self.bank_controller.save(self.bank_name.get(), self.account_name.get(), self.balance.get(), self.description.get())
        if status:
            messagebox.showinfo("Bank Saved", message)
            self.reset_form()
        else:
            messagebox.showerror("Bank Save Error", message)
    def edit_click(self):
        status, message= self.bank_controller.update(self.id.get(), self.bank_name.get(), self.account_name.get(), self.balance.get(), self.description.get())
        if status:
            messagebox.showinfo("Bank Updated", message)
            self.reset_form()
        else:
            messagebox.showerror("Bank Update Error", message)
    def delete_click(self):
        status, message= self.bank_controller.delete(self.id.get())
        if status:
            messagebox.showinfo("Bank Deleted", message)
            self.reset_form()
        else:
            messagebox.showerror("Bank Delete Error", message)
    def reset_form(self):
        self.id.clear()
        self.bank_name.clear()
        self.account_name.clear()
        self.balance.clear()
        self.description.clear()
        status, bank_list = self.bank_controller.find_all()
        self.refresh_table(bank_list)

    def refresh_table(self, bank_list):
        for item in self.table.get_children():
            self.table.delete(item)

        for bank in bank_list:
            customer_tuple = tuple(bank.__dict__.values())
            self.table.insert("", END, values=customer_tuple)

    def select_from_table(self, event):
        selected_bank = self.table.item(self.table.focus())["values"]
        bank = Bank(*selected_bank)
        self.id.set(bank.id)
        self.account_name.set(bank.account)
        self.balance.set(bank.balance)
        self.description.set(bank.description)
        


