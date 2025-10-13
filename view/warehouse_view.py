from tkinter import *

root = Tk()
root.title("Warehouse View")
root.geometry("300x250")


def edit():
    win = Tk()
    win.title("Edit")
    win.geometry("200x200")
    l = Label(win, text="enter product id")
    l.pack()
    entry = Entry(win)
    entry.pack()
    sub = Button(win, text="submit")
    sub.pack()

def add():
    win = Tk()
    win.title("Add")
    win.geometry("200x200")
    l = Label(win, text="enter product id")
    l.pack()
    entry = Entry(win)
    entry.pack()
    l = Label(win, text="enter product name")
    l.pack()
    entry = Entry(win)
    entry.pack()
    l = Label(win, text="enter product type")
    l.pack()
    entry = Entry(win)
    entry.pack()
    sub = Button(win, text="submit")
    sub.pack()


def find():
    win = Tk()
    win.title("Find")
    win.geometry("200x200")
    l = Label(win, text="enter product id")
    l.pack()
    entry = Entry(win)
    entry.pack()
    sub = Button(win, text="submit")
    sub.pack()



# ADD-SECTION
add_label = Label(root, text="Add product to warehouse")
add_label.pack()
add_btn = Button(root, text="Add product", bg="red", command=add)
add_btn.pack(pady=5)

# EDIT-SECTION
edit_label = Label(root, text="Edit product in warehouse")
edit_label.pack(pady=10)
edit_btn = Button(root, text="Edit product", bg="yellow", command=edit)
edit_btn.pack(pady=5)

# FIND-SECTION
find_label = Label(root, text="Find product in warehouse")
find_label.pack(pady=10)
find_btn = Button(root, text="Find product", bg="green", command=find)
find_btn.pack(pady=5)

root.mainloop()