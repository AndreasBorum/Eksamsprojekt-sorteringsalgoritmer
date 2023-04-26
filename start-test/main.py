import tkinter as tk
import class_canvas


class App(tk.Tk):
    """the tkinter class where the GUI runs"""
    def __init__(self):
        super().__init__()

        ## Setting up Initial Things
        self.title("Sample Tkinter Structuring")
        self.geometry("700x700")
        self.resizable(True, True)

        self.canvas = class_canvas.Canvas_animation2(self) 
        self.bind('<Button-1>', self.on_clik)
        self.temp =0 

        self.commands = ([0,[1,3,4,6,7,9]],[1,1,2],[2,1,2],[3,1,2])

    def on_clik(self,event):
        """compare two random collums on canvas on clickevent"""
        print("clicked")
        print(self.commands[0][1])
        if self.commands[self.temp][0] == 0:
            self.canvas.load_data(self.commands[self.temp][1])
        elif self.commands[self.temp][0] == 1:
            self.canvas.compare(self.commands[self.temp][1],self.commands[self.temp][2])
        elif self.commands[self.temp][0] == 2:
            self.canvas.before_swap(self.commands[self.temp][1],self.commands[self.temp][2])
        elif  self.commands[self.temp][0] == 3:
            self.canvas.after_swap(self.commands[self.temp][1],self.commands[self.temp][2])
        self.temp +=1
        if self.temp == len(self.commands):
            self.temp = 0




if __name__ == "__main__":
    app = App()
    app.mainloop()
