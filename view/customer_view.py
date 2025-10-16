from view import *

from model.entity.customer import Customer
from controller.customer_controller import CustomerController

class CustomerView:
    def __init__(self):
        self.customer_controller = CustomerController()
        self.window = Tk()
        self.window.geometry("740x320")
        self.window.title("Customer")

        self.id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.first_name = LabelWithEntry(self.window, "FirstName", 20, 60)
        self.last_name = LabelWithEntry(self.window, "LastName", 20, 100)
        self.phone_number = LabelWithEntry(self.window, "PhoneNumber", 20, 140, data_type=IntVar)
        self.address = LabelWithEntry(self.window, "Address", 20, 180)

        self.table = ttk.Treeview(self.window, columns=[1, 2, 3, 4, 5], show="headings", height=12)
        self.table.place(x=270, y=20)

        self.table.heading(1, text="Id")
        self.table.heading(2, text="FirstName")
        self.table.heading(3, text="LastName")
        self.table.heading(4, text="PhoneNumber")
        self.table.heading(5, text="Address")

        self.table.column(1, width=40)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=100)

        self.table.bind("<<TreeviewSelect>>", self.select_from_table)

        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=260)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=260)
        Button(self.window, text="Delete", width=7,command=self.delete_click).place(x=180, y=260)
        self.reset_form()
        self.window.mainloop()


    def save_click(self):
        status, message = self.customer_controller.save(self.first_name.get(), self.last_name.get(), self.phone_number.get(), self.address.get())
        if status:
            messagebox.showinfo("Customer Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Customer Save Error", message)


    def edit_click(self):
        status, message = self.customer_controller.update( self.id.get(), self.first_name.get(), self.last_name.get(),
                                                        self.phone_number.get(), self.address.get())
        if status:
            messagebox.showinfo("Customer Update", message)
            self.reset_form()
        else:
            messagebox.showerror("Customer Update Error", message)

    def delete_click(self):
        status, message = self.customer_controller.delete(self.id.get())
        if status:
            messagebox.showinfo("Customer Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("Customer Delete Error", message)


    def reset_form(self):
        self.id.clear()
        self.first_name.clear()
        self.last_name.clear()
        self.phone_number.clear()
        self.address.clear()
        status, customer_list = self.customer_controller.find_all()
        self.refresh_table(customer_list)

    def refresh_table(self, customer_list):
        for item in self.table.get_children():
            self.table.delete(item)

        for customer in customer_list:
            customer_tuple = tuple(customer.__dict__.values())
            self.table.insert("", END, values=customer_tuple)

    def select_from_table(self, event):
        selected_customer = self.table.item(self.table.focus())["values"]
        if selected_customer:
            customer = Customer(*selected_customer)
            self.id.set(customer.id)
            self.first_name.set(customer.first_name)
            self.last_name.set(customer.last_name)
            self.phone_number.set(customer.phone_number)
            self.address.set(customer.address)

