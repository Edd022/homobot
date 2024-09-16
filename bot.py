import pyautogui
import time

time.sleep(5)

pyautogui.moveTo(100, 200)
pyautogui.click()
pyautogui.write('Hola desde Python!', interval=0.1)
