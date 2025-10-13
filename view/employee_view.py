from tkinter import *

win=Tk()
win.title=("Employee")
win.geometry="1000x1000"
win.configure(bg="lightblue")




class LabelwithEntry:
    def __init__(self,master,label_text,color,x,y,data_type=StringVar,distance=110,height_difference=0):
        Label(master,text=label_text,bg=(color)).place(x=x,y=y)
        self.variable=data_type()
        Entry(master,textvariable=self.variable).place(x=x+distance,y=y+height_difference)
        
    

Label(win,text="Employee Management System",bg=("DodgerBlue3"),font=("Arial",18,"italic")).place(x=400,y=20)

id=LabelwithEntry(win,"id:","DodgerBlue3",10,100,IntVar,100)

first_name=LabelwithEntry(win,"first_name:","DodgerBlue3",10,130,StringVar,100)

last_name=LabelwithEntry(win,"last_name:","DodgerBlue3",10,160,StringVar,100)

salary=LabelwithEntry(win,"salary:","DodgerBlue3",10,190,StringVar,100)

occupation=LabelwithEntry(win,"occupation:","DodgerBlue3",10,220,StringVar,100)

phone_number=LabelwithEntry(win,"phone_number:","DodgerBlue3",10,250,IntVar,100)

username=LabelwithEntry(win,"username:","DodgerBlue3",10,280,StringVar,100)

password=LabelwithEntry(win,"password:","DodgerBlue3",10,310,StringVar,100)

Button(win,text="save",bg="DodgerBlue2",width=10).place(x=10,y=350)
Button(win,text="update",bg="DodgerBlue2",width=10).place(x=110,y=350)



id=LabelwithEntry(win,"id:","DodgerBlue3",10,430,IntVar,100)

Button(win,text="delete",bg="DodgerBlue2",width=10).place(x=10,y=470)
Button(win,text="find",bg="DodgerBlue2",width=10).place(x=110,y=470)








win.mainloop()