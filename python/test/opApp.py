import subprocess
import pyautogui
import time

subprocess.Popen('notepad.exe')

time.sleep(5)

# 在记事本中输入文本
pyautogui.write('Hello, world!', interval=0.25)
