from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg


win=Tk()
win.title("Employee")
win.geometry("1000x1000")
win.configure(bg="#FFF8F0")

#functions

def save():
    employee=(id.get(),first_name.get(),last_name.get(),salary.get(),occupation.get(),phone_number.get(),username.get(),password.get())
    table.insert("",END,values=employee)
    msg.showinfo("saved","employee saved")
    reset_form()
def update():
    employee=(id.set(id.get()),first_name.set(first_name.get()),last_name.set(last_name.get()),salary.set(salary.get()),occupation.set(occupation.get()),phone_number.set(phone_number.get()),username.set(username.get()),password.set(password.get()))
    table.insert("",END,values=employee)
    reset_form()
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
  
    
#class 
class LabelwithEntry:
    def __init__(self,master,label_text,color,x,y,data_type=StringVar,distance=110,height_difference=0):
        Label(master,text=label_text,bg=(color)).place(x=x,y=y)
        self.variable=data_type()
        Entry(master,textvariable=self.variable).place(x=x+distance,y=y+height_difference)
    
    def get(self):
        return self.variable.get()
    
    def set(self,value):
        return self.variable.set(value)
    

Label(win,text="Employee Management System",bg=("#F18284"),font=("Arial",18,"italic")).place(x=400,y=20)

#id
id=LabelwithEntry(win,"id:","#FFFFFF",10,100,IntVar,100)
#first_name
first_name=LabelwithEntry(win,"first_name:","#FFFFFF",10,130,StringVar,100)
#last_name
last_name=LabelwithEntry(win,"last_name:","#FFFFFF",10,160,StringVar,100)
#salary
salary=LabelwithEntry(win,"salary:","#FFFFFF",10,190,IntVar,100)
#occupation
occupation=LabelwithEntry(win,"occupation:","#FFFFFF",10,220,StringVar,100)
#phone_number

phone_number=LabelwithEntry(win,"phone_number:","#FFFFFF",10,250,IntVar,100)
#username
username=LabelwithEntry(win,"username:","#FFFFFF",10,280,StringVar,100)
#password
password=LabelwithEntry(win,"password:","#FFFFFF",10,310,StringVar,100)





#Button
Button(win,text="save",bg="#A7C7E7",width=10, command=save).place(x=10,y=350)
Button(win,text="update",bg="#BAFEC4",width=10, command=update).place(x=110,y=350)

id=LabelwithEntry(win,"id:","#FFFFFF",10,430,IntVar,100)

Button(win,text="delete",bg="#FFBAC3",width=10, command=delete).place(x=10,y=470)
Button(win,text="find",bg="#FBF17E",width=10).place(x=110,y=470)

#table
table=ttk.Treeview(win,columns=[1,2,3,4,5,6,7,8],show="headings")
table.place(x=400,y=100)

columns=["id","first_name","last_name","salary","occupation","phone_number","username","expiration_date"]

i=1
for col in columns:
    table.heading(i,text=col)
    table.column(i,width=100)
    i+=1





win.mainloop()