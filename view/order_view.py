from view import *
from tkinter.ttk import Combobox
from model.entity.order import Order
from controller.order_controller import OrderController

class OrderView(Frame):
    def __init__(self):
        self.order_controller = OrderController()
        self.window = Tk()
        self.window.title("Order View")
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
        self.table.heading(2, text="Customer ID")
        self.table.heading(3, text="Employee ID")
        self.table.heading(4, text="Date & Time")
        self.table.heading(5, text="Payment ID")
        self.table.heading(6, text="Ware Trans ID")
        self.table.heading(7, text="Tax")
        self.table.heading(8, text="Total Discount")
        self.table.heading(9, text="Total Amount")
        self.table.heading(10, text="Order Type")

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
        pass

    def edit_click(self):
        pass

    def delete_click(self):
        pass

    def reset_form(self):
        pass

    def refresh_table(self):
        pass

    def select_from_table(self, event):
        pass