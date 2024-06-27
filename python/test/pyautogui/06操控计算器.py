import pyautogui, os, time

os.system('calc')   # win 打开计算器
time.sleep(2)
keys = ['7', '+', '8', '=']

try: 
    pyautogui.PAUSE = .3
    for k in keys:
        ImgUrl = './imgs/%s.png' % k
        print(ImgUrl)
        # 在屏幕上 定位
        matchBox = pyautogui.locateOnScreen(ImgUrl, confidence=0.8) #  相似度90%  需要install opencv-python
        # 相似度90% 
        # 灰度匹配 降低颜色饱和度 提速30% 可能错误匹配
        boxCenter = pyautogui.center(matchBox)
        print(boxCenter)
        pyautogui.click(boxCenter)
except Exception as e:
    print('not found ',e)