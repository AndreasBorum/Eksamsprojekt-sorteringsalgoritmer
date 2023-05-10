import tkinter as tk

from animation.canvas_logic import CanvasLogic
from animation.animation_thread import  AnimationThread


class CanvasAnimation(tk.Frame, CanvasLogic):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.cx, self.cy = 500, 400
        self.canvas = tk.Canvas(self, width=self.cx, height=self.cy, bg='yellow')
        self.canvas.pack()


        self.margin_x = (self.cx*0.1)/2
        
        self.margin_yb = self.cy*0.2
        self.margin_yt = self.cy*0.1
        self.margin_y = self.margin_yb+self.margin_yt
     
        self.pos_y = self.cy-self.margin_yb


        self.animation_thread = AnimationThread(self)
        self.animation_running = False

    #------------------------------------------------------------------------------------------

    def draw_columns_defore_start(self, columns):
        """draws columns on the canvas"""
        self.canvas.delete("all")


        self.column_amount = columns
        self.coll_width = (self.cx-self.margin_x*2)/columns
        self.a = (self.cy-self.margin_y)/columns


        for i in range(1, self.column_amount+1):
            
            def pos_x(i):
                return self.coll_width*(i-1)+self.margin_x
            def hight(i):
                return self.cy-self.margin_yb-i*self.a
            
            self.canvas.create_rectangle(pos_x(i), self.pos_y, pos_x(i)+self.coll_width, hight(i), fill='gray75')
            self.canvas.create_text(pos_x(i)+self.coll_width/2, self.pos_y-10, text=i)

        

    def draw_columns_after_start(self, data):
        """draws columns on the canvas"""
        self.canvas.delete("all")
        self.data = data[:]

        self.columns=[]


        self.column_amount = len(data)
        self.coll_width = (self.cx-self.margin_x*2)/self.column_amount
        self.a = (self.cy-self.margin_y)/max(data)

            
        for i, j in enumerate(data):
            column_id = self.canvas.create_rectangle(self.pos_x(i), self.pos_y, self.pos_x(i)+self.coll_width, self.hight(i), fill='gray75', tags=('tag'+str(j)))
            self.canvas.create_text(self.pos_x(i)+self.coll_width/2, self.pos_y-10, text=j, tags=('tag'+str(j)))
            #self.canvas.addtag_withtag("tag5", (column_id, text_id))
            self.columns.append((column_id, "tag"+str(j)))

    def pos_x(self, i):
        return self.coll_width*i+self.margin_x
    def hight(self, i):
        return self.cy-self.margin_yb-self.data[i]*self.a


    def compare(self, i1, i2):
        """function to highlight the rectangles that are being compared"""
        self.canvas.itemconfig(self.columns[i1][0], fill='gray50')
        self.canvas.itemconfig(self.columns[i2][0], fill='gray50')

    def before_swap(self, i1, i2):
        """function to swap the rectangles that are being compared"""
        self.canvas.itemconfig(self.columns[i1][0], fill='red')
        self.canvas.itemconfig(self.columns[i2][0], fill='blue')

    def swap(self, i1, i2):
        """function to swap the rectangles"""
        self.canvas.abs_move(self.columns[i1][1], self.pos_x(i2), self.hight(i1))
        self.canvas.abs_move(self.columns[i2][1], self.pos_x(i1), self.hight(i2))
        self.columns[i1], self.columns[i2] = self.columns[i2], self.columns[i1]
        self.data[i1], self.data[i2] = self.data[i2], self.data[i1]


    def after_swap(self, i1, i2):
        """function to swap the rectangles"""
        self.canvas.itemconfig(self.columns[i1][0], fill='blue')
        self.canvas.itemconfig(self.columns[i2][0], fill='red')


    def clear_color(self):
        """function to clear the color of all rectangles"""
        for i in self.columns:
            self.canvas.itemconfig(i[0], fill='gray75')

    def done(self):
        """function to set the color of all rectangles to green"""
        for i in self.columns:
            self.canvas.itemconfig(i[0], fill='green')
        if self.master.animation_play_state:
                self.master.play_pause_animation()

#https://stackoverflow.com/questions/66918142/another-method-to-move-canvas-objects
def abs_move(self, _object, new_x, new_y):
    # Get the current object position
    x, y, *_ = self.bbox(_object)
    # Move the object
    self.move(_object, new_x-x-1, new_y-y-1)
# Monkey patch the `abs_move` method
tk.Canvas.abs_move = abs_move