
import math
import threading
import time

from pynput.mouse import Controller, Listener


class MouseCircler:
    def __init__(self):
        self.stop_event = threading.Event()
        self.controller = Controller()
        self.listener = Listener()
        self.is_mouse_moving = False
        self.x = 0
        self.y = 0

    def on_move(self, x, y):
        self. listener.start()
        if self.x or self.y != Listener(on_move=(x, y)):
            self.is_mouse_moving = True

    def move_mouse_in_circles(self):
        screen_width = 1920  # Substitua pelo valor correto da largura da sua tela
        screen_height = 1080  # Substitua pelo valor correto da altura da sua tela
        total_time = 5
        start_time = time.time()
        radius = 100

        while (time.time() - start_time) < total_time:
            if self.is_mouse_moving == False:
                angle = (time.time() - start_time) * 2 * math.pi
                x = int(screen_width / 2 + radius * math.cos(angle))
                y = int(screen_height / 2 + radius * math.sin(angle))
                self.controller.position = (x, y)
                time.sleep(0.1)
