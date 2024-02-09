import tkinter as tk
import string
import random
from tkinter import messagebox 

def password_generator():
    length_str = length_entry.get()
    if not length_str:
        messagebox.showerror("Error","Please enter a password length")

    length = int(length_str)
    if length <= 0:
        messagebox.showerror("Error", "Password length should be a positive integer")
        return
    

    complexities = {
        "low" : string.ascii_uppercase + string.digits,
        "medium" : string.ascii_letters + string.digits,
        "high" : string.ascii_letters + string.digits + string.punctuation
    }

    complexity_level = complexity_var.get()
    selected_complexities = complexities[complexity_level]

    password = "".join(random.choice(selected_complexities) for i in range(length))
    
    generated_password_var.set(password)

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length")
length_label.grid(row=0, column=0, padx=5, pady=5)

length_entry = tk.Entry(root, width=20)
length_entry.grid(row=0, column=1, padx=5, pady=5)

complexity_label = tk.Label(root, text="Complexity Level")
complexity_label.grid(row=1, column=0, padx=5, pady=5)

complexity_var = tk.StringVar(root)
complexity_var.set("medium")
complexity_var_option = tk.OptionMenu(root, complexity_var, 'low','medium','high')
complexity_var_option.grid(row=1, column=1, padx=5, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=password_generator)
generate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

generated_password_var= tk.StringVar()
generated_password_label = tk.Label(root, fg="blue", textvariable=generated_password_var)
generated_password_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


root.mainloop()

