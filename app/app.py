import math
import time
from threading import Thread

import pyautogui
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from pynput import mouse

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class MouseCircle:
    def __init__(self):
        self.mouse_moved = False

    def on_move(self, x, y):
        self.mouse_moved = True

    def move_in_circles(self):
        screen_width, screen_height = pyautogui.size()
        total_time = 30
        start_time = time.time()
        radius = 100
        while (time.time() - start_time) < total_time and not self.mouse_moved:
            angle = (time.time() - start_time) * 2 * math.pi
            x = int(screen_width / 2 + radius * math.cos(angle))
            y = int(screen_height / 2 + radius * math.sin(angle))
            pyautogui.moveTo(x, y)
            time.sleep(0.1)


mouse_circle = MouseCircle()


@app.get("/health")
def get_health():

    return status.HTTP_200_OK


@app.get("/start_mouse_circle")
async def start_mouse_circle():
    mouse_listener = mouse.Listener(on_move=mouse_circle.on_move)
    mouse_listener.start()

    def run_mouse_circles():
        mouse_circle.move_in_circles()
        mouse_listener.stop()

    # Start moving the mouse in circles in a separate thread
    mouse_thread = Thread(target=run_mouse_circles)
    mouse_thread.start()

    return "Mouse circles started!"


@app.middleware('http')
async def get_error(request: Request, call_next):
    response = await call_next(request)
    response.headers["referrer-policy"] = "strict-origin-when-cross-origin"

    return response
