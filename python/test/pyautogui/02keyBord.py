import pyautogui

# 键盘输入
pyautogui.PAUSE = 2
pyautogui.typewrite('hello world', interval=0.4)    # 键盘输入一段话 间隔0.4
pyautogui.typewrite(['a', 'b', '8', 'backspace', 'c', 'enter'], .3)   # 间隔。3 依次按下按键

# 组合键
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'x')
pyautogui.hotkey('ctrl', 'shift', 'p')

# 也可以拆分别为 keyup keydown