import pyautogui
import time

def send(amount, message):
    for i in range(amount):
        time.sleep(0.2)
        pyautogui.write(message)
        time.sleep(0.060)
        pyautogui.press('enter')