# list
classmates = ['weibin', 'bob', 'henry']
classmates.append(1)
print(classmates, classmates[-1], len(classmates))
classmates.pop()
classmates.clear()
classmates.copy()
classmates.extend(['mengling', 'cairy', 112])
classmates.index(112) # find index 不转换类型
classmates.remove(112)
classmates.reverse()
classmates.sort()
classmates.insert(1, 'bob')

# tuple 元组一旦初始化不能修改

onT = (1,)  # 只包含一个 需要 逗号
montons = ('xiamlaya', 'qiaogeli') # 无法修改
hoby = ('游泳', ["篮球", "羽毛球"], " 田径")
hoby[1][1] = '乒乓球'
# 嵌套 引用类型 即可修改 引用类型的 属性



