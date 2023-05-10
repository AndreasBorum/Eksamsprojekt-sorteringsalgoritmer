import tkinter as tk
import customtkinter as ctk


class NextPrevFrame(tk.Frame):
    def __init__(self, parent, app,  prev_page, next_page):
        tk.Frame.__init__(self, parent, bg="gray85")

        self.prev_button = ctk.CTkButton(
            self, text="Previous",  command=lambda: app.show_frame_by_number(prev_page))
        self.prev_button.pack(side="left")

        self.next_button = ctk.CTkButton(
            self, text="Next",   command=lambda: app.show_frame_by_number(next_page))
        self.next_button.pack(side="right")

        if next_page == 0:
            self.next_button.configure(text="Home")
