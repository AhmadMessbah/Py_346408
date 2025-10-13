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
win.configure(bg="#FFF8F0")




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
    reset_form()
    
def update():
    product=(id.set(id.get()),name.set(name.get()),brand.set(brand.get()),model.set(model.get()),serial.set(serial.get()),category.set(category.get()),unit.set(unit.get()),expiration_date.set(expiration_date.get()))
    table.insert("",END,values=product)  
    reset_form()
    
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
  




Label(win,text="Product Management System",bg=("#F18284"),font=("Arial",18,"italic")).place(x=400,y=20)

id=LabelwithEntry(win,"id:","#FFFFFF",10,100,IntVar,100)

name=LabelwithEntry(win,"name:","#FFFFFF",10,130,StringVar,100)

brand=LabelwithEntry(win,"brand:","#FFFFFF",10,160,StringVar,100)

model=LabelwithEntry(win,"model:","#FFFFFF",10,190,StringVar,100)

serial=LabelwithEntry(win,"serial:","#FFFFFF",10,220,StringVar,100)

category=LabelwithEntry(win,"category:","#FFFFFF",10,250,IntVar,100)

unit=LabelwithEntry(win,"unit:","#FFFFFF",10,280,StringVar,100)

expiration_date=LabelwithEntry(win,"expiration_date:","#FFFFFF",10,310,StringVar,100)



#save
def save_click():
    customer=(id.get(),name.get(),brand.get(),model.get(),serial.get(),category.get(),unit.get(),expiration_date.get())
    table.insert(" ",END,values=customer)
    
Button(win,text="save",bg="#FFD6A5",width=10).place(x=10,y=350)
Button(win,text="update",bg="#B5EAD7",width=10).place(x=110,y=350)



id=LabelwithEntry(win,"id:","#FFFFFF",10,430,IntVar,100)

Button(win,text="delete",bg="#A7C7E7",width=10).place(x=10,y=470)
Button(win,text="find",bg="#FFD6A5",width=10).place(x=110,y=470)



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