import tkinter as tk
from person_info import *


def add():
    id = id_entry.get()
    name = name_entry.get()
    family = family_entry.get()
    company = company_entry.get()
    print("Added:")
    print("Id: ", id)
    print("name: ", name)
    print("family: ", family)
    print("company: ", company)


def delete():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    family_entry.delete(0, tk.END)
    company_entry.delete(0, tk.END)


def edit():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    family_entry.delete(0, tk.END)
    company_entry.delete(0, tk.END)


window = tk.Tk()
window.title("Information Form")
# ID
id_button = tk.Label(window, text="ID :")
id_button.grid(row=0, column=0, padx=5, pady=5)
id_entry = tk.Entry(window)
id_entry.grid(row=0, column=1, padx=5, pady=5)
# Name
name_button = tk.Label(window, text="Name :")
name_button.grid(row=1, column=0, padx=5, pady=5)
name_entry = tk.Entry(window)
name_entry.grid(row=1, column=1, padx=5, pady=5)
# Family
family_button = tk.Label(window, text="Family: ")
family_button.grid(row=2, column=0, padx=5, pady=5)
family_entry = tk.Entry(window)
family_entry.grid(row=2, column=1, padx=5, pady=5)
# Company
company_button = tk.Label(window, text="Company: ")
company_button.grid(row=3, column=0, padx=5, pady=5)
company_entry = tk.Entry(window)
company_entry.grid(row=3, column=1, padx=5, pady=5)

edit_button = tk.Button(window, text="Edit", command=add)
edit_button.grid(row=5, column=5, padx=5, pady=5)

delete_button = tk.Button(window, text="Delete", command=delete)
delete_button.grid(row=5, column=4, padx=4, pady=4)

add_button = tk.Button(window, text="Add", command=edit)
add_button.grid(row=5, column=3, padx=3, pady=3)
window.mainloop()
