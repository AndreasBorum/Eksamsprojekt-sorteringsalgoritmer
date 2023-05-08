import tkinter as tk
import customtkinter as ctk
from time import sleep

from home_page import HomePage
from intro_page import IntroPage
from bubble_page import BubblesortPage
from quick_page import QuickSortPage


#https://stackoverflow.com/a/74844868

DARK_MODE = "dark"
ctk.set_appearance_mode(DARK_MODE)
ctk.set_default_color_theme("dark-blue")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("Change Frames")
        self.geometry("800x600+10+10")
        self.after(0, lambda:self.state('zoomed'))
        self.protocol("WM_DELETE_WINDOW", self.close_window)
        
        # root!
        self.main_container = ctk.CTkFrame(self, corner_radius=10)
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # left side panel -> for frame selection
        self.left_side_panel = ctk.CTkFrame(self.main_container, width=150, corner_radius=10)
        self.left_side_panel.pack(side=tk.LEFT, fill=tk.Y, expand=False, padx=5, pady=5)
        
        self.left_side_panel.grid_columnconfigure(0, weight=1)
        self.left_side_panel.grid_rowconfigure((0, 1, 2, 3), weight=0)
        self.left_side_panel.grid_rowconfigure((4, 5), weight=1)
        self.left_side_panel.grid_propagate(0)
        
        
        # self.left_side_panel WIDGETs
        self.logo_label = ctk.CTkLabel(self.left_side_panel, text="Welcome! \n", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        #self.scaling_label = ctk.CTkLabel(self.left_side_panel, text="UI Scaling:", anchor="w")
        #self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        #
        #self.scaling_optionemenu = ctk.CTkOptionMenu(self.left_side_panel, values=["80%", "90%", "100%", "110%", "120%"],
        #                                                    command=self.change_scaling_event)
        #self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20), sticky = "s")
        
        self.bt_Quit = ctk.CTkButton(self.left_side_panel, text="Quit", fg_color= '#EA0000', hover_color = '#B20000', command= self.close_window)
        self.bt_Quit.grid(row=9, column=0, padx=20, pady=10)
        
        # button to select correct frame IN self.left_side_panel WIDGET
        self.bt_home = ctk.CTkButton(self.left_side_panel, text="Home page", command=lambda: self.show_frame(HomePage))
        self.bt_home.grid(row=1, column=0, padx=20, pady=10)

        self.bt_intro = ctk.CTkButton(self.left_side_panel, text="Intro  page", command=lambda: self.show_frame(IntroPage))
        self.bt_intro.grid(row=2, column=0, padx=20, pady=10)
        
        self.bt_bubblesort = ctk.CTkButton(self.left_side_panel, text="Manage Categories", command=lambda: self.show_frame(BubblesortPage))
        self.bt_bubblesort.grid(row=3, column=0, padx=(40,20), pady=10)

        self.bt_quicksort = ctk.CTkButton(self.left_side_panel, text="Manage Products", command=lambda: self.show_frame(QuickSortPage))
        self.bt_quicksort.grid(row=4, column=0, padx=(40,20), pady=10)


        

        # right side panel -> have self.right_dashboard inside it
        self.right_side_panel = ctk.CTkFrame(self.main_container, corner_radius=10, fg_color="#000811")
        self.right_side_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.right_side_panel.grid_rowconfigure(0, weight = 1)
        self.right_side_panel.grid_columnconfigure(0, weight = 1)

    

        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (HomePage, IntroPage, BubblesortPage, QuickSortPage):
            frame = F(self)
  
            # initializing frame
            self.frames[F] = frame
  
            frame.grid(in_=self.right_side_panel, row = 0, column = 0, sticky ="nsew")          

        self.show_frame(BubblesortPage)


    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        self.frames[BubblesortPage].animation_frame.canvas.animation_thread.unset_on_page()
        self.frames[QuickSortPage].animation_frame.canvas.animation_thread.unset_on_page()
        frame = self.frames[cont]
        if frame ==  self.frames[BubblesortPage] or frame == self.frames[QuickSortPage]:
            frame.animation_frame.canvas.animation_thread.set_on_page()
        frame.tkraise()


    ## Change scaling of all widget 80% to 120%
    #def change_scaling_event(self, new_scaling: str):
    #    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    #    ctk.set_widget_scaling(new_scaling_float)
        
        
    # close the entire window    
    def close_window(self): 
            self.frames[BubblesortPage].animation_frame.canvas.animation_thread.close_thread()
            self.frames[QuickSortPage].animation_frame.canvas.animation_thread.close_thread()
            App.destroy(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()