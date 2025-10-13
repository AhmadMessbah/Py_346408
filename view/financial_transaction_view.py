from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from view.bank_view import window



window = Tk()
window.title("Financial Transaction")
window.geometry("500x450")

#  فیلدها
Label(window, text="ID:").place(x=20, y=20)
id_entry = Entry(window, width=40)
id_entry.place(x=150, y=20)

Label(window, text="Transaction Type:").place(x=20, y=60)
transaction_type_combo = ttk.Combobox(window, values=["Income", "Outgoing"], state="readonly", width=37)
transaction_type_combo.place(x=150, y=60)
transaction_type_combo.set("Income")

Label(window, text="Customer ID:").place(x=20, y=100)
customer_id_entry = Entry(window, width=40)
customer_id_entry.place(x=150, y=100)

Label(window, text="Employee ID:").place(x=20, y=140)
employee_id_entry = Entry(window, width=40)
employee_id_entry.place(x=150, y=140)

Label(window, text="Amount:").place(x=20, y=180)
amount_entry = Entry(window, width=40)
amount_entry.place(x=150, y=180)

Label(window, text="Date & Time:").place(x=20, y=220)
date_time_entry = Entry(window, width=40)
date_time_entry.place(x=150, y=220)

Label(window, text="Payment ID:").place(x=20, y=260)
payment_id_entry = Entry(window, width=40)
payment_id_entry.place(x=150, y=260)

Label(window, text="Description:").place(x=20, y=300)
description_entry = Entry(window, width=40)
description_entry.place(x=150, y=300)

#  دکمه‌ها
Button(window, text="Save", width=12).place(x=50, y=350)
Button(window, text="Delete", width=12).place(x=350, y=350)  # فعلاً بدون عملکرد

window.mainloop()
