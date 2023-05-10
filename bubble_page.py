import customtkinter as ctk
from PIL import Image

from helper import CTkWrappingLabel
import import_text
from animation.bubble_sort import BubbleSort
from algorithms_page import AlgorithmPage
from next_prev_frame import NextPrevFrame


class BubblesortPage(AlgorithmPage):
    def __init__(self, app):
        super().__init__(app.right_side_panel, BubbleSort)

        self.header_label.configure(text="Bubble Sort")

        self.description_label = CTkWrappingLabel(
            self.description_frame, text=import_text.bubble_page_text, text_color="black", justify="left")
        self.description_label.grid(
            row=1, column=0, pady=10, padx=10, sticky="new")

        flowchart_image = ctk.CTkImage(Image.open(
            r"images\bubble flowchart.png"), size=(300, 500))
        flowchart_label = ctk.CTkLabel(
            self.description_frame, image=flowchart_image, text="")
        flowchart_label.grid(row=1, column=1, sticky="ne", padx=10, pady=10)

        next_prev_frame = NextPrevFrame(self, app, 1, 3)
        next_prev_frame.grid(row=7, column=0, columnspan=2,
                             sticky="nsew", padx=10, pady=10)
