import customtkinter as ctk
from style import classes_style as style


class HomePage(ctk.CTkFrame):
    """Home page class that is a tk frame"""

    def __init__(self, parent, master):
        super().__init__(parent)
        self.parent = parent

        # temp
        page_label = ctk.CTkLabel(self, text="Home Page")
        page_label.grid(row=0, column=0, columnspan=2)

        # welcome lable
        welcome_label = ctk.CTkLabel(self, text='Velkommen')
        welcome_label.grid(row=1, column=0, padx=30, sticky='N')