class Animal():
    def __init__(self) -> None:
        self.foot = 4

    def sing(std):
        print('animal saying xxxx')

class Dog(Animal):  # 继承
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
    def sing(std):
        print('dog %s sing wangwang' % std.name)

class Bird(Animal):
    def __init__(self, name) -> None:
        self.name = name
        super().__init__()
    def sing(std):
        print('bird %s sing jiujiujiu' % (std.name))

# 多态
a1 = Animal()
a1.sing()

d1 = Dog('mahua')
d1.sing()
print(d1.foot)
print(isinstance(d1, Animal)) # true
b1 = Bird("bag")
b1.sing()