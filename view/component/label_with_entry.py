from tkinter import *

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

