from time import sleep
from threading import Event, Thread, Lock


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
        with self.lock:
            self.animation_speed = self.speed_func(speed)

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
                    with self.lock:
                        sleep(self.animation_speed)
                sleep(0.1)
            sleep(0.1)
        print("thread closed")
        return

    def speed_func(self, speed):
        new_speed = 1.09**speed*0.1-(0.1-0.005)
        print(new_speed)
        return new_speed
