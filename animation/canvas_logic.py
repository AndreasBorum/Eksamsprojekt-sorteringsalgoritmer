from abc import ABC, abstractmethod
import time


class CanvasLogic(ABC):

    def update_start_columns(self, columns):
        """called before the data is generated, to preview columns on the canvas"""
        self.start_columns = columns
        self.draw_columns_defore_start(self.start_columns)

    def play_pause_animation(self, speed):
        """called when play/pause  btn is clicked. plays/pauses the animation"""
        for i in range(10):
            self.animation_step_forward()


    def animation_speed(self, speed):
        """called when the animation speed is changed. Changes the animation speed"""
        pass

    def animation_step_forward(self):
        """called when the step forward btn is clicked. moves the animation forward one step"""
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
        """called when the step back btn is clicked. moves the animation back one step"""
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
        self.animation_state =False

    def generate_data_from_algorithm(self, algorithm, size):
        """called when start btn is clicked. takes the number of columns and calls the algorithm."""
        data = algorithm(size)
        self.draw_columns_after_start(data[0])
        self.unpack_instruction_steps(data[1])

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
