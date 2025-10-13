from tkinter import ttk

# todo *** not used !!!!

class Table:
    def __init__(self, parent):
        self.table = ttk.Treeview(parent, columns=[1, 2, 3, 4, 5, 6, 7], show="headings")
        self.table.place(x=300,y=20)
        self.set_column_headings()
        self.set_column_widths()

    def set_column_headings(self):
        headings = ["ID", "Order ID", "Product ID", "Quantity", "Price", "Discount", "Description"]
        for i, heading in enumerate(headings):
            self.table.heading(i, text=heading)

    def set_column_widths(self):
        widths = [40, 60, 70, 60, 90, 60, 140]
        for i, width in enumerate(widths):
            self.table.column(i, width=width)
