from tkinter import *
from PIL import ImageTk, Image
from model import Session
from view.customer_view import CustomerView
from view.employee_view import EmployeeView
from view.book_view import BookView


class DashboardView:
    def employee_view(self):
        ui = EmployeeView()

    def customer_view(self):
        ui = CustomerView()

    def book_view(self):
        ui = BookView()


    def __init__(self):
        self.employee = Session.employee
        font = ("Arial", 18, "bold")
        width = 24
        background_color = "violet red"
        foreground_color = "white"

        y_dist = 60

        self.window = Tk()
        self.window.geometry("540x400")
        self.window.title("Dashboard")
        self.window.config(bg="white")

        image = Image.open("./view/images/img.png")
        image = ImageTk.PhotoImage(image)

        Label(self.window, image=image).place(x=195, y=15)

        Button(self.window, font=font, width=width, bg=background_color, fg=foreground_color, text="Employee",
               command=self.employee_view).place(x=80, y=180)
        Button(self.window, font=font, width=width, bg=background_color, fg=foreground_color, text="Customer",
               command=self.customer_view).place(x=80, y=180 + y_dist * 1)
        Button(self.window, font=font, width=width, bg=background_color, fg=foreground_color, text="Book",
               command=self.book_view).place(x=80, y=180 + y_dist * 2)

        employee_name = self.employee.username if self.employee else "Not Logged In"
        Label(self.window, text=f"Employee : {employee_name}", font=font, bg="white").place(x=80, y=850)

        self.window.mainloop()




