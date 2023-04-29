import tkinter as tk
import customtkinter as ctk

#https://stackoverflow.com/a/74844868

DARK_MODE = "dark"
ctk.set_appearance_mode(DARK_MODE)
ctk.set_default_color_theme("dark-blue")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("Change Frames")
        self.geometry("800x600")
        
        # root!
        self.main_container = ctk.CTkFrame(self, corner_radius=10)
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # left side panel -> for frame selection
        self.left_side_panel = ctk.CTkFrame(self.main_container, width=150, corner_radius=10)
        self.left_side_panel.pack(side=tk.LEFT, fill=tk.Y, expand=False, padx=5, pady=5)
        
        self.left_side_panel.grid_columnconfigure(0, weight=1)
        self.left_side_panel.grid_rowconfigure((0, 1, 2, 3), weight=0)
        self.left_side_panel.grid_rowconfigure((4, 5), weight=1)
        
        
        # self.left_side_panel WIDGET
        self.logo_label = ctk.CTkLabel(self.left_side_panel, text="Welcome! \n", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.scaling_label = ctk.CTkLabel(self.left_side_panel, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.left_side_panel, values=["80%", "90%", "100%", "110%", "120%"],
                                                            command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20), sticky = "s")
        
        self.bt_Quit = ctk.CTkButton(self.left_side_panel, text="Quit", fg_color= '#EA0000', hover_color = '#B20000', command= self.close_window)
        self.bt_Quit.grid(row=9, column=0, padx=20, pady=10)
        
        # button to select correct frame IN self.left_side_panel WIDGET
        self.bt_dashboard = ctk.CTkButton(self.left_side_panel, text="Dashboard")
        self.bt_dashboard.grid(row=1, column=0, padx=20, pady=10)

        self.bt_statement = ctk.CTkButton(self.left_side_panel, text="Statement")
        self.bt_statement.grid(row=2, column=0, padx=20, pady=10)
        
        self.bt_categories = ctk.CTkButton(self.left_side_panel, text="Manage Categories")
        self.bt_categories.grid(row=3, column=0, padx=20, pady=10)
        

        # right side panel -> have self.right_dashboard inside it
        self.right_side_panel = ctk.CTkFrame(self.main_container, corner_radius=10, fg_color="#000811")
        self.right_side_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        
        #self.right_dashboard = ctk.CTkFrame(self.main_container, corner_radius=10, fg_color="blue")
        #self.right_dashboard.pack(in_=self.right_side_panel, side=tk.TOP, fill=tk.BOTH, expand=True, padx=0, pady=0)
        

        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (HomePage, StartPage):
            frame = F(self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            



            #frame.pack(in_=self.right_side_panel, side=tk.TOP, fill=tk.BOTH, expand=True, padx=0, pady=0)
  
        self.show_frame(HomePage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.pack(in_=self.right_side_panel, side=tk.TOP, fill=tk.BOTH, expand=True, padx=0, pady=0)



    # Change scaling of all widget 80% to 120%
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)
        
        
    # close the entire window    
    def close_window(self): 
            App.destroy(self)
            
            
    # CLEAR ALL THE WIDGET FROM self.right_dashboard(frame) BEFORE loading the widget of the concerned page       
    def clear_frame(self):
        for widget in self.right_dashboard.winfo_children():
            widget.destroy()



class HomePage(ctk.CTkFrame):
    def __init__(self, app):
        super().__init__(app.right_side_panel, corner_radius=10, fg_color="blue")

        #self.pack(in_=app.right_side_panel, side=tk.TOP, fill=tk.BOTH, expand=True, padx=0, pady=0)

        self.label = ctk.CTkLabel(self, text="Home Page")
        self.label.pack(padx=10, pady=10)
        self.canvas = tk.Canvas(self, width=100, height=100, bg='gray75')
        self.canvas.pack()


class StartPage(ctk.CTkFrame):
    def __init__(self, app):
        super().__init__(app.right_side_panel, corner_radius=10, fg_color="blue")

        #self.pack(in_=app.right_side_panel, side=tk.TOP, fill=tk.BOTH, expand=True, padx=0, pady=0)

        self.label = ctk.CTkLabel(self, text="Start Page")
        self.label.pack(padx=10, pady=10)



a = App()
a.mainloop()