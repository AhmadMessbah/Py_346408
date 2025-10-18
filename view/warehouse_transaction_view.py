from view import  *

from model.entity.warehouse_transaction import WarehouseTransaction
from controller.warehouse_transaction_controller import WarehouseTransactionController


class WarehouseTransactionView:
    def __init__(self):
        self.warehouse_transaction_controller = WarehouseTransactionController()
        self.window = Tk()
        self.window.geometry("1000x320")
        self.window.title("Warehouse Transaction")

        self.id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.product_id = LabelWithEntry(self.window, "product Id", 20, 40, data_type=IntVar)
        self.quantity = LabelWithEntry(self.window, "quantity", 20, 60, data_type=IntVar)
        self.transaction_type = LabelWithEntry(self.window, "transaction type", 20, 100)
        self.transaction_datetime = LabelWithEntry(self.window, "transaction datetime", 20, 140, data_type=StringVar)
        self.customer_id = LabelWithEntry(self.window, "customer_id", 20, 180, data_type=IntVar)
        self.employee_id = LabelWithEntry(self.window, "employee_id", 20, 220, data_type=IntVar)

        self.table = ttk.Treeview(self.window, columns=[1, 2, 3, 4, 5, 6, 7], show="headings", height=12)
        self.table.place(x=270, y=20)

        self.table.heading(1, text="Id")
        self.table.heading(2, text="Product Id")
        self.table.heading(3, text="Quantity")
        self.table.heading(4, text="Transaction Type")
        self.table.heading(5, text="Transaction Date")
        self.table.heading(6, text="Customer Id")
        self.table.heading(7, text="Employee Id")

        self.table.column(1, width=40)
        self.table.column(2, width=80)
        self.table.column(3, width=60)
        self.table.column(4, width=100)
        self.table.column(5, width=100)
        self.table.column(6, width=90)
        self.table.column(7, width=90)

        Button(self.window, text="Save", width=7).place(x=20, y=260)
        Button(self.window, text="Edit", width=7).place(x=100, y=260)
        Button(self.window, text="Delete", width=7).place(x=180, y=260)

        self.window.mainloop()

    def save_click(self):
        status, message = self.warehouse_transaction_controller.save(self.product_id.get(),self.quantity.get(),self.transaction_type.get(),self.transaction_datetime.get(), self.employee_id.get(), self.customer_id.get())
        if status:
            messagebox.showinfo("Transaction Saved", message)
        else:
            messagebox.showerror("Transaction Save Error", message)

    def edit_click(self):
        status, message = self.warehouse_transaction_controller.update(self.product_id.get(),self.quantity.get(),self.transaction_type.get(),self.transaction_datetime.get(), self.employee_id.get(), self.customer_id.get())
        if status:
            messagebox.showinfo("Transaction Updated", message)
        else:
            messagebox.showerror("Transaction Update Error", message)
    def delete_click(self):
        status, message = self.warehouse_transaction_controller.delete(self.product_id.get(),self.quantity.get(),self.transaction_type.get(),self.transaction_datetime.get(), self.employee_id.get(), self.customer_id.get())
        if status:
            messagebox.showinfo("Transaction Deleted", message)
        else:
            messagebox.showerror("Transaction Delete Error", message)
    def reset_form(self):
        self.id.clear()
        self.product_id.clear()
        self.quantity.clear()
        self.transaction_type.clear()
        self.transaction_datetime.clear()
        self.employee_id.clear()
        self.customer_id.clear()

    def refresh_table(self, transaction_list):
        for item in self.table.get_children():
            self.table.delete(item)

        for transaction in transaction_list:
            product_tuple = tuple(transaction.__dict__.values())
            self.table.insert("", END, values=product_tuple)


    def select_from_table(self, event):
        selected_transaction = self.table.item(self.table.focus())["values"]
        transaction = WarehouseTransaction(*selected_transaction)
        self.id.set(transaction.id)
        self.product_id.set(transaction.product_id)
        self.quantity.set(transaction.quantity)
        self.transaction_type.set(transaction.transaction_type)
        self.transaction_datetime.set(transaction.transaction_datetime)
        self.employee_id.set(self.customer_id)







