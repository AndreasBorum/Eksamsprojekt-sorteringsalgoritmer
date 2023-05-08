from animation.canvas_logic import CanvasLogic
from algorithms import quick_sort


class QuickSortLogic(CanvasLogic):
    def __init__(self) -> None:
        super().__init__()
    
    def generate_data(self, size):
        """called when start btn is clicked. takes the number of columns and calls the algorithm."""
        self.generate_data_from_algorithm(quick_sort, size)

    def animation_extra_step_back(self):
        pass

    def animation_extra_step_forward(self):
        pass
