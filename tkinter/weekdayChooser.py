import customtkinter as ctk
root = ctk.CTk()
import random
root.geometry('700x100')

def hideAlldays():
    for check in day_labels:
        check.toggle()


    if day_labels[0].get():
        button1.configure(text='Uncheck All days')
    else:  
        button1.configure(text='check All days')



def hideRandomDay():
    uncheckeddays = []
    for day in day_labels:
        if not day.get():
            uncheckeddays.append(day)

    if uncheckeddays:
        randomDay= random.randint(0,len(uncheckeddays)-1)
        uncheckeddays[randomDay].select()
    

        
        
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

frame = ctk.CTkFrame(root)
frame.pack(pady=10)

day_labels = []

for i in days_of_week:
    label = ctk.CTkCheckBox(frame,text=i)
    label.pack(side='left')
    day_labels.append(label)

button1 = ctk.CTkButton(root, text='check All Days', command=hideAlldays)
button1.pack(side='left',expand=True)
button2 = ctk.CTkButton(root, text='Select Random Day', command=hideRandomDay)
button2.pack(side='left',padx=10,expand=True)
 
root.mainloop()