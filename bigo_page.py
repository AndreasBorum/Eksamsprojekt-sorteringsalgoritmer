import customtkinter as ctk
import  tkinter as tk
from PIL import Image



import style
from helper import CTkWrappingLabel
import import_text
from next_prev_frame  import NextPrevFrame

class BigOPage(ctk.CTkFrame):
    def __init__(self, app):
        super().__init__(app.right_side_panel, **style.frame_style)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(6, weight=1)


        self.header_label = ctk.CTkLabel(self, text="Big O page", justify=tk.CENTER, text_color="black", font=ctk.CTkFont(size=20, weight="bold"))
        self.header_label.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

        self.intro_label =CTkWrappingLabel(self, text=import_text.bigo_page_text, text_color="black", justify=tk.LEFT)
        self.intro_label.grid(row=1, column=0, sticky="new", padx=10, pady=10)

        flowchart_image = ctk.CTkImage(Image.open("images\BigO.png"), size=(600,500))
        flowchart_label = ctk.CTkLabel(self, image=flowchart_image, text="")
        flowchart_label.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        next_prev_frame = NextPrevFrame(self, app, 3, 0)
        next_prev_frame.grid(row=7, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
