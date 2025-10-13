from tkinter.ttk import Treeview


class HeadingWithWidth:
    def __init__(self, table, column_id, label_text, width=60):
        Treeview.heading(table, column=column_id, text=label_text)
        Treeview.column(table, column=column_id, width=width)
