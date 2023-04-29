import customtkinter as ctk
from home_page import HomePage

class App(ctk.CTk):
    """the tkinter class where the GUI runs"""
    def __init__(self):
        super().__init__()

        ## Setting up Initial Things
        self.title("Sample Tkinter Structuring")
        self.geometry("700x500")
        self.resizable(True, True)

        # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        # from https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/

        # creating a container
        container = ctk.CTkFrame(self) 
        container.grid(row=0, column=0, sticky="nsew")

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (HomePage, HomePage):
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
            frame.grid_rowconfigure(0, weight = 1)
            frame.grid_columnconfigure(0, weight = 1)
  
        self.show_frame(HomePage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
