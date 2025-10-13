'''from controller.payment_controller import PaymentController

name = input("Enter name : ")
description = input("Enter description : ")
 
payment_controller = PaymentController()
payment_controller.save(name, description)
'''
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
win=Tk()
win.title=("Payment")
win.geometry="1000x1000"
win.configure(bg="lightblue")


class LabelwithEntry:
    def __init__(self,master,label_text,color,x,y,data_type=StringVar,distance=110,height_difference=0):
        Label(master,text=label_text,bg=(color)).place(x=x,y=y)
        self.variable=data_type()
        Entry(master,textvariable=self.variable).place(x=x+distance,y=y+height_difference)
        
    

Label(win,text="Payment Management System",bg=("DodgerBlue3"),font=("Arial",18,"italic")).place(x=400,y=20)

id=LabelwithEntry(win,"id:","DodgerBlue3",10,100,IntVar,100)

transaction_type=StringVar()
Label(win,text="transaction_type",bg='DodgerBlue3').place(x=10,y=130)
Radiobutton(win,text="payment",variable=transaction_type,value="payment",bg="lightblue").place(x=110,y=130)
Radiobutton(win,text="reception",variable=transaction_type,value="reception",bg="lightblue").place(x=180,y=130)



Label(win,text="payment_type",bg='DodgerBlue3').place(x=10,y=160)
ttk.Combobox(win,values=[],width=17,textvariable="payment_type",state="readonly").place(x=110,y=160)



date_time=LabelwithEntry(win,"date_time:","DodgerBlue3",10,190,StringVar,100)

customer_id=LabelwithEntry(win,"customer_id:","DodgerBlue3",10,220,StringVar,100)

Button(win,text="save",bg="DodgerBlue2",width=10).place(x=10,y=250)
Button(win,text="update",bg="DodgerBlue2",width=10).place(x=110,y=250)



id=LabelwithEntry(win,"id:","DodgerBlue3",10,330,IntVar,100)

Button(win,text="delete",bg="DodgerBlue2",width=10).place(x=10,y=370)
Button(win,text="find",bg="DodgerBlue2",width=10).place(x=110,y=370)


win.mainloop()
