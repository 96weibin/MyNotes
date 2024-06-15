import logging
import pyautogui, os, time

os.system('calc')   # win 打开计算器
current_dir = os.getcwd()
print(current_dir)
time.sleep(2)

keys = ['7', '+', '8', '=']

try: 
    pyautogui.PAUSE = .3
    for k in keys:
        ImgUrl = '%s/imgs/%s.png' % (current_dir, k)
        print(ImgUrl)
        # 在屏幕上 定位
        matchBox = pyautogui.locateOnScreen(ImgUrl, confidence=0.9, region=(0,0, 2000, 1800), grayscale=True) #  相似度90%  需要install opencv-python
        # 相似度90% 
        # 灰度匹配 降低颜色饱和度 提速30% 可能错误匹配
        boxCenter = pyautogui.center(matchBox)
        pyautogui.click(boxCenter)
except Exception as e:
    logging.exception(' 错误 %s', e) 
    print('not found ',e)