from abc import ABC, abstractmethod


class CanvasLogic(ABC):

    def update_start_columns(self, columns):
        """called before the data is generated, to preview columns on the canvas"""
        self.start_columns = columns
        self.draw_columns_defore_start(self.start_columns)

    def play_pause_animation(self, speed):
        """called when play/pause  btn is clicked. plays/pauses the animation"""
        if self.animation_running:
            print("stops thread")
            self.animation_thread.stop_animation()
            self.animation_running = False
        elif not self.animation_running:
            print("starts thread")
            self.animation_thread.start_animation()
            self.animation_running = True

        self.animation_thread.set_speed(speed)

    def set_animation_speed(self, speed):
        """called when the animation speed is changed. Changes the animation speed"""
        self.animation_thread.set_speed(speed)

    def animation_step_forward(self):
        """moves the animation forward one step"""
        self.step_counter += 1

        if self.step_counter == len(self.instruction_steps):
            self.step_counter -= 1
            return

        match self.instruction_steps[self.step_counter]:
            case [0, x, y]:
                self.clear_color()
                self.compare(x, y)
            case [1, x, y]:
                self.clear_color()
                self.before_swap(x, y)
            case [2, x, y]:
                self.swap(x, y)
                self.after_swap(x, y)
            case [3]:
                self.done()
            case _:
                self.animation_extra_step_forward(
                    self.instruction_steps[self.step_counter])

    def animation_step_back(self):
        """moves the animation back one step"""
        self.step_counter -= 1

        if self.step_counter == -1:
            self.clear_color()
            return
        elif self.step_counter < -1:
            self.step_counter = -1
            return

        match self.instruction_steps[self.step_counter]:
            case [0, x, y]:
                self.clear_color()
                self.compare(x, y)
            case [1, x, y]:
                self.swap(x, y)
                self.before_swap(x, y)
            case [2, x, y]:
                self.clear_color()
                self.after_swap(x, y)
            case _:
                self.animation_extra_step_back(
                    self.instruction_steps[self.step_counter])

    def unpack_instruction_steps(self, steps):
        """Imports the instruction steps"""
        self.instruction_steps = []
        for step in steps:
            if step[0] == 1:
                self.instruction_steps.extend([step, [2, step[1], step[2]]])
            else:
                self.instruction_steps.append(step)

        self.step_counter = -1
        self.animation_state = False

    def generate_data_from_algorithm(self, algorithm, size):
        """called when start btn is clicked. takes the number of columns and calls the algorithm."""
        self.data1 = algorithm(size)
        # print(self.data)
        self.draw_data()

    def draw_data(self):
        self.draw_columns_after_start(self.data1[0])
        self.unpack_instruction_steps(self.data1[1])

    # ----------------- abstract methods -----------------

    @abstractmethod
    def animation_extra_step_back(self, step):
        pass

    @abstractmethod
    def animation_extra_step_forward(self, step):
        pass

    @abstractmethod
    def generate_data(self, size):
        """function to generate the data"""
        pass

    @abstractmethod
    def draw_columns_defore_start(self, columns):
        pass

    @abstractmethod
    def draw_columns_after_start(self, data):
        pass

    @abstractmethod
    def compare(self, i1, i2):
        """function to highlight the rectangles that are being compared"""
        pass

    @abstractmethod
    def before_swap(self, i1, i2):
        """function to swap the rectangles that are being compared"""
        pass

    @abstractmethod
    def swap(self, i1, i2):
        """function to swap the rectangles"""
        pass

    @abstractmethod
    def after_swap(self, i1, i2):
        """function to swap the rectangles"""
        pass

    @abstractmethod
    def clear_color(self):
        """function to clear the color of all rectangles"""
        pass

    @abstractmethod
    def done(self):
        """function to set the color of all rectangles to green"""
        pass
