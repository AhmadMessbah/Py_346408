from view import *

from controller.financial_transaction_controller import FinancialTransactionController
from view import *

from model.entity.financial_transaction import FinancialTransaction
from controller.customer_controller import CustomerController

class FinancialTransactionView:
    def __init__(self):
        self.financial_transaction_controller = FinancialTransactionController()
        self.window=Tk()
        self.window.geometry("1050x400")
        self.window.title("Financial transaction")

        self.id= LabelWithEntry(self.window, "ID:", 20,20)
        self.transaction_type= LabelWithEntry(self.window, "Transaction", 20,60)
        self.customer_id= LabelWithEntry(self.window, "CustomerID", 20,100)
        self.employee_id= LabelWithEntry(self.window, "EmployeeID", 20,140)
        self.amount= LabelWithEntry(self.window, "Amount", 20,180)
        self.date_and_time= LabelWithEntry(self.window, "Date&Time", 20,220)
        self.payment_id= LabelWithEntry(self.window, "PaymentID", 20,260)
        self.description= LabelWithEntry(self.window, "Description", 20,300)

        self.table = ttk.Treeview(self.window,columns=[1,2,3,4,5,6,7,8],show="headings", height=16)
        self.table.place(x=270,y=20)

        self.table.heading(1, text="ID")
        self.table.heading(2, text="Transaction")
        self.table.heading(3, text="CustomerID")
        self.table.heading(4, text="EmployeeID")
        self.table.heading(5, text="Amount")
        self.table.heading(6, text="Date&Time")
        self.table.heading(7, text="PaymentID")
        self.table.heading(8, text="Description")

        self.table.column(1, width=40)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=60)
        self.table.column(5, width=100)
        self.table.column(6, width=60)
        self.table.column(7, width=60)
        self.table.column(8, width=100)
        self.table.bind("<<TreeviewSelect>>", self.select_from_table)

        Button(self.window, text="Save", width=7).place(x=20,y=340)
        Button(self.window, text="Edit", width=7).place(x=100,y=340)
        Button(self.window, text="Delete", width=7).place(x=180, y=340)
        self.reset_form()
        self.window.mainloop()


    def save_click(self):
        status, message = self.financial_transaction_controller.save(self.transaction_type.get(), self.employee_id.get(), self.amount.get(), self.date_and_time.get(),self.payment_id.get(),self.description.get())
        if status:
            messagebox.showinfo("Financial_Transaction Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Financial_Transaction", message)

    def edit_click(self):
        status, message = self.financial_transaction_controller.update(self.id.get(),self.transaction_type.get(), self.employee_id.get(),
                                                                       self.amount.get(), self.date_and_time.get(),self.payment_id.get(),self.description.get())
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
        self.transaction_type.clear()
        self.customer_id.clear()
        self.employee_id.clear()
        self.amount.clear()
        self.date_and_time.clear()
        self.payment_id.clear()
        self.description.clear()
        status, financial_transaction_list = self.financial_transaction_controller.find_all()
        self.refresh_table(financial_transaction_list)

    def refresh_table(self, financial_transaction_list):
        for item in self.table.get_children():
            self.table.delete(item)

        for customer in financial_transaction_list:
            financial_transaction_tuple = tuple(customer.__dict__.values())
            self.table.insert("", END, values=financial_transaction_tuple)

    def select_from_table(self, event):
        selected_financial_transaction = self.table.item(self.table.focus())["values"]
        if selected_financial_transaction:
            financial_transaction = financial_transaction (*selected_financial_transaction)
            self.id.set(financial_transaction.id)
            self.transaction_type.set(financial_transaction.transaction_type)
            self.employee_id.set(financial_transaction.employee_id)
            self.amount.set(financial_transaction.amount)
            self.date_and_time.set(financial_transaction.date_and_time)
            self.payment_id.set(financial_transaction.payment_id)
            self.description.set(financial_transaction.description)

