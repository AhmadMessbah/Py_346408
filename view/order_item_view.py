from view import *

from model.entity.order_item import OrderItem
from controller.order_item_controller import OrderItemController

class OrderItemView:
    def __init__(self):

        self.order_item_controller = OrderItemController()

        self.window = Tk()
        self.window.title("Order Item")
        self.window.geometry("850x410")

        self.id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.order_id = LabelWithEntry(self.window, "Order Id", 20, 60, data_type=IntVar)
        self.product_id = LabelWithEntry(self.window, "Product Id", 20, 100, data_type=IntVar)
        self.quantity = LabelWithEntry(self.window, "Quantity", 20, 140, data_type=IntVar)
        self.price = LabelWithEntry(self.window, "Price", 20, 180, data_type=IntVar)
        self.discount = LabelWithEntry(self.window, "Discount", 20, 220, data_type=IntVar)
        self.description = LabelWithEntry(self.window, "Description", 20, 260)
        #self, window, headings, column_widths, x, y, height = 10, function_name = None
        self.table = Table(self.window,["id", "Order Id","Product","Quantity","Price","Discount","Description"],[40,60,120,60,90,60,140]
                           , 300 , 20 , 14 , self.selecct_from_table)

        self.table = ttk.Treeview(self.window, columns=[1, 2, 3, 4, 5, 6, 7], show="headings", height=14)
        self.table.place(x=300, y=20)
        #
        # self.table.heading(1, text="Id")
        # self.table.heading(2, text="Order Id")
        # self.table.heading(3, text="Product")
        # self.table.heading(4, text="Quantity")
        # self.table.heading(5, text="Price")
        # self.table.heading(6, text="Discount")
        # self.table.heading(7, text="Description")
        #
        # self.table.column(1, width=40)
        # self.table.column(2, width=60)
        # self.table.column(3, width=120)
        # self.table.column(4, width=60)
        # self.table.column(5, width=90)
        # self.table.column(6, width=60)
        # self.table.column(7, width=140)

        # self.table.bind("<<TreeviewSelect>>", self.select_from_table)

        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=300)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=97, y=300)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=175, y=300)

        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = self.order_item_controller.save(self.order_id.get(), self.product_id.get(), self.quantity.get(),
                                                          self.price.get(), self.discount.get(), self.description.get())
        if status:
            messagebox.showinfo("Order Item Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Order Item Save Error", message)

    def edit_click(self):
        status, message = self.order_item_controller.update(self.id.get(),self.order_id.get(), self.product_id.get(), self.quantity.get(),
                                                          self.price.get(), self.discount.get(), self.description.get())
        if status:
            messagebox.showinfo("Order Item Update", message)
            self.reset_form()
        else:
            messagebox.showerror("Order Item Update Error", message)

    def delete_click(self):
        status, message = self.order_item_controller.delete(self.id.get())
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
       status, order_item_list = self.order_item_controller.find_all()
       self.refresh_table(order_item_list)

    def refresh_table(self, order_item_list):
        for item in self.table.get_children():
            self.table.delete(item)

        for order_item in order_item_list:
            order_item_tuple = tuple(order_item.__dict__.values())
            self.table.insert("", END, values=order_item_tuple)

    def select_from_table(self, event):
        selected_order_item = self.table.item(self.table.focus())["values"]
        if selected_order_item:
            order_item = OrderItem(*selected_order_item)
            self.id.set(order_item.id)
            self.order_id.set(order_item.order_id)
            self.product_id.set(order_item.product_id)
            self.quantity.set(order_item.quantity)
            self.price.set(order_item.price)
            self.discount.set(order_item.discount)
            self.description.set(order_item.description)
