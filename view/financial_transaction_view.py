from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tools.financial_trancaction_veiw_tools import *

#  توابع
def save_click():
    messagebox.showinfo("Save", "Transaction  saved")
#  پنجره
win = Tk()
win.title("Financial Transaction")
win.geometry("500x450")

#  فیلدها
Label(win, text="ID:").place(x=20, y=20)
id_entry = Entry(win, width=40)
id_entry.place(x=150, y=20)

Label(win, text="Transaction Type:").place(x=20, y=60)
transaction_type_combo = ttk.Combobox(win, values=["Income", "Outgoing"], state="readonly", width=37)
transaction_type_combo.place(x=150, y=60)
transaction_type_combo.set("Income")

Label(win, text="Customer ID:").place(x=20, y=100)
customer_id_entry = Entry(win, width=40)
customer_id_entry.place(x=150, y=100)

Label(win, text="Employee ID:").place(x=20, y=140)
employee_id_entry = Entry(win, width=40)
employee_id_entry.place(x=150, y=140)

Label(win, text="Amount:").place(x=20, y=180)
amount_entry = Entry(win, width=40)
amount_entry.place(x=150, y=180)

Label(win, text="Date & Time:").place(x=20, y=220)
date_time_entry = Entry(win, width=40)
date_time_entry.place(x=150, y=220)

Label(win, text="Payment ID:").place(x=20, y=260)
payment_id_entry = Entry(win, width=40)
payment_id_entry.place(x=150, y=260)

Label(win, text="Description:").place(x=20, y=300)
description_entry = Entry(win, width=40)
description_entry.place(x=150, y=300)

#  دکمه‌ها
Button(win, text="Save", width=12, command=save_click).place(x=50, y=350)

Button(win, text="Delete", width=12).place(x=350, y=350)  # فعلاً بدون عملکرد

win.mainloop()
