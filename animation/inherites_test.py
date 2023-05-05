from abc import ABC, abstractmethod

class CanvasLogic(ABC):
    def draw_column(self):
        print('draw column from CanvasLogic')
        self.draw_column_on_canvas()
        self.extra()

    @abstractmethod
    def draw_column_on_canvas(self):
        pass

    @abstractmethod
    def extra(self):
        pass


class BubbleLogic(CanvasLogic):
    def draw_bubble(self):
        print('draw bubble from BubbleLogic')
        self.draw_bubble_on_canvas()

    def extra(self):
        print('extra from BubbleLogic')

    @abstractmethod
    def draw_bubble_on_canvas(self):
        pass

class CancasAnimation(CanvasLogic):
    def draw_column_on_canvas(self):
        print('drawing column from CanvasAnimation')


class BubbleSort(BubbleLogic, CancasAnimation):
    def draw_bubble_on_canvas(self):
        print('drawing bubble from BubbleSort')


b= BubbleSort()

b.draw_bubble()
b.draw_column()