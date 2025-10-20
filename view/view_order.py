from tkinter import *
from view.component.table import Table
from view.component.lable_with_entry import LabelWithEntry
from controller.order_item_controller import OrderItemController


class ViewOrder:
    def __init__(self):

        self.order_item_controller = OrderItemController()

        self.window = Tk()
        self.window.title("Order View")
        self.window.geometry("900x150")

        self.customer_id = LabelWithEntry(self.window, "Customer", 20, 20, data_type=IntVar)
        self.order_id = LabelWithEntry(self.window, "Order Id", 20, 65, data_type=IntVar)
        self.date_time = LabelWithEntry(self.window, "Date & Time", 20, 105)

        self.table = Table(self.window,
                           ["Id", "Order Id", "Product", "Quantity", "Price", "Discount", "Description"],
                           [40, 60, 120, 60, 90, 60, 140]
                           , 300, 20,
                           4)

        self.reset_form()
        self.window.mainloop()

    def reset_form(self):
        self.customer_id.clear()
        self.order_id.clear()
        status, order_item_list = self.order_item_controller.find_by_order_id(self.order_id)
        self.table.refresh_table(order_item_list)


