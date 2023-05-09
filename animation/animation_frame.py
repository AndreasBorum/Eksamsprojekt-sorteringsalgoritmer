import customtkinter as ctk
import  tkinter as tk
import style
from animation.canvas_animation import CanvasAnimation

class AnimationFrame(tk.Frame):
    def __init__(self, parent, sorting_type):
        super().__init__(parent, highlightbackground="blue", highlightthickness=2)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.animation_state = False
        self.animation_play_state = False

        self.canvas=sorting_type(self)
        self.canvas.grid(row=0, column=0, pady=10, columnspan=2, padx=10, sticky="nsew")

        self.start_frame = tk.Frame(self, highlightbackground="blue", highlightthickness=2)
        self.start_frame.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")

        self.start_btn = ctk.CTkButton(self.start_frame, text="Start", command=self.start_stop_animation)
        self.start_btn.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        self.start_slider = ctk.CTkSlider(self.start_frame, from_=4, to=30, command=self.update_canavs_start_culumns)
        self.start_slider.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")        


        self.play_frame = tk.Frame(self, highlightbackground="blue", highlightthickness=2)
        self.play_frame.grid(row=1, column=1, pady=10, padx=10, sticky="nsew")

        self.switch_var = ctk.StringVar(value="on")
        self.play_switch = ctk.CTkSwitch(self.play_frame, text="Play", command=self.play_pause_animation, variable=self.switch_var, onvalue="on", offvalue="off")
        self.play_switch.deselect()
        self.play_switch.grid(row=0, column=0, pady=10, columnspan=2, padx=10, sticky="nsew")

        self.animation_speed_slider = ctk.CTkSlider(self.play_frame, from_=0.01, to=2, number_of_steps=100, command=self.animation_speed)
        self.animation_speed_slider.grid(row=1, column=0, pady=10, columnspan=2,padx=10, sticky="nsew")

        self.animation_step_forward_btn = ctk.CTkButton(self.play_frame, text="Step Forward", command=self.animation_step_forward)
        self.animation_step_forward_btn.grid(row=2, column=0, pady=10, padx=10, sticky="nsew")

        self.animation_step_back_btn = ctk.CTkButton(self.play_frame, text="Step Back", command=self.animation_step_back)
        self.animation_step_back_btn.grid(row=2, column=1, pady=10, padx=10, sticky="nsew")

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
            self.play_switch.configure(state="disabled")
            self.animation_speed_slider.configure(state="disabled")
            self.animation_step_forward_btn.configure(state="disabled")
            self.animation_step_back_btn.configure(state="disabled")

            self.update_canavs_start_culumns(self.start_slider.get())

        elif not self.animation_state:
            self.animation_state = True
            self.start_btn.configure(text="Stop")
            self.start_slider.configure(state="disabled")
            self.play_switch.configure(state="normal")
            self.animation_speed_slider.configure(state="normal")
            self.animation_step_forward_btn.configure(state="normal")
            self.animation_step_back_btn.configure(state="normal")

            self.canvas.generate_data(round(self.start_slider.get()))

            if self.animation_play_state:
                self.animation_play_state = False
                self.play_pause_animation()


    def update_canavs_start_culumns(self, value):
        self.canvas.update_start_columns(round(value))

    def play_pause_animation(self):
        if self.switch_var.get() == "on":
            self.play_switch.configure(text="Pause")
            self.animation_play_state = True
            self.animation_step_forward_btn.configure(state="disabled")
            self.animation_step_back_btn.configure(state="disabled")
            self.canvas.play_pause_animation(self.animation_speed_slider.get())
        else:
            self.play_switch.configure(text="Play")
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

    