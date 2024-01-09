import customtkinter as ctk
from tkinter import ttk, messagebox
import sqlite3

root = ctk.CTk()
root.title("Todo List App")
# root.geometry("500x500")

id_var = ctk.StringVar()
taskName_var = ctk.StringVar()
taskStatus_var = ctk.StringVar()

tasks = []

# Database

db_file = "taskDB.db";
conn = sqlite3.connect(db_file)

cursor = conn.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Tasks(
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT,
        Status TEXT
    )
    ''')

conn.commit()

def update_table():
    table.delete(*table.get_children())
    for task in tasks:
        table.insert("", "end", values=task)

def load_from_db():
    global tasks
    cursor = conn.cursor()
    cursor.execute('Select Id, Name, Status FROM Tasks')
    conn.commit()
    tasks = cursor.fetchall()
    
    update_table()
    
    


# Button Commands
def add_task():
    taskName = taskName_var.get()
    taskStatus = taskStatus_var.get()
    
    if taskName:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Tasks(Name, Status) VALUES (?,?)', (taskName, taskStatus))
        conn.commit()
        messagebox.showinfo("Success", "Task was added successfully")
        load_from_db()
        clear_form()



def update_task():
    task_id = id_var.get()
    task_name = taskName_var.get()
    task_status = taskStatus_var.get()
    if task_id != "" and task_name != "":
        cursor = conn.cursor()
        cursor.execute('UPDATE Tasks SET Name=?, Status=? WHERE id=?', (task_name, task_status, task_id))
        conn.commit()
        messagebox.showinfo("Success", "Task was updated sucessfully")
        load_from_db()
        clear_form()
    else:
        messagebox.showerror("Error", "Please select a task")


def delete_task():
    task_id = id_var.get()
    
    if task_id:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Tasks WHERE id=?', (task_id))
        conn.commit()
        load_from_db()
        clear_form()
        messagebox.showinfo("Success", "Task was deleted successfully")
    else:
        messagebox.showerror("Error", "Please select a task")

def clear_form():
    taskName_var.set("")
    id_var.set("")
    taskStatus_var.set("Not Completed")

def selected_task(event):
    selected_task = table.selection()
    
    if selected_task:
        task_id = table.item(selected_task)['values'][0]
        task_name = table.item(selected_task)['values'][1]
        task_status = table.item(selected_task)['values'][2]
        
        id_var.set(task_id)
        taskName_var.set(task_name)
        taskStatus_var.set(task_status)


form_frame = ctk.CTkFrame(root)
form_frame.pack(side=ctk.TOP, pady=20)

ctk.CTkLabel(form_frame, text="Task Id:").grid(row=0, column=0, padx=(10, 5))
entry_id = ctk.CTkEntry(form_frame, textvariable=id_var, state='disabled')
entry_id.grid(row=0, column=1)

ctk.CTkLabel(form_frame, text="Task Name:").grid(row=1, column=0, padx=(10, 5))
entry_taskName = ctk.CTkEntry(form_frame, textvariable=taskName_var)
entry_taskName.grid(row=1, column=1)

ctk.CTkLabel(form_frame, text="Task Status:").grid(row=2, column=0)
entry_taskStatus = ctk.CTkComboBox(form_frame, values=[
    'Completed',
    'Not Completed'
], variable=taskStatus_var)
entry_taskStatus.grid(row=2, column=1)
entry_taskStatus.set('Not Completed')

# Buttons
button_frame = ctk.CTkFrame(form_frame)
button_frame.grid(row=3, column=0, columnspan=2, pady=20)

add_button = ctk.CTkButton(button_frame, text="Add Task", command=add_task)
add_button.pack(side=ctk.LEFT, padx=10)

update_button = ctk.CTkButton(button_frame, text="Update Task", command=update_task)
update_button.pack(side=ctk.LEFT, padx=10)

delete_button = ctk.CTkButton(button_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=ctk.LEFT, padx=10)


clear_button = ctk.CTkButton(button_frame, text="Clear", command=clear_form)
clear_button.pack(side=ctk.LEFT, padx=10)


# Table
table_frame = ctk.CTkFrame(root)
table_frame.pack(side=ctk.BOTTOM, pady=10)


columns = ('Task Id', 'Task Name', 'Task Status')

table = ttk.Treeview(table_frame, columns=columns, show='headings')
table.grid(row=0, column=0, sticky='nesw')


for column in columns:
    table.heading(column, text=column)
    table.column(column)

# Select Task from Table
table.bind('<<TreeviewSelect>>', selected_task)

load_from_db()

root.mainloop()