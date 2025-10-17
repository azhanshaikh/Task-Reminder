import tkinter as tk
from tkinter import messagebox
import os

FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            for task in f.readlines():
                task_list.insert(tk.END, task.strip())

def save_tasks():
    with open(FILE, "w") as f:
        tasks = task_list.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")

def add_task():
    task = entry.get()
    if task.strip() == "":
        messagebox.showwarning("Empty Input", "Please enter a task.")
    else:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()

def delete_task():
    try:
        selected = task_list.curselection()[0]
        task_list.delete(selected)
        save_tasks()
    except:
        messagebox.showwarning("No Selection", "Please select a task to delete.")

def mark_task():
    try:
        selected = task_list.curselection()[0]
        task = task_list.get(selected)
        task_list.delete(selected)
        task_list.insert(selected, f"✓ {task}")
        save_tasks()
    except:
        messagebox.showwarning("No Selection", "Please select a task to mark.")

root = tk.Tk()
root.title("Daily Task Manager")
root.geometry("350x400")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack()

task_list = tk.Listbox(root, width=45, height=15)
task_list.pack(pady=10)

mark_button = tk.Button(root, text="Mark Completed", width=15, command=mark_task)
mark_button.pack()

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack(pady=5)

load_tasks()
root.mainloop()
