import tkinter as tk
from tkinter import messagebox
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(" panel")
        self.geometry("220x250")

        self.entries = {}
        self.create_form()
        self.create_buttons()
    def create_form(self):
        fields = [
            ("ID", "id"),
            ("Property", "property"),
            ("Panel ID", "panel_id"),
            ("Value", "value")
        ]

        for i, (label_text, key) in enumerate(fields):
            label = tk.Label(self, text=label_text)
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")

            entry = tk.Entry(self)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries[key] = entry

    def create_buttons(self):
        buttons_frame = tk.Frame(self)
        buttons_frame.grid(row=6, column=0, columnspan=2, pady=10)

        add_button = tk.Button(buttons_frame, text="Add", command=self.add_data)
        add_button.grid(row=0, column=0, padx=5)

        edit_button = tk.Button(buttons_frame, text="Edit", command=self.edit_data)
        edit_button.grid(row=0, column=1, padx=5)

        delete_button = tk.Button(buttons_frame, text="Delete", command=self.delete_data)
        delete_button.grid(row=0, column=2, padx=5)

    def add_data(self):
        data = {key: entry.get() for key, entry in self.entries.items()}
        print("Added data:", data)

    def edit_data(self):
        messagebox.showinfo("Edit", "Edit button clicked!")

    def delete_data(self):
        messagebox.showinfo("Delete", "Delete button clicked!")

if __name__ == "__main__":
    app = Application()
    app.mainloop()