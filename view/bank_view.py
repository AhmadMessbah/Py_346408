from tkinter import *
from model.repository.bank_repository import BankRepository


class BankGui:
    def __init__(self):
        self.window = Tk()
        self.window.title("bank")
        self.window.geometry("400x500")
        self.window.configure("sky blue")
        self.bank_repository = BankRepository()
    
    def get_info(self):

        Label(self.window, "bank name:", fg="navy", font=("Arial", 16)).place(x=50, y=30)
        Entry(self.window, width=30, fg="navy", font=("Arial", 15)).place(x=160, y=60)

        Label(self.window, text="account name:", fg="navy", font=("Arial", 16)).place(x=50, y=100)
        Entry(self.window, width=30, fg="navy", font=("Arial", 15)).place(x=160, y=130)

        Label(self.window, text="balance:", fg="navy", font=("Arial", 16)).place(x=50, y=170)
        Entry(self.window, width=30, fg="navy", font=("Arial", 15),).place(x=160, y=200)

        Label(self.window, text="description:", fg="navy", font=("Arial", 16)).place(x=50, y=240)
        Entry(self.window, width=30, fg="nazy", font=("Arial", 15)).place(x=160, y=270)

        Button(self.window, text="save", command=self.bank_repository.save,
                width=10, fg="navy", font=("Arial", 12)).place(x=100, y=320)
