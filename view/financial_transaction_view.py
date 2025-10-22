from view import *

from controller.financial_transaction_controller import FinancialTransactionController
from view import *

from model.entity.financial_transaction import FinancialTransaction
from controller.customer_controller import CustomerController


class FinancialTransactionView:
    def __init__(self):
        self.financial_transaction_controller = FinancialTransactionController()
        self.window = Tk()
        self.window.geometry("1000x400")
        self.window.title("Financial transaction")

        self.id = LabelWithEntry(self.window, "Id", 20, 20, state="readonly")
        self.transaction_type = LabelWithEntry(self.window, "Type", 20, 60)
        self.customer_id = LabelWithEntry(self.window, "CustomerId", 20, 100)
        self.employee_id = LabelWithEntry(self.window, "EmployeeId", 20, 140)
        self.amount = LabelWithEntry(self.window, "Amount", 20, 180)
        self.date_time = LabelWithEntry(self.window, "Date&Time", 20, 220)
        self.payment_id = LabelWithEntry(self.window, "PaymentId", 20, 260)
        self.description = LabelWithEntry(self.window, "Description", 20, 300)

        self.table = Table(
            self.window,
            ["Id", "Type", "CustomerId", "EmployeeId","Amount","Date&Time","PaymentId", "Description"],
            [60, 100, 100, 80, 100,80,80,100],
            270, 20,
            16,
            self.select_from_table
        )


        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=340)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=340)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=340)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = self.financial_transaction_controller.save(self.transaction_type.get(),
                                                                     self.customer_id.get(), self.employee_id.get(),
                                                                     self.amount.get(), self.date_time.get(),
                                                                     self.payment_id.get(), self.description.get())
        if status:
            messagebox.showinfo("Financial_Transaction Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Financial_Transaction", message)

    def edit_click(self):
        status, message = self.financial_transaction_controller.update(self.id.get(), self.transaction_type.get(),
                                                                       self.customer_id.get(), self.employee_id.get(),
                                                                       self.amount.get(), self.date_time.get(),
                                                                       self.payment_id.get(), self.description.get())
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
        self.date_time.clear()
        self.payment_id.clear()
        self.description.clear()
        status, financial_transaction_list = self.financial_transaction_controller.find_all()
        self.table.refresh_table(financial_transaction_list)



    def select_from_table(self, selected_financial_transaction):
        if selected_financial_transaction:
            financial_transaction = FinancialTransaction(*selected_financial_transaction)
            self.id.set(financial_transaction.id)
            self.transaction_type.set(financial_transaction.transaction_type)
            self.customer_id.set(financial_transaction.customer_id)
            self.employee_id.set(financial_transaction.employee_id)
            self.amount.set(financial_transaction.amount)
            self.date_time.set(financial_transaction.date_time)
            self.payment_id.set(financial_transaction.payment_id)
            self.description.set(financial_transaction.description)
