import tkinter as tk
from tkinter import messagebox
from model.entity.warehouse import Warehouse
from model.service.warehouse_service import WarehouseService


def open_edit_window():
    # ایجاد پنجره جدید
    edit_window = tk.Toplevel()
    edit_window.title("Edit Product in Warehouse")
    edit_window.geometry("300x220")
    edit_window.resizable(False, False)

    # عنوان
    title_label = tk.Label(edit_window, text="Edit Product in Warehouse", font=("Arial", 12, "bold"))
    title_label.pack(pady=10)

    # ورودی‌ها
    product_id_label = tk.Label(edit_window, text="Product ID:")
    product_id_label.pack()
    product_id_entry = tk.Entry(edit_window, width=25)
    product_id_entry.pack(pady=5)

    quantity_label = tk.Label(edit_window, text="Quantity:")
    quantity_label.pack()
    quantity_entry = tk.Entry(edit_window, width=25)
    quantity_entry.pack(pady=5)

    # تابع دکمه Edit
    def edit_product():
        product_id = product_id_entry.get().strip()
        quantity = quantity_entry.get().strip()

        if not product_id or not quantity:
            messagebox.showwarning("Error", "Please fill in all fields!")
            return

        try:
            product_id = int(product_id)
            quantity = int(quantity)
        except ValueError:
            messagebox.showerror("Error", "Product ID and Quantity must be numbers!")
            return

        # ساخت شیء Warehouse و ارسال به سرویس
        warehouse = Warehouse(None, product_id, quantity)
        warehouse_service = WarehouseService()

        try:
            warehouse_service.update(warehouse)
            messagebox.showinfo("Success", f"Product {product_id} updated successfully!")
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to update product:\n{e}")

    # دکمه Edit
    edit_button = tk.Button(edit_window, text="Edit", command=edit_product, bg="#4CAF50", fg="white", width=10)
    edit_button.pack(pady=10)


# اجرای اصلی
if name == "main":
    root = tk.Tk()
    root.title("Warehouse Manager")
    root.geometry("250x150")

    edit_btn = tk.Button(root, text="Open Edit Window", command=open_edit_window)
    edit_btn.pack(expand=True)

    root.mainloop()

open_edit_window()