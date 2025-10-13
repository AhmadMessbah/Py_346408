from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg

win=Tk()
win.title=("customer")
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
    customer=(id.get(),first_name.get(),last_name.get(),phone_number.get(),address.get())
    table.insert("",END,values=customer)
    msg.showinfo("saved","customer saved")
    reset_form()
    
def update():
    customer=(id.set(id.get()),first_name.set(first_name.get()),last_name.set(last_name.get()),phone_number.set(phone_number.get()),address.set(address.get()))
    reset_form()
    
def delete():
    pass
    
def reset_form():
  id.set(0) 
  first_name.set(" ") 
  last_name.set(" ") 
  phone_number.set(0)
  address.set(" ")
  
  
#title
Label(win,text="customer Management System",bg=("DodgerBlue3"),font=("Arial",18,"italic")).place(x=400,y=20)
#id
id=LabelwithEntry(win,"id:","DodgerBlue3",10,100,IntVar,100)

#first_name
first_name=LabelwithEntry(win,"first_name:","DodgerBlue3",10,130,StringVar,100)

#last_name
last_name=LabelwithEntry(win,"last_name:","DodgerBlue3",10,160,StringVar,100)

#phone_number
phone_number=LabelwithEntry(win,"phone_number:","DodgerBlue3",10,190,IntVar,100)


#address
address=LabelwithEntry(win,"address:","DodgerBlue3",10,220,StringVar,100)




    
Button(win,text="save",bg="DodgerBlue2",command=save,width=10).place(x=10,y=250)


Button(win,text="update",bg="DodgerBlue2",width=10).place(x=110,y=250)



id=LabelwithEntry(win,"id:","DodgerBlue3",10,330,IntVar,100)

Button(win,text="delete",bg="DodgerBlue2",width=10).place(x=10,y=370)
Button(win,text="find",bg="DodgerBlue2",width=10).place(x=110,y=370)

#table
table=ttk.Treeview(win,columns=[1,2,3,4,5],show="headings")
table.place(x=400,y=100)



columns=["id","first_name","last_name","phone_number","address"]

i=1
for col in columns:
    table.heading(i,text=col)
    table.column(i,width=100)
    i+=1









win.mainloop()