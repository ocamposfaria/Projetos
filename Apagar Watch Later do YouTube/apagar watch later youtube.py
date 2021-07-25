import pyautogui
import time


x = 0

time.sleep(5)

while x != 240:
    pyautogui.moveTo(1845, 365)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(1694, 539)
    pyautogui.click()
    time.sleep(0.5)
    x = x + 1
