import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def edit_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        selected_task = task_listbox.get(selected_index)
        task_entry.delete(0, tk.END)
        task_entry.insert(0, selected_task)

def delete_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        task_listbox.delete(selected_index)

# Create the main application window
app = tk.Tk()
app.title("To-Do List")

# Task entry and buttons
task_entry = tk.Entry(app, width=50)
task_entry.pack(pady=10)

add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack()

edit_button = tk.Button(app, text="Edit Task", command=edit_task)
edit_button.pack()

delete_button = tk.Button(app, text="Delete Task", command=delete_task)
delete_button.pack()

# Task listbox
task_listbox = tk.Listbox(app, selectmode=tk.SINGLE, height=15, width=50)
task_listbox.pack()

# Bind click event to task_listbox
task_listbox.bind("<ButtonRelease-1>", lambda event: edit_task())

# Start the main event loop
app.mainloop()

