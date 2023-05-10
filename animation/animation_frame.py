import customtkinter as ctk
import  tkinter as tk
import style
from animation.canvas_animation import CanvasAnimation

class AnimationFrame(tk.Frame):
    def __init__(self, parent, sorting_type):
        super().__init__(parent)
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0), weight=1)

        self.animation_state = False
        self.animation_play_state = False

        self.canvas=sorting_type(self)
        self.canvas.grid(row=0, column=0, pady=10, columnspan=2, padx=10, sticky="nsew")


        self.start_frame = ctk.CTkFrame(self)
        self.start_frame.grid(row=1, column=0, pady=10, padx=10, sticky="snew")

        self.start_btn = ctk.CTkButton(self.start_frame, text="Start", command=self.start_stop_animation)
        self.start_btn.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        column_slider_label = ctk.CTkLabel(self.start_frame, text="Number of columns:")
        column_slider_label.grid(row=1, column=0, padx = 10 , pady=(10,0))
        self.start_slider = ctk.CTkSlider(self.start_frame, from_=4, to=30, command=self.update_canavs_start_culumns)
        self.start_slider.grid(row=2, column=0, pady=(0,10), padx=10, sticky="nsew")        


        self.play_frame = ctk.CTkFrame(self)
        self.play_frame.grid(row=1, column=1, pady=10, padx=10, sticky="snew")

        #self.switch_var = ctk.StringVar(value="on")
        #self.play_pause_btn = ctk.CTkSwitch(self.play_frame, text="Play", command=self.play_pause_animation, variable=self.switch_var, onvalue="on", offvalue="off")
        #self.play_pause_btn.deselect()
        #self.play_pause_btn.grid(row=0, column=0, pady=10, columnspan=2, padx=10, sticky="nsew")

        self.play_pause_btn = ctk.CTkButton(self.play_frame, text="Play", command=self.play_pause_animation)
        self.play_pause_btn.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        self.reset_btn = ctk.CTkButton(self.play_frame, text="Reset", command=self.reset)
        self.reset_btn.grid(row=0, column=1, pady=10, padx=10, sticky="e")


        speed_slider_label = ctk.CTkLabel(self.play_frame, text="Animation speed:")
        speed_slider_label.grid(row=1, column=0, padx = 10 , pady=(10,0))
        self.animation_speed_slider = ctk.CTkSlider(self.play_frame, from_=0.01, to=2, number_of_steps=100, command=self.animation_speed)
        self.animation_speed_slider.grid(row=2, column=0, pady=(0,10), columnspan=2,padx=10, sticky="nsew")

        self.animation_step_back_btn = ctk.CTkButton(self.play_frame, text="<-- Step", command=self.animation_step_back)
        self.animation_step_back_btn.grid(row=3, column=0, pady=10, padx=10, sticky="nsew")

        self.animation_step_forward_btn = ctk.CTkButton(self.play_frame, text="Step -->", command=self.animation_step_forward)
        self.animation_step_forward_btn.grid(row=3, column=1, pady=10, padx=10, sticky="nsew")

        for widget in self.play_frame.winfo_children():
            widget.configure(state="disabled")

        self.update_canavs_start_culumns(self.start_slider.get())

    def start_stop_animation(self):
        """called when start stop button is pressed. if amnimation_state is False it will generate data and disable start_slider and enable animation controles. 
        If animation_state is True it will disable animation controles and enable start_slider. 
        Also changes the text of start_btn to "Stop" if animation_state is True and vice versa. 
        """
        if self.animation_state:
            self.animation_state = False
            self.start_btn.configure(text="Start")
            self.start_slider.configure(state="normal")
            for widget in self.play_frame.winfo_children():
                widget.configure(state="disabled")

            if self.animation_play_state:
                self.play_pause_animation()

            self.update_canavs_start_culumns(self.start_slider.get())

        elif not self.animation_state:
            self.animation_state = True
            self.start_btn.configure(text="Stop")
            self.start_slider.configure(state="disabled")
            for widget in self.play_frame.winfo_children():
                widget.configure(state="normal")

            if self.animation_play_state:
                self.play_pause_animation()


            self.canvas.generate_data(round(self.start_slider.get()))

            

    def update_canavs_start_culumns(self, value):
        self.canvas.update_start_columns(round(value))

    def play_pause_animation(self):
        if not self.animation_play_state:
            self.play_pause_btn.configure(text="Pause")
            self.animation_play_state = True
            self.animation_step_forward_btn.configure(state="disabled")
            self.animation_step_back_btn.configure(state="disabled")
            self.canvas.play_pause_animation(self.animation_speed_slider.get())
        else:
            self.play_pause_btn.configure(text="Play")
            self.animation_play_state = False
            self.animation_step_forward_btn.configure(state="normal")
            self.animation_step_back_btn.configure(state="normal")
            self.canvas.play_pause_animation(self.animation_speed_slider.get())

    def animation_speed(self, speed):
        self.canvas.set_animation_speed(speed)

    def animation_step_forward(self):
        self.canvas.animation_step_forward()

    def  animation_step_back(self):
        self.canvas.animation_step_back()

    def reset(self):
        if self.animation_play_state:
            self.play_pause_animation()
        self.canvas.draw_data()

    