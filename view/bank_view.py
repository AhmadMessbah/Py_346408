from view import *
from model import Bank
from controller import BankController

class BankView:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("700x320")
        self.window.title("Bank")

        self.id = LabelWithEntry(self.window, "Id", 20,20, data_type=IntVar, state="readonly")
        self.bank_name= LabelWithEntry(self.window, "BankName", 20,60)
        self.account_name= LabelWithEntry(self.window, "AccountName", 20,100)
        self.balance = LabelWithEntry(self.window, "Balance", 20,140,data_type= IntVar)
        self.description= LabelWithEntry(self.window, "Description", 20,180)

        self.table = Table(
            self.window,
            ["Id", "BankName", "AccountName", "Balance", "Description"],
            [40,100,100,60,100],
            270,20,
            12,
            self.select_from_table
        )

        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20,y=260)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100,y=260)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=260)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message= BankController.save(self.bank_name.get(), self.account_name.get(), self.balance.get(), self.description.get())
        if status:
            messagebox.showinfo("Bank Saved", message)
            self.reset_form()
        else:
            messagebox.showerror("Bank Save Error", message)
    def edit_click(self):
        status, message= BankController.update(self.id.get(), self.bank_name.get(), self.account_name.get(), self.balance.get(), self.description.get())
        if status:
            messagebox.showinfo("Bank Updated", message)
            self.reset_form()
        else:
            messagebox.showerror("Bank Update Error", message)
    def delete_click(self):
        status, message= BankController.delete(self.id.get())
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
        status, bank_list = BankController.find_all()
        self.table.refresh_table(bank_list)

    def select_from_table(self, selected_bank):
        if selected_bank:
            status, bank = BankController.find_by_id(selected_bank[0])
            if status:
                bank = Bank(*selected_bank)
                self.id.set(bank.id)
                self.bank_name.set(bank.name)
                self.account_name.set(bank.account)
                self.balance.set(bank.balance)
                self.description.set(bank.description)



