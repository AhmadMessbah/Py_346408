from view import *

from model.entity.product import Product
from controller.product_controller import ProductController

class ProductView:
    def __init__(self):
        self.product_controller = ProductController()
        self.window = Tk()
        self.window.geometry("1000x440")
        self.window.title("product")

        self.id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.name = LabelWithEntry(self.window, "Name", 20, 60)
        self.brand = LabelWithEntry(self.window, "Brand", 20, 100)
        self.model = LabelWithEntry(self.window, "Model", 20, 140, data_type=IntVar)
        self.serial = LabelWithEntry(self.window, "Serial", 20, 180)
        self.category = LabelWithEntry(self.window, "Category", 20, 220)
        self.unit = LabelWithEntry(self.window, "Unit", 20, 260)
        self.expirationdate = LabelWithEntry(self.window, "ExpirationDate", 20, 300)

        self.table = ttk.Treeview(self.window, columns=[1, 2, 3, 4, 5, 6, 7, 8], show="headings", height=18)
        self.table.place(x=270, y=20)

        self.table.heading(1, text="Id")
        self.table.heading(2, text="Name")
        self.table.heading(3, text="Brand")
        self.table.heading(4, text="Model")
        self.table.heading(5, text="Serial")
        self.table.heading(6, text="Category")
        self.table.heading(7, text="Unit")
        self.table.heading(8, text="ExpirationDate")

        self.table.column(1, width=40)
        self.table.column(2, width=100)
        self.table.column(3, width=100)
        self.table.column(4, width=60)
        self.table.column(5, width=100)
        self.table.column(6, width=100)
        self.table.column(7, width=100)
        self.table.column(8, width=100)

        self.table.bind("<<TreeviewSelect>>", self.select_from_table)

        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=380)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=100, y=380)
        Button(self.window, text="Delete", width=7,command=self.delete_click).place(x=180, y=380)
        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = self.product_controller.save(self.name.get(), self.brand.get(), self.model.get(), self.category.get(),
                                                       self.serial.get(),self.unit.get(),self.expirationdate.get())
        if status:
            messagebox.showinfo("Product Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Product Save Error", message)

    def edit_click(self):
        status, message = self.product_controller.update( self.id.get(), self.name.get(), self.brand.get(),self.model.get(),
                                                          self.category.get(),self.serial.get(),self.unit.get(),self.expirationdate.get())
        if status:
            messagebox.showinfo("Product Update", message)
            self.reset_form()
        else:
            messagebox.showerror("Product Update Error", message)

    def delete_click(self):
        status, message = self.product_controller.delete(self.id.get())
        if status:
            messagebox.showinfo("Product Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("Product Delete Error", message)

    def reset_form(self):
        self.id.clear()
        self.name.clear()
        self.brand.clear()
        self.model.clear()
        self.category.clear()
        self.serial.clear()
        self.unit.clear()
        self.expirationdate.clear()
        status, product_list = self.product_controller.find_all()
        self.refresh_table(product_list)

    def refresh_table(self, product_list):
        for item in self.table.get_children():
            self.table.delete(item)

        for product in product_list:
            product_tuple = tuple(product.__dict__.values())
            self.table.insert("", END, values=product_tuple)

    def select_from_table(self, event):
        selected_product = self.table.item(self.table.focus())["values"]
        if selected_product:
            product = Product(*selected_product)
            self.id.set(product.id)
            self.name.set(product.name)
            self.brand.set(product.brand)
            self.model.set(product.model)
            self.category.set(product.category)
            self.unit.set(product.unit)
            self.serial.set(product.serial)
            self.expirationdate.set(product.expiration_date)