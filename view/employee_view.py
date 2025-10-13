from tkinter import *
from tkinter import ttk
from tkinter import messagebox


win=Tk()
win.title=("Employee")
win.geometry="1000x1000"
win.configure(bg="lightblue")

def save():
    customer=(id.get(),first_name.get(),last_name.get(),salary.get(),occupation.get(),phone_number.get(),username.get(),password.get())
    table.insert(" ",END,values=customer)
    

def update():
    employee=(id.set(id.get()),first_name.set(first_name.get()),last_name.set(last_name.get()),salary.set(salary.get()),occupation.set(occupation.get()),phone_number.set(phone_number.get()),username.set(username.get()),password.set(password.get()))
    table.insert(" ",END,values=employee)

def delete():
    pass

def reset_form():
  id.set(0) 
  first_name.set(" ") 
  last_name.set(" ") 
  salary.set(0)
  occupation.set(" ")
  phone_number.set(" ")
  username.set(" ")
  password.set(" ")
  
    
    
    
class LabelwithEntry:
    def __init__(self,master,label_text,color,x,y,data_type=StringVar,distance=110,height_difference=0):
        Label(master,text=label_text,bg=(color)).place(x=x,y=y)
        self.variable=data_type()
        Entry(master,textvariable=self.variable).place(x=x+distance,y=y+height_difference)
        
    

Label(win,text="Employee Management System",bg=("DodgerBlue3"),font=("Arial",18,"italic")).place(x=400,y=20)

id=LabelwithEntry(win,"id:","DodgerBlue3",10,100,IntVar,100)

first_name=LabelwithEntry(win,"first_name:","DodgerBlue3",10,130,StringVar,100)

last_name=LabelwithEntry(win,"last_name:","DodgerBlue3",10,160,StringVar,100)

salary=LabelwithEntry(win,"salary:","DodgerBlue3",10,190,IntVar,100)

occupation=LabelwithEntry(win,"occupation:","DodgerBlue3",10,220,StringVar,100)

phone_number=LabelwithEntry(win,"phone_number:","DodgerBlue3",10,250,IntVar,100)

username=LabelwithEntry(win,"username:","DodgerBlue3",10,280,StringVar,100)

password=LabelwithEntry(win,"password:","DodgerBlue3",10,310,StringVar,100)

Button(win,text="save",bg="DodgerBlue2",width=10, command=save).place(x=10,y=350)
Button(win,text="update",bg="DodgerBlue2",width=10, command=update).place(x=110,y=350)



id=LabelwithEntry(win,"id:","DodgerBlue3",10,430,IntVar,100)

Button(win,text="delete",bg="DodgerBlue2",width=10, command=delete).place(x=10,y=470)
Button(win,text="find",bg="DodgerBlue2",width=10).place(x=110,y=470)

#table
table=ttk.Treeview(win,columns=[1,2,3,4,5,6,7,8],show="headings")
table.place(x=400,y=100)

table.heading(1, text="id")
table.heading(2, text="first_name")
table.heading(3, text="last_name")
table.heading(4, text="salary")
table.heading(5, text="occupation")
table.heading(6, text="phone_number")
table.heading(7, text="username")
table.heading(8, text="password")


table.column(1,width=100)
table.column(2,width=100)
table.column(3,width=100)
table.column(4,width=100)
table.column(5,width=100)
table.column(6,width=100)
table.column(7,width=100)
table.column(8,width=100)






win.mainloop()