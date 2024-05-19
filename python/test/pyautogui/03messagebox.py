import pyautogui



# confirm(text='', title='', buttons=['OK', 'Cancel'])
res = pyautogui.confirm('do you want do type password?')
print(res)
if(res == 'Cancel'): 
    # alert(text='', title='', button='OK')
    pyautogui.alert('canceled', '给取消了', '可以吧。。。')
else:
    # password(text='', title='', default='', mask='*')
    password = pyautogui.password('pass world', 'type pass title', mask='--')
    print(password)

# 提示框
# prompt(text='', title='' , default='')
pyautogui.prompt('This lets the user type in a string and press OK.')