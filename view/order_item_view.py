from view import *

from model import OrderItem
from controller import OrderItemController

class OrderItemView:
    def __init__(self):
        self.window = Tk()
        self.window.title("Order Item")
        self.window.geometry("900x380")

        self.id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.order_id = LabelWithEntry(self.window, "Order Item", 20, 60, data_type=IntVar)
        self.product_id = LabelWithEntry(self.window, "Product Id", 20, 100, data_type=IntVar)
        self.quantity = LabelWithEntry(self.window, "Quantity", 20, 140, data_type=IntVar)
        self.price = LabelWithEntry(self.window, "Price", 20, 180, data_type=IntVar)
        self.discount = LabelWithEntry(self.window, "Discount", 20, 220, data_type=IntVar)
        self.description = LabelWithEntry(self.window, "Description", 20, 260)

        self.table = Table(self.window,
                           ["Id", "Order Id", "Product", "Quantity", "Price", "Discount", "Description"],
                           [40, 60, 120, 60, 90, 60, 140]
                           , 300 ,20 ,
                           14 ,
                           self.select_from_table
                           )

        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=300)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=97, y=300)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=175, y=300)

        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = OrderItemController.save(self.order_id.get(), self.product_id.get(), self.quantity.get(),
                                                          self.price.get(), self.discount.get(), self.description.get())
        if status:
            messagebox.showinfo("Order Item Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Order Item Save Error", message)

    def edit_click(self):
        status, message = OrderItemController.update(self.id.get(),self.order_id.get(), self.product_id.get(), self.quantity.get(),
                                                          self.price.get(), self.discount.get(), self.description.get())
        if status:
            messagebox.showinfo("Order Item Update", message)
            self.reset_form()
        else:
            messagebox.showerror("Order Item Update Error", message)

    def delete_click(self):
        status, message = OrderItemController.delete(self.id.get())
        if status:
            messagebox.showinfo("Order Item Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("Order Item Delete Error", message)

    def reset_form(self):
       self.id.clear()
       self.order_id.clear()
       self.product_id.clear()
       self.quantity.clear()
       self.price.clear()
       self.discount.clear()
       self.description.clear()
       status, order_item_list = OrderItemController.find_all()
       self.table.refresh_table(order_item_list)

    def select_from_table(self, selected_order_item):
        if selected_order_item:
            status , order_item = OrderItemController.find_by_id(selected_order_item[0])
            if status:
                order_item = OrderItem(*selected_order_item)
                self.id.set(order_item.id)
                self.order_id.set(order_item.order_id)
                self.product_id.set(order_item.product_id)
                self.quantity.set(order_item.quantity)
                self.price.set(order_item.price)
                self.discount.set(order_item.discount)
                self.description.set(order_item.description)
