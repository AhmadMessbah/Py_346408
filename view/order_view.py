from test.order_test import order
from view import *
from tkinter.ttk import Combobox

from model.entity.order import Order
from controller.order_controller import OrderController

class OrderView:
    def __init__(self):

        self.order_controller = OrderController()

        self.window = Tk()
        self.window.title("Order")
        self.window.geometry("1310x510")

        self.id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.customer_id = LabelWithEntry(self.window, "Customer Id", 20, 60, data_type=IntVar)
        self.employee_id = LabelWithEntry(self.window, "Employee Id", 20, 100, data_type=IntVar)
        self.date_time = LabelWithEntry(self.window, "Date & Time", 20, 140)
        self.payment_id = LabelWithEntry(self.window, "Payment Id", 20, 180, data_type=IntVar)
        self.warehouse_transaction_id = LabelWithEntry(self.window, "Ware Trans Id", 20, 225, data_type=IntVar)
        self.tax = LabelWithEntry(self.window, "Tax", 20, 270, data_type=IntVar)
        self.total_discount = LabelWithEntry(self.window, "Total Discount", 20, 310, data_type=IntVar)
        self.total_amount = LabelWithEntry(self.window, "Total Amount", 20, 350, data_type=IntVar)

        order_type_list = ["Basket", "Sell", "Buy"]
        type_order = StringVar(value="Basket")
        Label(self.window, text="Order Type").place(x=20, y=390)
        self.order_type = Combobox(
            self.window,
            values=order_type_list,
            textvariable=type_order,
            width=17,
            state="readonly")
        self.order_type.place(x=110, y=390)

        self.table = Table(
            self.window,
            ["Id", "Order Type", "Customer", "Employee", "Date & Time", "Total Amount", "Total Discount", "Total Discount"],
            [40, 90, 120, 120,140, 90, 90, 90, 90, 120],
            280, 20,
            21,
            self.select_from_table
        )


        # v_scroll = ttk.Scrollbar(self.window, command=self.table.yview)
        # self.table.configure(yscrollcommand=v_scroll.set(0.0,0.4))
        # v_scroll.place(x=1212, y=20, height=445)


        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=440)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=97, y=440)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=175, y=440)
        Button(self.window, text="View Order", width=21,command=self.order_item_view).place(x=20, y=480)

        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = self.order_controller.save(self.order_type.get(), self.customer_id.get(), self.employee_id.get(),
                                                     self.date_time.get(), self.payment_id.get(),
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
        self.customer_id.clear()
        self.employee_id.clear()
        self.date_time.clear()
        self.payment_id.clear()
        self.warehouse_transaction_id.clear()
        self.tax.clear()
        self.total_discount.clear()
        self.total_amount.clear()
        self.order_type.set("Basket")
        status, order_list = self.order_controller.find_all()
        self.table.refresh_table(order_list)

    def select_from_table(self, selected_order):
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

    def order_item_view(self):
        ui = OrderItemView()