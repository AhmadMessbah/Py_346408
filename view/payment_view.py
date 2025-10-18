from view import *

from model.entity.payment import Payment
from controller.payment_controller import PaymentController


class PaymentView:
    def __init__(self):
        self.payment_controller = PaymentController()
        self.window = Tk()
        self.window.geometry("1050x450")
        self.window.title("Payment")

        self.id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.transaction_type = LabelWithEntry(self.window, "TransactType", 20, 60)
        self.payment_type = LabelWithEntry(self.window, "PaymentType", 20, 100)
        self.date_time = LabelWithEntry(self.window, "DateTime", 20, 140)
        self.customer_id = LabelWithEntry(self.window, "CustomerId", 20, 180, data_type=IntVar)
        self.total_amount = LabelWithEntry(self.window, "TotalAmount", 20, 220, data_type=IntVar)
        self.employee_id = LabelWithEntry(self.window, "EmployeeId", 20, 260, data_type=IntVar)
        self.description = LabelWithEntry(self.window, "Description", 20, 300)

        self.table = ttk.Treeview(self.window, columns=[1, 2, 3, 4, 5, 6, 7, 8], show="headings", height=19)
        self.table.place(x=280, y=20)

        self.table.heading(1, text="Id")
        self.table.heading(2, text="TransactType")
        self.table.heading(3, text="PaymentType")
        self.table.heading(4, text="DateTime")
        self.table.heading(5, text="CustomerId")
        self.table.heading(6, text="TotalAmount")
        self.table.heading(7, text="EmployeeId")
        self.table.heading(8, text="Description")

        self.table.column(1, width=40)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)
        self.table.column(6, width=100)
        self.table.column(7, width=100)
        self.table.column(8, width=100)

        self.table.bind("<<TreeviewSelect>>", self.select_from_table)

        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=400)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=400)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=400)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = self.payment_controller.save(self.transaction_type.get(), self.payment_type.get(),
                                                       self.date_time.get(), self.customer_id.get(),
                                                       self.total_amount.get(), self.employee_id.get(),
                                                       self.description.get())
        if status:
            messagebox.showinfo("Payment Info Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Payment Info Save Error", message)

    def edit_click(self):
        status, message = self.payment_controller.update(self.transaction_type.get(), self.payment_type.get(),
                                                         self.date_time.get(), self.customer_id.get(),
                                                         self.total_amount.get(), self.employee_id.get(),
                                                         self.description.get(), self.id.get())
        if status:
            messagebox.showinfo("Payment Info Update", message)
            self.reset_form()
        else:
            messagebox.showerror("Payment Info Update Error", message)

    def delete_click(self):
        status, message = self.payment_controller.delete(self.id.get())
        if status:
            messagebox.showinfo("Payment Info Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("Payment Info Delete Error", message)

    def reset_form(self):
        self.id.clear()
        self.transaction_type.clear()
        self.payment_type.clear()
        self.date_time.clear()
        self.customer_id.clear()
        self.total_amount.clear()
        self.employee_id.clear()
        self.description.clear()
        status, payment_list = self.payment_controller.find_all()
        self.refresh_table(payment_list)

    def refresh_table(self, payment_list):
        for item in self.table.get_children():
            self.table.delete(item)

        for payment in payment_list:
            payment_tuple = tuple(payment.__dict__.values())
            self.table.insert("", END, values=payment_tuple)

    def select_from_table(self, event):
        selected_payment = self.table.item(self.table.focus())["values"]
        if selected_payment:
            payment = Payment(*selected_payment)
            self.id.set(payment.id)
            self.transaction_type.set(payment.transaction_type)
            self.payment_type.set(payment.payment_type)
            self.date_time.set(payment.date_time)
            self.customer_id.set(payment.customer_id)
            self.total_amount.set(payment.total_amount)
            self.employee_id.set(payment.employee_id)
            self.description.set(payment.description)
