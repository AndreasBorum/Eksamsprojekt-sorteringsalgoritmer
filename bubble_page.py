import customtkinter as ctk
import  tkinter as tk
import style
import long_text
from animation.animation_frame import AnimationFrame
from animation.bubble_sort import BubbleSort

class BubblesortPage(ctk.CTkFrame):
    def __init__(self, app):
        super().__init__(app.right_side_panel, **style.frame_style)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.description_frame = tk.Frame(self, highlightbackground="blue", highlightthickness=2)
        self.description_frame.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        self.animation_frame = AnimationFrame(self, BubbleSort)
        self.animation_frame.grid(row=0, column=1, pady=10, padx=10, sticky="nsew")

        self.header_label = ctk.CTkLabel(self.description_frame, text="Bubble sort", text_color="black", font=ctk.CTkFont(size=20, weight="bold"))
        self.header_label.grid(row=0, column=0, pady=10, padx=10)

        self.description_label = ctk.CTkLabel(self.description_frame, text=long_text.home_page_text, text_color="black", font=ctk.CTkFont(size=14), wraplength=200, justify=tk.CENTER)
        self.description_label.grid(row=1, column=0, pady=10, padx=10)