import customtkinter as ctk


class CTkWrappingLabel(ctk.CTkLabel):
    '''a type of Label that automatically adjusts the wrap to the size
    this function is a modified version of:https://stackoverflow.com/a/62485627'''

    def __init__(self, master=None, **kwargs):
        ctk.CTkLabel.__init__(self, master, **kwargs)
        self.bind('<Configure>', self.update)

    def update(self, *arg):
        self.configure(wraplength=self.winfo_width()*0.77)
