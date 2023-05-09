from time import sleep
from threading import Event, Thread, Lock
from typing import Any

class AnimationThread():
    def __init__(self, CanvasLogic):
        self.CanvasLogic = CanvasLogic
        self.running = Event()
        self.on_page = Event()
        self.app_running = Event()
        Thread(target=self.animate).start()
        self.lock = Lock()

    def start_animation(self):
        self.running.set()

    def stop_animation(self):
        self.running.clear()

    def set_on_page(self):
        self.on_page.set()

    def unset_on_page(self):
        self.on_page.clear()

    def set_speed(self, speed):
        print("before set thread speed", speed)
        with self.lock:
            self.animation_speed = speed
            print("set threat animation speed: ", self.animation_speed)

    def close_thread(self):
        print("closing thread")
        self.app_running.set()
        self.on_page.clear()
        self.running.clear()
        
    def __str__(self) -> str:
        return "AnimationThread"

    def animate(self):
        print("Animation thread started")
        while not self.app_running.is_set():
            while self.on_page.is_set():
                while self.running.is_set():
                    self.CanvasLogic.animation_step_forward()
                    print("Animation step forward")
                    with self.lock:
                        print(self.animation_speed)

                        sleep(self.animation_speed)
                sleep(0.1)
            sleep(0.1)
        print("thread closed")
        return