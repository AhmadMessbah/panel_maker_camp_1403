import tkinter as tk
from person_info import *

def submit():
    id = id_entry.get()
    name = name_entry.get()
    #if name_validator(name) == False:
        #print("invalid name")
    family = family_entry.get()
   # if family_validator(family) == False:
       # print("invalid family")
    company = company_entry.get()
   # if company_validator(company) == False:
        #print("invalid company")
    print("Id: ",id)
    print("name: ",name)
    print("family: ",family)
    print("company: ",company)

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

submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.grid(row=5, column=5, padx=5, pady=5)
window.mainloop()
