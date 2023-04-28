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
        self.bind('<Button-1>', self.left_clik)
        self.bind('<Button-3>', self.right_clik)
        self.temp =-1 

        self.commands = ([0,[1,3,2,4]],[1,0,1],[1,1,2],[2,1,2],[3,1,2],[4])

    def left_clik(self,event):
        """
        This function is called when the left mouse button is clicked
        """

        self.temp +=1
        if self.temp == len(self.commands):
            self.temp = 0

        match self.commands[self.temp]:
            case [0,x]:
                self.canvas.load_data(x)
            case [1,x,y]:
                self.canvas.clear_color()
                self.canvas.compare(x,y)
            case [2,x,y]:
                self.canvas.clear_color()
                self.canvas.before_swap(x,y)
            case [3,x,y]:
                self.canvas.swap(x,y)
                self.canvas.after_swap(x,y)
            case [4]:
                self.canvas.done()

        
    def right_clik(self, event):

        self.temp -=1
        if  self.temp < 0:
            self.temp =0
            return
        
        match self.commands[self.temp]:
            case [0,x]:
                self.canvas.load_data(x)
            case [1,x,y]:
                self.canvas.clear_color()
                self.canvas.compare(x,y)
            case [2,x,y]: 
                self.canvas.swap(x,y)
                self.canvas.before_swap(x,y)
            case [3,x,y]:
                self.canvas.clear_color()
                self.canvas.after_swap(x,y)




if __name__ == "__main__":
    app = App()
    app.mainloop()
