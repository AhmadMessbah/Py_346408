from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win=Tk()
win.title=("customer")
win.geometry="1000x1000"
win.configure(bg="lightblue")




class LabelwithEntry:
    def __init__(self,master,label_text,color,x,y,data_type=StringVar,distance=110,height_difference=0):
        Label(master,text=label_text,bg=(color)).place(x=x,y=y)
        self.variable=data_type()
        Entry(master,textvariable=self.variable).place(x=x+distance,y=y+height_difference)
        
    

Label(win,text="customer Management System",bg=("DodgerBlue3"),font=("Arial",18,"italic")).place(x=400,y=20)

id=LabelwithEntry(win,"id:","DodgerBlue3",10,100,IntVar,100)

first_name=LabelwithEntry(win,"first_name:","DodgerBlue3",10,130,StringVar,100)

last_name=LabelwithEntry(win,"last_name:","DodgerBlue3",10,160,StringVar,100)

phone_number=LabelwithEntry(win,"phone_number:","DodgerBlue3",10,190,IntVar,100)

address=LabelwithEntry(win,"address:","DodgerBlue3",10,220,StringVar,100)


Button(win,text="save",bg="DodgerBlue2",width=10).place(x=10,y=250)
Button(win,text="update",bg="DodgerBlue2",width=10).place(x=110,y=250)



id=LabelwithEntry(win,"id:","DodgerBlue3",10,330,IntVar,100)

Button(win,text="delete",bg="DodgerBlue2",width=10).place(x=10,y=370)
Button(win,text="find",bg="DodgerBlue2",width=10).place(x=110,y=370)

#table
table=ttk.Treeview(win,columns=[1,2,3,4,5],show="headings")
table.place(x=400,y=100)

table.heading(1, text="id")
table.heading(1, text="first_name")
table.heading(1, text="last_name")
table.heading(1, text="phone_number")
table.heading(1, text="address")


table.column(1,width=100)
table.column(2,width=100)
table.column(3,width=100)
table.column(4,width=100)
table.column(5,width=100)












win.mainloop()