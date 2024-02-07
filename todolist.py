import tkinter as tk
from tkinter import messagebox

class TodoListApp:

    def __init__(self, root):
        self.root = root
        self.root.title("To-do List App")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.grid(row=2, column=0, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

        self.load_tasks()

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append(task_text)
            self.task_listbox.insert(tk.END, task_text)
            self.task_entry.delete(0,tk.END)
            self.save_tasks()

    def update_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            new_text = self.task_entry.get().strip()
            if new_text:
                selected_task = selected_task[0]
                self.tasks[selected_task] = new_text
                self.task_listbox.delete(selected_task)
                self.task_listbox.insert(selected_task, new_text)
                self.save_tasks()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning","Please, enter a valid task")

    def delete_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            selected_task = selected_task[0]
            del self.tasks[selected_task]
            self.task_listbox.delete(selected_task)
            self.save_tasks()

    def save_tasks(self):
        with open("tasks.txt","w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt","r") as file:
                tasks = file.readlines()
                self.tasks = [task.strip() for task in tasks]
                for task in tasks:
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass

root = tk.Tk()
app = TodoListApp(root)
root.mainloop()