from animation.canvas_animation  import CanvasAnimation
from animation.bubble_sort_logic import BubbleSortLogic

class BubbleSort(BubbleSortLogic, CanvasAnimation):
    def __init__(self, master):
        CanvasAnimation.__init__(self, master)
