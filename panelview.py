from tkinter import *

# Panelview():
    required_panel = []

    def submit_btn_click(event):
        required_panel.append(id_value.get())
        required_panel.append(panel_value.get())
        required_panel.append(person_value.get())
        required_panel.append(duration_value.get())
        required_panel.append(price_value.get())







    panel_win = Tk()
    panel_win.title("panel entry")
    panel_win.geometry("600x400")

    # id_lbl
    id_value = StringVar()
    Entry(panel_win, font=("arial", 20), textvariable=id_value, bg="lightblue").place(x=100, y=40)

    # panel_id_lbl
    panel_id_value = StringVar()
    Entry(panel_win, font=("arial", 20), textvariable=panel_id_value, bg="lightblue").place(x=100, y=80)

    # person_id_lbl
    person_id_value = StringVar()
    Entry(panel_win, font=("arial", 20), textvariable=person_id_value, bg="lightblue").place(x=100, y=120)

    # duration_lbl
    duration_value = StringVar()
    Entry(panel_win, font=("arial", 20), textvariable=duration_value, bg="lightblue").place(x=100, y=160)

    # price_lbl
    price_value = StringVar()
    Entry(panel_win, font=("arial", 20), textvariable=price_value, bg="lightblue").place(x=100, y=200)




    submit_btn = Button(panel_win, font=("arial", 17), width=8, text="submit")
    submit_btn.place(x= 250, y=300)
    submit_btn.bind("<Button-1>", submit_btn_click)





    panel_win.mainloop()