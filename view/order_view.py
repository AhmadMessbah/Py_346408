from view import *
from tkinter.ttk import Combobox

from model.entity.order import Order
from controller.order_controller import OrderController

class OrderView:
    def __init__(self):
        self.order_controller = OrderController()
        self.window = Tk()
        self.window.title("Order")
        self.window.geometry("1250x510")

        self.id = LabelWithEntry(self.window, "ID", 20, 20, data_type=IntVar, state="readonly")
        self.customer_id = LabelWithEntry(self.window, "Customer ID", 20, 60, data_type=IntVar)
        self.employee_id = LabelWithEntry(self.window, "Employee ID", 20, 100, data_type=IntVar)
        self.date_time = LabelWithEntry(self.window, "Date & Time", 20, 140)
        self.payment_id = LabelWithEntry(self.window, "Payment ID", 20, 180, data_type=IntVar)
        self.warehouse_transaction_id = LabelWithEntry(self.window, "Ware Trans ID", 20, 225, data_type=IntVar)
        self.tax = LabelWithEntry(self.window, "Tax", 20, 270, data_type=IntVar)
        self.total_discount = LabelWithEntry(self.window, "Total Discount", 20, 310, data_type=IntVar)
        self.total_amount = LabelWithEntry(self.window, "Total Amount", 20, 350, data_type=IntVar)

        self.order_type_list = ["Basket", "Sell", "Buy"]
        self.order_type = StringVar(value="Basket")
        Label(self.window, text="Order Type").place(x=20, y=390)
        Combobox(
            self.window,
            values=self.order_type_list,
            textvariable=self.order_type,
            width=17,
            state="readonly"
        ).place(x=110, y=390)

        self.table = ttk.Treeview(self.window, columns=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], show="headings", height=21)
        self.table.place(x=280, y=20)

        self.table.heading(1, text="ID")
        self.table.heading(2, text="Order Type")
        self.table.heading(3, text="Customer ID")
        self.table.heading(4, text="Employee ID")
        self.table.heading(5, text="Date & Time")
        self.table.heading(6, text="Payment ID")
        self.table.heading(7, text="Ware Trans ID")
        self.table.heading(8, text="Tax")
        self.table.heading(9, text="Total Discount")
        self.table.heading(10, text="Total Amount")

        self.table.column(1, width=40)
        self.table.column(2, width=90)
        self.table.column(3, width=90)
        self.table.column(4, width=140)
        self.table.column(5, width=90)
        self.table.column(6, width=90)
        self.table.column(7, width=90)
        self.table.column(8, width=90)
        self.table.column(9, width=90)
        self.table.column(10, width=120)

        self.table.bind("<<TreeviewSelect>>", self.select_from_table)

        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=440)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=97, y=440)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=175, y=440)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = self.order_controller.save(self.order_type.get(), self.customer_id.get(), self.employee_id.get(),
                                                     self.date_time.get(),self.payment_id.get(),
                                                     self.warehouse_transaction_id.get(), self.tax.get(),
                                                     self.total_discount.get(), self.total_amount.get())
        if status:
            messagebox.showinfo("Order Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Order Save Error", message)

    def edit_click(self):
        status, message = self.order_controller.update(self.id.get(), self.order_type.get(), self.customer_id.get(), self.employee_id.get(),
                                                       self.date_time.get(), self.payment_id.get(), self.warehouse_transaction_id.get(),
                                                       self.tax.get(), self.total_discount.get(), self.total_amount.get())
        if status:
            messagebox.showinfo("Order Update", message)
            self.reset_form()
        else:
            messagebox.showerror("Order Update Error", message)

    def delete_click(self):
        status, message = self.order_controller.delete(self.id.get())
        if status:
            messagebox.showinfo("Order Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("Order Delete Error", message)

    def reset_form(self):
        self.id.clear()
        self.order_type_list.clear()
        self.customer_id.clear()
        self.employee_id.clear()
        self.date_time.clear()
        self.payment_id.clear()
        self.warehouse_transaction_id.clear()
        self.tax.clear()
        self.total_discount.clear()
        self.total_amount.clear()
        status, order_list = self.order_controller.find_all()
        self.refresh_table(order_list)

    def refresh_table(self, order_list):
        for item in self.table.get_children():
            self.table.delete(item)

        for order in order_list:
            order_tuple = tuple(order.__dict__.values())
            self.table.insert("", END, values=order_tuple)

    def select_from_table(self, event):
        selected_order = self.table.item(self.table.focus())["values"]
        if selected_order:
            order = Order(*selected_order)
            self.id.set(order.id)
            self.order_type.set(order.order_type)
            self.customer_id.set(order.customer_id)
            self.employee_id.set(order.employee_id)
            self.date_time.set(order.date_time)
            self.payment_id.set(order.payment_id)
            self.warehouse_transaction_id.set(order.warehouse_transaction_id)
            self.tax.set(order.tax)
            self.total_discount.set(order.total_discount)
            self.total_amount.set(order.total_amount)
