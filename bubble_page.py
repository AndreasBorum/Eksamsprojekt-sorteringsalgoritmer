import customtkinter as ctk
import  tkinter as tk
import style
import long_text
from animation.bubble_sort import BubbleSort
from algorithms_page  import AlgorithmPage

class BubblesortPage(AlgorithmPage):
    def __init__(self, app):
        super().__init__(app.right_side_panel, BubbleSort)

        self.header_label.configure(text="Bubble Sort")

        self.description_label = ctk.CTkLabel(self.description_frame, text=long_text.home_page_text, text_color="black", font=ctk.CTkFont(size=14), wraplength=200, justify=tk.CENTER)
        self.description_label.grid(row=1, column=0, pady=10, padx=10)