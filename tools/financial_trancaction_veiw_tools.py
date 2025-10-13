from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from model.repository.financial_transaction_repository import FinancialTransactionRepository

class TrancactionGui:
    def __init__(self):
        self.window = Tk()
        self.window.title("Financial Transaction")
        self.window.geometry("500x450")
        self.window.configure("sky blue")
        self.finacial_trancaction_repository = FinancialTransactionRepository()
def to_tuple(self):
    return tuple(self.id,self.transaction_type, self.customer_id , self.employee_id,self. amount, self.date_time,self.payment_id,self.description)


def reset_form(id,transaction_type, customer_id , employee_id, amount, date_time,payment_id,description):
    id.clear()
    transaction_type.clear()
    customer_id.clear()
    employee_id.clean()
    amount.clear()
    date_time.clear()
    payment_id.clear()
    description.clear()


def save_click(id,transaction_type, customer_id , employee_id, amount, date_time,payment_id,description):
    try:

        financial_transaction = (id.get(), transaction_type.get(), customer_id.get(),  employee_id.get(), amount.get(), date_time.get(), payment_id.get(),description.get())

        table.insert(
            "",
            END,
            values=financial_transaction
        )

        messagebox.showinfo("Save", "Trancaction has been saved")
        reset_form()
    except Exception as e:
        messagebox.showerror("Error", f"{e}")
class LabelWithEntry:
    def __init__(self, master, label_text, x, y, distance_1=130, ,data_type=IntVar):
        self.data_type = data_type
        self.variable = data_type()
        Label(master, text=label_text, fg="navy",width=40,font=("Arial", 16)).place(x=x, y=y)
        Entry(master, textvariable=self.variable,width=40 ,fg="navy",font=("Arial", 16)).place(x=x + distance_1, y=y)

    def get(self):
        return self.variable.get()


    def clear(self):
        if self.data_type == StringVar:
            self.variable.set("")
        elif self.data_type==IntVar:
            self.variable.set(0)
        else:
            raise ValueError("Invalid Type")


