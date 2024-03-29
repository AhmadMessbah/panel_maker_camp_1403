from tikinter import *
from validator import *

def submit():
    id = id_entry.get()
    name = name_entry.get()
    if name_validator(name) == False:
        print("invalid name")
    family = family_entry.get()
    if family_validator(family) == False:
        print("invalid family")
    company = company_entry.get()
    if company_validator(company) == False:
        print("invalid company")
    print("Id: ",id)
    print("name: ",name)
    print("family: ",family)
    print("company: ",company)


print(1)
