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


        self.table = Table(
            self.window,
            ["Id", "first_name", "last_name", "phone_number", "address"],
            [40, 100, 100, 60, 100],
            270, 20,
            12,
            self.select_from_table
        )

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



    def select_from_table(self, event):
        selected_customer = self.table.item(self.table.focus())["values"]
        if selected_customer:
            customer = Customer(*selected_customer)
            self.id.set(customer.id)
            self.first_name.set(customer.first_name)
            self.last_name.set(customer.last_name)
            self.phone_number.set(customer.phone_number)
            self.address.set(customer.address)

