'''from controller.payment_controller import PaymentController

name = input("Enter name : ")
description = input("Enter description : ")
 
payment_controller = PaymentController()
payment_controller.save(name, description)
'''
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox as msg


win=Tk()
win.title=("Payment")
win.geometry="1000x1000"
win.configure(bg="lightblue")

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
    
        
def save():
    
    payment=(id.get(),transaction_type.get(),payment_type.get(),date_time.get(),customer_id.get())
    table.insert("",END,values=payment)
    
    msg.showinfo("saved","payment saved")
    reset_form()

def update():
    payment=(id.set(id.get()),transaction_type.set(transaction_type.get()),payment_type.set(payment_type.get()),date_time.set(date_time.get()),customer_id.set(customer_id.get()))
    table.insert("",END,values=payment)   
    reset_form()
def delete():
    pass

def reset_form():
  id.set(0) 
  transaction_type.set(" ") 
  payment_type.set(" ") 
  date_time.set(" ")
  customer_id.set(" ")
  
  
    

Label(win,text="Payment Management System",bg=("DodgerBlue3"),font=("Arial",18,"italic")).place(x=400,y=20)

id=LabelwithEntry(win,"id:","DodgerBlue3",10,100,IntVar,100)
id.set("")
transaction_type=StringVar()
Label(win,text="transaction_type",bg='DodgerBlue3').place(x=10,y=130)
Radiobutton(win,text="payment",variable=transaction_type,value="payment",bg="lightblue").place(x=110,y=130)
Radiobutton(win,text="reception",variable=transaction_type,value="reception",bg="lightblue",font=('Arial',10)).place(x=180,y=130)


payment_type=StringVar()
Label(win,text="payment_type",bg='DodgerBlue3').place(x=10,y=160)
ttk.Combobox(win,values=["debit card","check","cash","credit"],width=17,textvariable="payment_type",state="readonly").place(x=110,y=160)


date_time=StringVar()
date_time=LabelwithEntry(win,"date_time:","DodgerBlue3",10,190,StringVar,100)

customer_id=StringVar()
customer_id=LabelwithEntry(win,"customer_id:","DodgerBlue3",10,220,StringVar,100)



Button(win,text="save",bg="DodgerBlue2",width=10).place(x=10,y=250)

Button(win,text="update",bg="DodgerBlue2",width=10).place(x=110,y=250)



id=LabelwithEntry(win,"id:","DodgerBlue3",10,330,IntVar,100)

Button(win,text="delete",bg="DodgerBlue2",width=10).place(x=10,y=370)
Button(win,text="find",bg="DodgerBlue2",width=10).place(x=110,y=370)

#table
table=ttk.Treeview(win,columns=[1,2,3,4,5],show="headings")
table.place(x=400,y=100)



columns=["id","transaction_type","payment_type","date_time","customer_id"]

i=1
for col in columns:
    table.heading(i,text=col)
    table.column(i,width=100)
    i+=1

win.mainloop()
