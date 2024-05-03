__author__ = 'weibin'

class Animal():
    x = 123
    def __init__(self) -> None:
        pass
    def sing(self):
        print('animal sing xxxx')

a1 = Animal()
print(dir(Animal))
print(dir(a1))
print(dir('123'))
print(dir(123))     

# dir 查看 对象的属性， 可见 万物皆对象

print(hasattr(a1, "x"))     # true
print(hasattr(Animal, "x")) # true

# 可见 对象 和 实例都拥有相同的 属性

print(hasattr(a1, 'y'))     # false
setattr(a1, 'y', 'is y')    # 设置属性
print(hasattr(a1, 'y'))     # true
print(getattr(a1, 'y', 'yyy'))     # default 'yyy'


