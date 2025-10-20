from view import *

from model import Delivery
from controller import DeliveryController

class DeliveryView:
    def __init__(self):
        self.delivery_controller = DeliveryController()
        self.window = Tk()
        self.window.geometry("740x320")
        self.window.title("Delivery")

        self.id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.first_name = LabelWithEntry(self.window, "FirstName", 20, 60)
        self.last_name = LabelWithEntry(self.window, "LastName", 20, 100)
        self.address = LabelWithEntry(self.window, "Address", 20, 140)
        self.description = LabelWithEntry(self.window, "Description", 20, 180)

        self.table = ttk.Treeview(self.window, columns=[1, 2, 3, 4, 5], show="headings", height=12)
        self.table.place(x=270, y=20)

        self.table.heading(1, text="Id")
        self.table.heading(2, text="FirstName")
        self.table.heading(3, text="LastName")
        self.table.heading(4, text="Address")
        self.table.heading(5, text="Description")

        self.table.column(1, width=40)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)

        self.table.bind("<<TreeviewSelect>>", self.select_from_table)

        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=260)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=260)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=180, y=260)
        self.reset_form()
        self.window.mainloop()


    def save_click(self):
        status, message = self.delivery_controller.save(self.first_name.get(), self.last_name.get(), self.address.get(), self.description.get())
        if status:
            messagebox.showinfo("Delivery Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Delivery Save Error", message)


    def edit_click(self):
        status, message = self.delivery_controller.update( self.id.get(), self.first_name.get(), self.last_name.get(),
                                                        self.address.get(), self.description.get())
        if status:
            messagebox.showinfo("Delivery Update", message)
            self.reset_form()
        else:
            messagebox.showerror("Delivery Update Error", message)

    def delete_click(self):
        status, message = self.delivery_controller.delete(self.id.get())
        if status:
            messagebox.showinfo("Delivery Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("Delivery Delete Error", message)


    def reset_form(self):
        self.id.clear()
        self.first_name.clear()
        self.last_name.clear()
        self.address.clear()
        self.description.clear()
        status, delivery_list = self.delivery_controller.find_all()
        self.refresh_table(delivery_list)

    def refresh_table(self, delivery_list):
        for item in self.table.get_children():
            self.table.delete(item)

        for delivery in delivery_list:
            delivery_tuple = tuple(delivery.__dict__.values())
            self.table.insert("", END, values=delivery_tuple)

    def select_from_table(self, event):
        selected_delivery = self.table.item(self.table.focus())["values"]
        if selected_delivery:
            delivery = Delivery(*selected_delivery)
            self.id.set(delivery.id)
            self.first_name.set(delivery.first_name)
            self.last_name.set(delivery.last_name)
            self.address.set(delivery.address)
            self.description.set(delivery.description)

