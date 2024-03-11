# if else
ages = input("age: ")
age = int(ages)
if age > 18:
    print("hello man")
else:
    print("hello boy")

# 用ifelse 的 三元运算 替代
msg = "hello man" if age > 18 else "hello Boy"
print(msg)