import os
import win32api
import pyautogui
import time
from PIL import Image


screenshot_folder = "captures"
os.makedirs(screenshot_folder, exist_ok=True)
cursor_image = Image.open("cursor_image.png")

def capture_screen(interval):
    count = 191
    while True:
        cursor = pyautogui.position()
        mouse_pressed = 1 if win32api.GetKeyState(0x01) < 0 else 0  # if win32api.GetKeyState(0x01) is lower than 0, left button is clicked
        screenshot = pyautogui.screenshot()
        screenshot = screenshot.convert("L")
        screenshot.paste(cursor_image, (cursor.x, cursor.y), cursor_image)  # add a cursor to the image, on the actual position
        screenshot.save(os.path.join(screenshot_folder, f"screenshot_{count}_{mouse_pressed}.png"))
        count += 1
        time.sleep(interval)

capture_screen(0.1)
