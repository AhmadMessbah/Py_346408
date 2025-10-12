from tkinter import *
from tkinter import ttk


class LabelWithEntry:
    def __init__(self, master, label_text, x, y, distance=90, data_type=IntVar):
        self.data_type = data_type
        self.variable = data_type()
        Label(master, text=label_text).place(x=x, y=y)
        Entry(master, textvariable=self.variable).place(x=x + distance, y=y)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)

    def clear(self):
        if self.data_type == IntVar:
            self.variable.set(0)
        elif self.data_type == StringVar:
            self.variable.set("")
        elif self.data_type == DoubleVar:
            self.variable.set(0.0)
        elif self.data_type== BooleanVar:
            self.variable.set(True)

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

