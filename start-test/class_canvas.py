import tkinter as tk

color = ['blue', 'red']

class draw_canvas():
    def __init__(self, master):
        self.master = master
        self.cx, self.cy = 500, 400
        self.canvas = tk.Canvas(master, width=self.cx, height=self.cy, bg='gray75')
        self.canvas.pack()

        self.rects([[1,2,3,6,7,8,9,10], 1,[]])

    def rects(self, data):
        number_of_rects = len(data[0])
        margin = (self.cx-self.cx*0.9)/2
        coll_width = (self.cx-margin*2)/number_of_rects
        a = self.cy*0.8/max(data[0])
        print(a)


        for i, j in enumerate(data[0]):
            if i in data[2]:
                self.canvas.create_rectangle(coll_width*i+margin, self.cy*0.9-j*a, coll_width*i+margin+coll_width, self.cy*0.9, fill=color[data[1]])
            else:
                coll=self.canvas.create_rectangle(coll_width*i+margin, self.cy*0.9-j*a, coll_width*i+margin+coll_width, self.cy*0.9, fill='gray75')
