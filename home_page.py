import customtkinter as ctk
from PIL import Image

import style
import import_text
from helper import CTkWrappingLabel


class HomePage(ctk.CTkFrame):
    def __init__(self, app):
        super().__init__(app.right_side_panel, **style.frame_style)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.header_label = ctk.CTkLabel(
            self, text="Home Page", text_color="black", font=ctk.CTkFont(size=50, weight="bold"))
        self.header_label.grid(row=0, column=1, pady=20, padx=10)

        self.description_label = CTkWrappingLabel(
            self, text=import_text.home_page_text, text_color="black", font=ctk.CTkFont(size=14))
        self.description_label.grid(
            row=2, column=1, pady=10, padx=50, sticky="ew")

        ctk.CTkFrame(self, corner_radius=3, height=8).grid(
            row=3, column=1, pady=10, padx=40, sticky="ew")

        menu_frame = ctk.CTkFrame(self, fg_color="gray85")
        menu_frame.grid(row=4, column=1, sticky="nsew", padx=20, pady=10)
        menu_frame.columnconfigure((0, 1, 2), weight=1)

        image_height = 110
        image_width = image_height*(16/9)

        intro_image = ctk.CTkImage(Image.open(
            "images\intro page.png"), size=(image_width, image_height))
        intro_btn = ctk.CTkButton(menu_frame, image=intro_image, text="Intro",
                                  compound="top", command=lambda: app.show_frame_by_number(1))
        intro_btn.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        ctk.CTkFrame(menu_frame, corner_radius=1, height=3).grid(
            row=1, column=0, columnspan=5, pady=10, padx=40, sticky="ew")

        bubble_image = ctk.CTkImage(Image.open(
            r"images\bubble page.png"), size=(image_width, image_height))
        bubble_btn = ctk.CTkButton(menu_frame, image=bubble_image, text="Bubblesort",
                                   compound="top", command=lambda: app.show_frame_by_number(2))
        bubble_btn.grid(row=2, column=0, padx=10, pady=10)

        quick_image = ctk.CTkImage(Image.open(
            "images\quick page.png"), size=(image_width, image_height))
        quick_btn = ctk.CTkButton(menu_frame, image=quick_image, text="Quicksort",
                                  compound="top", command=lambda: app.show_frame_by_number(3))
        quick_btn.grid(row=2, column=1, padx=10, pady=10)

        coming_soon_image = ctk.CTkImage(Image.open(
            "images\coming soon.jpg"), size=(image_width, image_height))
        coming_soon_btn = ctk.CTkButton(
            menu_frame, image=coming_soon_image, text="Comming soon", compound="top")
        coming_soon_btn.grid(row=2, column=2, padx=10, pady=10)

        ctk.CTkFrame(menu_frame, corner_radius=1, height=3).grid(
            row=3, column=0, columnspan=5, pady=10, padx=40, sticky="ew")

        big_o_image = ctk.CTkImage(Image.open(
            r"images\big O page.png"), size=(image_width, image_height))
        big_o_btn = ctk.CTkButton(menu_frame, image=big_o_image, text="Big O notation",
                                  compound="top", command=lambda: app.show_frame_by_number(4))
        big_o_btn.grid(row=4, column=0, columnspan=5, padx=10, pady=10)
