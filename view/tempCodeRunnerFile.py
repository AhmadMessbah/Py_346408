columns=["id","first_name","last_name","phone_number","address"]

i=1
for col in columns:
    table.heading(i,text=col)
    table.column(i,width=100)
    i+=1
