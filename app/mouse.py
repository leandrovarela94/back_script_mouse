import math
import time

import pyautogui
from pynput import mouse

# Global variable to track mouse movement
mouse_moved = False


def on_move(x, y):
    global mouse_moved
    mouse_moved = True


def move_mouse_in_circles():
    # Get the screen width and height to stay within the screen boundaries
    screen_width, screen_height = pyautogui.size()

    # Total time in seconds to run the loop
    total_time = 30

    start_time = time.time()
    radius = 100  # Adjust the radius of the circle as needed
    while (time.time() - start_time) < total_time and not mouse_moved:
        # Calculate the new mouse cursor position to move in a circle
        angle = (time.time() - start_time) * 2 * \
            math.pi  # Varies from 0 to 2*pi over time
        x = int(screen_width / 2 + radius * math.cos(angle))
        y = int(screen_height / 2 + radius * math.sin(angle))

        pyautogui.moveTo(x, y)
        time.sleep(0.1)  # Adjust the sleep time as needed to control the speed


if __name__ == '__main__':
    # Start monitoring mouse movements
    mouse_listener = mouse.Listener(on_move=on_move)
    mouse_listener.start()

    # Run the mouse movement loop
    move_mouse_in_circles()

    # Stop the mouse movement loop if the mouse is moved
    if mouse_moved:
        mouse_listener.stop()
