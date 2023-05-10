import customtkinter as ctk
import  tkinter as tk
from PIL import  Image
import webbrowser


import style
import import_text
from animation.quick_sort import QuickSort
from algorithms_page  import AlgorithmPage
from next_prev_frame import NextPrevFrame
from helper import CTkWrappingLabel



class QuickSortPage(AlgorithmPage):
    def __init__(self, app):
        super().__init__(app.right_side_panel, QuickSort)

        self.header_label.configure(text="QuickSort")

        self.description_label = CTkWrappingLabel(self.description_frame, text=import_text.quick_page_text, text_color="black", justify=tk.LEFT)
        self.description_label.grid(row=1, column=0, pady=10, padx=10, sticky="ew")

        yt_btn = ctk.CTkButton(self.description_frame, text="Watch Video", command=lambda: webbrowser.open("https://youtu.be/Vtckgz38QHs?t=10",new=1))
        yt_btn.grid(row=2, column=0, pady=10, padx=10)

        flowchart_image = ctk.CTkImage(Image.open(r"images\Quick_sort_algorithm.png"), size=(400,300))
        flowchart_label = ctk.CTkLabel(self.description_frame, image=flowchart_image, text="")
        flowchart_label.grid(row=3, column=0, padx=10, pady=10)


        next_prev_frame = NextPrevFrame(self, app, 2, 4)
        next_prev_frame.grid(row=7, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)