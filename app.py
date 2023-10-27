import math
import time
from threading import Thread

import keyboard  # Importe a biblioteca keyboard em vez de pynput
import pyautogui
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

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

    def on_move(self, e):
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


@app.get("/start_mouse_circle")
async def start_mouse_circle():
    # Use o método hook para monitorar o mouse
    keyboard.hook(mouse_circle.on_move)
    keyboard.unhook_all()  # Certifique-se de remover qualquer gancho de teclado existente

    def run_mouse_circles():
        mouse_circle.move_in_circles()
        keyboard.unhook_all()

    # Inicie o movimento do mouse em círculos em uma thread separada
    mouse_thread = Thread(target=run_mouse_circles)
    mouse_thread.start()

    return "Mouse circles started!"


@app.middleware('http')
async def get_error(request: Request, call_next):
    response = await call_next(request)
    response.headers["referrer-policy"] = "strict-origin-when-cross-origin"

    return response


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
