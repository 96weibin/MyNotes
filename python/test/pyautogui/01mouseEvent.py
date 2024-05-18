import pyautogui

# pyautogui.PAUSE = 2.5           # 保险措施每次调用暂停2.5s
pyautogui.FAILSAFE = True

mousPos = pyautogui.position() # 获取鼠标坐标
screenSize = pyautogui.size()    # 屏幕区域大小

print(mousPos, screenSize)  #Point(x=1813, y=2317)



# 鼠标功能

# 鼠标移动
pyautogui.moveTo(200, 200, 2)   # 移动到200 200
pyautogui.moveRel(200, -200, 2)  # 相对于当前鼠标位置继续移动 200 200


# 拖动
pyautogui.drag(200, 200, 2)     # 拖动到 200 200
pyautogui.dragRel(200, -200, 2) # 相对于当前鼠标位置继续拖动 200 -200

# 点击
# pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
pyautogui.click(500, 10, 2, .1, button='left')   # 500, 10 点击两次， 间隔.1秒

pyautogui.mouseDown(100,100)
pyautogui.mouseUp(100, 100)
pyautogui.rightClick(100,100)
pyautogui.middleClick(100, 100)
pyautogui.doubleClick(100, 100)
pyautogui.tripleClick(100, 100)


