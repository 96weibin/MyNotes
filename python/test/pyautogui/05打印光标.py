import pyautogui, time, sys

print("press Ctrl-c to quit")
try:
    while True:
        x, y = pyautogui.position()
        print("x: %d, y: %d" % (x, y))
        time.sleep(1)

except Exception as e:
    print('\n')



    