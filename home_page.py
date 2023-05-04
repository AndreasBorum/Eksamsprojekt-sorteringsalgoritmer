import customtkinter as ctk
import  tkinter as tk
import style
import long_text
from helper import  CTkWrappingLabel


class HomePage(ctk.CTkFrame):
    def __init__(self, app):
        super().__init__(app.right_side_panel, **style.frame_style)
        self.grid_columnconfigure(1, weight=1)


        self.header_label = ctk.CTkLabel(self, text="Home Page", text_color="black", font=ctk.CTkFont(size=50, weight="bold"))
        self.header_label.grid(row=0, column=1,pady=20, padx=10)
        
        self.description_label = CTkWrappingLabel(self, text=long_text.home_page_text, text_color="black", font=ctk.CTkFont(size=14))
        self.description_label.grid(row=2, column=1, pady=10, padx=50, sticky="ew")


        ctk.CTkFrame(self, corner_radius=3, height=8).grid(row=3, column=1, pady=10, padx=40, sticky="ew")