#chera khat aval khata mideh?
from view import *

from controller.financial_transaction_controller import FinancialTransactionController
from model.entity.financial_transaction import FinancialTransaction
from controller.employee_controller import EmployeeController


class FinancialTransactionView:
    def __init__(self):
        self.financial_transaction_controller = FinancialTransactionController()
        self.window = Tk()
        self.window.geometry("1000x400")
        self.window.title("Employee transaction")

        self.id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.first_name = LabelWithEntry(self.window, "FirstName", 20, 60)
        self.last_name = LabelWithEntry(self.window, "LastName", 20, 100)
        self.salary = LabelWithEntry(self.window, "Salary", 20, 140, data_type=IntVar)
        self.occupation = LabelWithEntry(self.window, "Occupation", 20, 180)
        self.phone_number = LabelWithEntry(self.window, "PhoneNumber", 20, 220)
        self.username = LabelWithEntry(self.window, "Username", 20, 260)
        self.password = LabelWithEntry(self.window, "Password", 20, 300)

        self.table = ttk.Treeview(self.window, columns=[1, 2, 3, 4, 5, 6, 7, 8], show="headings", height=16)
        self.table.place(x=270, y=20)

        self.table.heading(1, text="Id")
        self.table.heading(2, text="FirstName")
        self.table.heading(3, text="LastName")
        self.table.heading(4, text="Salary")
        self.table.heading(5, text="Occupation")
        self.table.heading(6, text="PhoneNumber")
        self.table.heading(7, text="Username")
        self.table.heading(8, text="Password")

        self.table.column(1, width=60)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=80)
        self.table.column(5, width=100)
        self.table.column(6, width=80)
        self.table.column(7, width=80)
        self.table.column(8, width=100)
        self.table.bind("<<TreeviewSelect>>", self.select_from_table)

        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=340)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=340)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=340)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = self.financial_transaction_controller.save(self.first_name.get(),
                                                                     self.last_name.get(), self.salary.get(),
                                                                     self.occupation.get(), self.phone_number.get(),
                                                                     self.username.get(), self.password.get())
        if status:
            messagebox.showinfo("Financial_Transaction Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Financial_Transaction", message)

    def edit_click(self):
        status, message = self.financial_transaction_controller.update(self.id.get(), self.first_name.get(),
                                                                       self.last_name.get(), self.salary.get(),
                                                                       self.occupation.get(), self.phone_number.get(),
                                                                       self.username.get(), self.password.get())
        if status:
            messagebox.showinfo("Financial_Transaction update", message)
            self.reset_form()
        else:
            messagebox.showerror("Financial_Transaction update error", message)

    def delete_click(self):
        status, message = self.financial_transaction_controller.delete(self.id.get())
        if status:
            messagebox.showinfo("Financial_Transaction update", message)
            self.reset_form()
        else:
            messagebox.showerror("Financial_Transaction update error", message)

    def reset_form(self):
        self.id.clear()
        self.first_name.clear()
        self.last_name.clear()
        self.salary.clear()
        self.occupation.clear()
        self.phone_number.clear()
        self.username.clear()
        self.password.clear()
        status, financial_transaction_list = self.financial_transaction_controller.find_all()
        self.refresh_table(financial_transaction_list)

    def refresh_table(self, financial_transaction_list):
        for item in self.table.get_children():
            self.table.delete(item)

        for financialtransaction in financial_transaction_list:
            financial_transaction_tuple = tuple(financialtransaction.__dict__.values())
            self.table.insert("", END, values=financial_transaction_tuple)

    def select_from_table(self, event):
        selected_financial_transaction = self.table.item(self.table.focus())["values"]
        if selected_financial_transaction:
            financial_transaction = FinancialTransaction(*selected_financial_transaction)
            self.id.set(financial_transaction.id)
            self.first_name.set(financial_transaction.transaction_type)
            (self.last_name.set(financial_transaction.customer_id))
            self.salary.set(financial_transaction.employee_id)
            self.occupation.set(financial_transaction.amount)
            self.phone_number.set(financial_transaction.date_time)
            self.username.set(financial_transaction.payment_id)
            self.password.set(financial_transaction.description)
