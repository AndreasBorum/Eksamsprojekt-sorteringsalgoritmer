import tkinter as tk

class CanvasAnimation(tk.Frame):
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


    def update_start_columns(self, columns):
        """called before the data is generated, to preview columns on the canvas"""
        self.start_columns = round(columns)
        self.draw_columns_defore_start(self.start_columns)


    def generate_data(self):
        """called when start btn is clicked. takes the number of columns and calls the algorithm."""
        self.draw_columns_after_start([1,3,5,6,7,3,5,4])
        #self.instruction_steps=[1,1,2]




    def play_pause_animation(self):
        """called when play/pause  btn is clicked. starts/stops the animation"""
        pass

    def animation_speed(self, speed):
        """called when the animation speed is changed. Changes the animation speed"""
        pass

    def animation_step_forward(self):
        """called when the step forward btn is clicked. moves the animation forward one step"""
        pass

    def animation_step_back(self):
        """called when the step back btn is clicked. moves the animation back one step"""
        pass

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

        self.columns=[]


        self.column_amount = len(data)
        self.coll_width = (self.cx-self.margin_x*2)/self.column_amount
        self.a = (self.cy-self.margin_y)/max(data)

       
        def pos_x(i):
            return self.coll_width*i+self.margin_x
        def hight(i):
            return self.cy-self.margin_yb-data[i]*self.a
            
        for i, j in enumerate(data):
            column_id = self.canvas.create_rectangle(pos_x(i), self.pos_y, pos_x(i)+self.coll_width, hight(i), fill='gray75', tags=('tag'+str(j)))
            self.canvas.create_text(pos_x(i)+self.coll_width/2, self.pos_y-10, text=j, tags=('tag'+str(j)))
            #self.canvas.addtag_withtag("tag5", (column_id, text_id))
            self.columns.append((column_id, "tag"+str(j)))