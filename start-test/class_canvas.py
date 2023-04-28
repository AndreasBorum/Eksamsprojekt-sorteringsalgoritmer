import tkinter as tk

class Canvas_animation():
    def __init__(self, master):
        self.master = master
        self.cx, self.cy = 500, 400
        self.canvas = tk.Canvas(master, width=self.cx, height=self.cy, bg='gray75')
        self.canvas.pack()


    def load_data(self, data_in):
        """
        function to load data on canvas
        :param data: list of numbers to be displayed on canvas
        :return: list of rectangles on canvas
        """
        self.canvas.delete('all')
        self.data = data_in[:]
        number_of_rects = len(self.data)
        self.margin_x = (self.cx*0.1)/2
        
        self.margin_yb = self.cy*0.2
        self.margin_yt = self.cy*0.1
        self.margin_y = self.margin_yb+self.margin_yt
        
        self.a = (self.cy-self.margin_y)/max(self.data)
     

        self.coll_width = (self.cx-self.margin_x*2)/number_of_rects

        self.pos_y = self.cy-self.margin_yb

        self.draw_rects(self.data)

    def pos_x(self, i):
        return self.coll_width*i+self.margin_x

    def hight(self, i):
        return self.cy-self.margin_yb-self.data[i]*self.a



    def draw_rects(self, data):
        """
        function to draw rectangles on canvas
        :param data: list of numbers to be displayed on canvas
        """

        self.columns=[]
        for i, j in enumerate(data):
            column_id = self.canvas.create_rectangle(self.pos_x(i), self.pos_y, self.pos_x(i)+self.coll_width, self.hight(i), fill='gray75', tags=('tag'+str(j)))
            self.canvas.create_text(self.pos_x(i)+self.coll_width/2, self.pos_y-10, text=j, tags=('tag'+str(j)))
            #self.canvas.addtag_withtag("tag5", (column_id, text_id))
            self.columns.append((column_id, "tag"+str(j)))

    
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



class Canvas_animation2(Canvas_animation):
    def __init__(self, master):
        super().__init__(master)
        self.pivot =self.canvas.create_line(0,0,0,0, arrow=tk.LAST)
    
    def move_pivot(self, i):
        """funktion to move arrow/pivot"""
        self.canvas.coords(self.pivot, self.pos_x(i)+self.coll_width/2, self.cy-10, self.pos_x(i)+self.coll_width/2, self.cy-50)
        self.canvas.update()

#https://stackoverflow.com/questions/66918142/another-method-to-move-canvas-objects
def abs_move(self, _object, new_x, new_y):
    # Get the current object position
    x, y, *_ = self.bbox(_object)
    # Move the object
    self.move(_object, new_x-x-1, new_y-y-1)
# Monkey patch the `abs_move` method
tk.Canvas.abs_move = abs_move