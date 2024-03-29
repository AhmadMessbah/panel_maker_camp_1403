from tkinter import *
from panel.panelview import *



def person_btn_click():
    pass
def panel_btn_click():
    Panelview[]
def properties_btn_click():
    pass


main_win = Tk()
main_win.title("panel entry")
main_win.geometry("600x400")





person_btn = Button(main_win, font=("arial", 19), width=8, text="person")
person_btn.place(x= 250, y=80)
person_btn.bind("<Button-1>", person_btn_click)

panel_btn = Button(main_win, font=("arial", 19), width=8, text="panel")
panel_btn.place(x= 250, y=160)
panel_btn.bind("<Button-1>", on_click)

properties_btn = Button(main_win, font=("arial", 19), width=8, text="properties")
properties_btn.place(x= 250, y=240)
properties_btn.bind("<Button-1>", properties_btn_click)




main_win.mainloop()