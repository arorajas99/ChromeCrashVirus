import time
import pyautogui
pyautogui.hotkey('win','s')
time.sleep(1)
pyautogui.hotkey('c','h','r','o','m','e')
time.sleep(1)
pyautogui.hotkey('enter')
time.sleep(5)

def crash():
    for i in range (0,100):
    pyautogui.hotkey('ctrl','t')
    for i in range (0,100):
    pyautogui.hotkey('ctrl','n')
for i in range(100):
    crash()
