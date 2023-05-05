from animation.canvas_logic import CanvasLogic
from algorithms import bobble_sort


class BubbleSortLogic(CanvasLogic):
    def __init__(self) -> None:
        super().__init__()
    
    def generate_data(self, size):
        """called when start btn is clicked. takes the number of columns and calls the algorithm."""
        data= bobble_sort(size)
        print(data)
        print(size)

        self.draw_columns_after_start(data[0])
        self.import_instruction_steps(data[1])

    def animation_extra_step_back(self):
        pass

    def animation_extra_step_forward(self):
        pass
