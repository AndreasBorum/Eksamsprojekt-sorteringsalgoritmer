from animation.canvas_animation  import CanvasAnimation
from animation.quick_sort_logic import  QuickSortLogic

class QuickSort(QuickSortLogic, CanvasAnimation):
    def __init__(self, master):
        CanvasAnimation.__init__(self, master)
