import customtkinter as ctk
import  tkinter as tk
import style
from animation.animation_frame import AnimationFrame

class AlgorithmPage(ctk.CTkFrame):
    def __init__(self, app, algoritmn_type):
        super().__init__(app, **style.frame_style)
        self.grid_columnconfigure(0, weight=1)
        #self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.animation_frame = AnimationFrame(self, algoritmn_type)
        self.animation_frame.grid(row=0, column=1, pady=10, padx=10, sticky="nsew")


        self.description_frame = tk.Frame(self, highlightbackground="blue", highlightthickness=2)
        self.description_frame.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        self.description_frame.grid_columnconfigure(0, weight=1)


        self.header_label = ctk.CTkLabel(self.description_frame, text_color="black", font=ctk.CTkFont(size=20, weight="bold"))
        self.header_label.grid(row=0, column=0, pady=10, padx=10, sticky="ew")
