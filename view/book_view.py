from view import *

from model import Book
from controller import BookController


class BookView:
    def __init__(self):

        self.window = Tk()
        self.window.title("Book")
        self.window.geometry("1360x585")

        self.book_id = LabelWithEntry(self.window, "Id", 20, 20, data_type=IntVar, state="readonly")
        self.title = LabelWithEntry(self.window, "Title", 20, 60)
        self.customer_id = LabelWithEntry(self.window, "Customer Id", 20, 100, data_type=IntVar)
        self.employee_id = LabelWithEntry(self.window, "Employee Id", 20, 140, data_type=IntVar)
        self.year = LabelWithEntry(self.window, "Year", 20, 180)
        self.payment = LabelWithEntry(self.window, "Payment", 20, 220, data_type=IntVar)
        self.publisher = LabelWithEntry(self.window, "Publisher", 20, 260)
        self.isbn = LabelWithEntry(self.window, "Isbn", 20, 300, data_type=IntVar)
        self.tax = LabelWithEntry(self.window, "Tax", 20, 380, data_type=IntVar)
        self.total_discount = LabelWithEntry(self.window, "Total Discount", 20, 420, data_type=IntVar)
        self.total_amount = LabelWithEntry(self.window, "Total Amount", 20, 460, data_type=IntVar)






        book_state_list = ["Borrow", "Sell", "Buy", "Not Given"]
        type_book = StringVar(value="Sell")
        Label(self.window, text="Status Type").place(x=20, y=340)
        self.status = Combobox(
            self.window,
            values=book_state_list,
            textvariable=type_book,
            width=17,
            state="readonly")
        self.status.place(x=110, y=340)

        self.search_customer_id = LabelWithEntry(self.window, "Customer Id", 280, 20, data_type=IntVar, distance=75,
                                                 on_keypress_function=self.search_by_customer_id)
        self.search_employee_id = LabelWithEntry(self.window, "Employee Id", 500, 20, data_type=IntVar, distance=75,
                                                 on_keypress_function=self.search_by_employee_id)
        self.search_title = LabelWithEntry(self.window, "Title", 720, 20, distance=55,
                                                 on_keypress_function=self.search_by_title)

        self.table = Table(
            self.window,
            ["Id", "Title", "Customer", "Employee", "Year", "Payment", "Publisher", "ISBN", "Status", "Tax", "Total Discount", "Total Amount"],
            [40, 90, 100, 100, 40, 90, 100, 100, 90, 50, 90, 90],
            260, 60,
            23,
            self.select_from_table
        )

        Button(self.window, text="Save", width=7, command=self.save_click).place(x=20, y=540)
        Button(self.window, text="Edit", width=7, command=self.edit_click).place(x=97, y=540)
        Button(self.window, text="Delete", width=7, command=self.delete_click).place(x=175, y=540)
        Button(self.window, text="View Book", width=29, command=self.book_item_view).place(x=20, y=500)

        self.reset_form()
        self.window.mainloop()

    def save_click(self):
        status, message = BookController.save(self.title.get(), self.customer_id.get(), self.employee_id.get(),
                                                     self.year.get(), self.payment.get(),
                                                     self.publisher.get(), self.isbn.get(),
                                                     self.status.get(), self.tax.get(),
                                                     self.total_discount.get(), self.total_amount.get())
        if status:
            messagebox.showinfo("Book Save", message)
            self.reset_form()
        else:
            messagebox.showerror("Book Save Error", message)

    def edit_click(self):
        status, message = BookController.update(self.book_id.get(), self.title.get(), self.customer_id.get(), self.employee_id.get(),
                                               self.year.get(), self.payment.get(), self.publisher.get(),
                                               self.isbn.get(), self.status.get(), self.tax.get(),
                                               self.total_discount.get(), self.total_amount.get())
        if status:
            messagebox.showinfo("Book Update", message)
            self.reset_form()
        else:
            messagebox.showerror("Book Update Error", message)

    def delete_click(self):
        status, message = BookController.delete(self.book_id.get())
        if status:
            messagebox.showinfo("Book Delete", message)
            self.reset_form()
        else:
            messagebox.showerror("Book Delete Error", message)

    def book_item_view(self):
        pass
        #ui = ShowBookiew()

    def reset_form(self):
        self.book_id.clear()
        self.title.clear()
        self.customer_id.clear()
        self.employee_id.clear()
        self.year.clear()
        self.payment.clear()
        self.publisher.clear()
        self.isbn.clear()
        self.status.set("Sell")
        self.tax.clear()
        self.total_discount.clear()
        self.total_amount.clear()
        status, book_list = BookController.find_all()
        self.table.refresh_table(book_list)

    def select_from_table(self, selected_book):
        if selected_book:
            status, book = BookController.find_by_id(selected_book[0])
            if status:
                self.book_id.set(book.book_id)
                self.title.set(book.title)
                self.customer_id.set(book.customer_id)
                self.employee_id.set(book.employee_id)
                self.year.set(book.year)
                self.payment.set(book.payment)
                self.publisher.set(book.publisher)
                self.isbn.set(book.isbn)
                self.status.set(book.status)
                self.tax.set(book.tax)
                self.total_discount.set(book.total_discount)
                self.total_amount.set(book.total_amount)
    def search_by_title(self):
        status, book_list = BookController.find_by_title(self.search_title.get())
        if status and book_list:
            self.table.refresh_table(book_list)
        else:
            self.reset_form()

    def search_by_customer_id(self):
        status, book_list = BookController.find_by_customer_id(self.search_customer_id.get())
        if status and book_list:
            self.table.refresh_table(book_list)
        else:
            self.reset_form()

    def search_by_employee_id(self):
        status, book_list = BookController.find_by_employee_id(self.search_employee_id.get())
        if status and book_list:
            self.table.refresh_table(book_list)
        else:
            self.reset_form()






