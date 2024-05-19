import pyautogui

screen = pyautogui.screenshot()     # 截屏
pyautogui.screenshot('abc.png')     # 截屏 另存为
pyautogui.locateOnScreen('abc.png') # 获取定位