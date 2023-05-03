import customtkinter as ctk
import  tkinter as tk
import style

class IntroPage(ctk.CTkFrame):
    def __init__(self, app):
        super().__init__(app.right_side_panel, **style.frame_style)


        self.label = ctk.CTkLabel(self, text="intro page", justify=tk.CENTER)
        self.label.pack(padx=10, pady=10)