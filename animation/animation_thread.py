from time import sleep
from threading import Event, Thread, Lock

class AnimationThread():
    def __init__(self, CanvasLogic):
        self.CanvasLogic = CanvasLogic
        self.running = Event()
        self.on_page = Event()
        Thread(target=self.animate).start()

    def start(self):
        self.running.set()

    def stop(self):
        self.running.clear()
        

    def animate(self):
        print("Animation thread started")
        while self.on_page.is_set():
            while self.running.is_set():
                self.CanvasLogic.animation_step_forward()
                print("Animation step forward")
                sleep(1)
            sleep(0.1)