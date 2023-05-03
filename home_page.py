import customtkinter as ctk
import  tkinter as tk
import style
import long_text

class HomePage(ctk.CTkFrame):
    def __init__(self, app):
        super().__init__(app.right_side_panel, **style.frame_style)


        self.header_label = ctk.CTkLabel(self, text="Home Page", text_color="black", font=ctk.CTkFont(size=20, weight="bold"))
        self.header_label.grid(row=0, column=0, pady=10, padx=10)

        self.description_label = ctk.CTkLabel(self, text=long_text.home_page_text, text_color="black", font=ctk.CTkFont(size=14), wraplength=200, justify=tk.CENTER)
        self.description_label.grid(row=1, column=0, pady=10, padx=10)