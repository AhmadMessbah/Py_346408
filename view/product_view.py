'''from controller.product_controller import ProductController

name = input("Enter name : ")
description = input("Enter description : ")

product_controller = ProductController()
product_controller.save(name, description)
'''
 
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox as msg

win=Tk()
win.title=("Product")
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
    product=(id.get(),name.get(),brand.get(),model.get(),serial.get(),category.get(),unit.get(),expiration_date.get())
    table.insert("",END,values=product)
    msg.showinfo("saved","product saved")

def update():
    product=(id.set(id.get()),name.set(name.get()),brand.set(brand.get()),model.set(model.get()),serial.set(serial.get()),category.set(category.get()),unit.set(unit.get()),expiration_date.set(expiration_date.get()))
    table.insert(" ",END,values=product)  

def delete():
    pass

def reset_form():
  id.set(0) 
  name.set(" ") 
  brand.set(" ") 
  model.set(" ")
  serial.set(" ")
  category.set(" ")
  unit.set(" ")
  expiration_date.set(" ")
  




Label(win,text="Product Management System",bg=("DodgerBlue3"),font=("Arial",18,"italic")).place(x=400,y=20)

id=LabelwithEntry(win,"id:","DodgerBlue3",10,100,IntVar,100)

name=LabelwithEntry(win,"name:","DodgerBlue3",10,130,StringVar,100)

brand=LabelwithEntry(win,"brand:","DodgerBlue3",10,160,StringVar,100)

model=LabelwithEntry(win,"model:","DodgerBlue3",10,190,StringVar,100)

serial=LabelwithEntry(win,"serial:","DodgerBlue3",10,220,StringVar,100)

category=LabelwithEntry(win,"category:","DodgerBlue3",10,250,IntVar,100)

unit=LabelwithEntry(win,"unit:","DodgerBlue3",10,280,StringVar,100)

expiration_date=LabelwithEntry(win,"expiration_date:","DodgerBlue3",10,310,StringVar,100)



#save
def save_click():
    customer=(id.get(),name.get(),brand.get(),model.get(),serial.get(),category.get(),unit.get(),expiration_date.get())
    table.insert(" ",END,values=customer)
    
Button(win,text="save",bg="DodgerBlue2",width=10).place(x=10,y=350)
Button(win,text="update",bg="DodgerBlue2",width=10).place(x=110,y=350)



id=LabelwithEntry(win,"id:","DodgerBlue3",10,430,IntVar,100)

Button(win,text="delete",bg="DodgerBlue2",width=10).place(x=10,y=470)
Button(win,text="find",bg="DodgerBlue2",width=10).place(x=110,y=470)



#table
table=ttk.Treeview(win,columns=[1,2,3,4,5,6,7,8],show="headings")
table.place(x=400,y=100)


columns=["id","name","brand","model","serial","category","unit","expiration_date"]

i=1
for col in columns:
    table.heading(i,text=col)
    table.column(i,width=100)
    i+=1





win.mainloop()