flag1 = True
flag2 = False
str1 = "hello"
num1 = 0
num2 = 1
emp = None  # 控制 None

# 与或非 and or not
print(flag1 and flag2)  
print(flag1 or flag2)
print(not str1)
print(not emp)
print(not num1)
print(not num2)
# 动态语言 弱类型 str => int
if True :
    str1 = 9    
print(type(str1))       