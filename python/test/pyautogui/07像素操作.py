import pyautogui

screen = pyautogui.screenshot()
pix = screen.getpixel((100,700))    # 获取像素 rgb
print(pix)

isRed = pyautogui.pixelMatchesColor(300,400, (0, 100, 0))
print(isRed)