from view import *

from model.entity.warehouse import Warehouse
from controller.warehouse_controller import WarehouseController

class WarehouseView:
    def __init__(self):
        self.warehouse_controller = WarehouseController()
        self.window = Tk()
        self.window.title("Warehouse View")
        self.window.geometry("750x320")

        self.id = LabelWithEntry(self.window,"Id",20,20, data_type=IntVar,state="readonly")
        self.product_id = LabelWithEntry(self.window,"ProductId",20,60)
        self.quantity = LabelWithEntry(self.window,"Quantity",20,100)


        self.table = ttk.Treeview(self.window,columns=[1,2,3],show="headings", height=16)
        self.table.place(x=270,y=20)

        self.table.heading(1, text="Id")
        self.table.heading(2, text="FirstName")
        self.table.heading(3, text="LastName")


        self.table.column(1, width=40)
        self.table.column(2, width=100)
        self.table.column(3, width=100)


        self.table.bind("<<TreeviewSelect>>", self.select_from_table)

        Button(self.window, text="Save", width=8, command=self.save_click).place(x=20, y=340)
        Button(self.window, text="Edit", width=8, command=self.save_click).place(x=100, y=340)
        Button(self.window, text="Delete", width=8, command=self.save_click).place(x=180, y=340)
        self.reset_form()
        self.window.mainloop()


    def save_click(self):
        status, message = self.warehouse_controller.save(self.product_id.get(), self.quantity.get())
        if status:
            messagebox.showinfo("Warehouse Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Warehouse Save Error", message)


    def edit_click(self):
        status, message = self.warehouse_controller.update(self.id.get(), self.product_id.get(), self.quantity.get())
        if status:
            messagebox.showinfo("Warehouse update", message)
            self.reset_form()
        else:
            messagebox.showerror("Warehouse update Error", message)

    def delete_click(self):
        status, message = self.warehouse_controller.delete(self.id.get())
        if status:
            messagebox.showinfo("Warehouse Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("Warehouse Delete Error", message)

    def reset_form(self):
        self.id.clear()
        self.product_id.clear()
        self.quantity.clear()

        status, warehouse_list = self.warehouse_controller.find_all()
        self.refresh_table(warehouse_list)

    def refresh_table(self, warehouse_list):
        for item in self.table.get_children():
            self.table.delete(item)

        for warehouse in warehouse_list:
            warehouse_tuple = tuple(warehouse.__dict__.values())
            self.table.insert("", END, values=warehouse_tuple)

    def select_from_table(self, event):
        selected_warehouse = self.table.item(self.table.focus())["values"]
        if selected_warehouse:
            warehouse = Warehouse(*selected_warehouse)
            self.id.set(warehouse.id)
            self.product_id.set(warehouse.product_id)
            self.quantity.set(warehouse.quantity)









