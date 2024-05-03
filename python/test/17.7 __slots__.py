

from types import MethodType


class Student():
    name = 'new boy'
    pass

Student.sayHi = lambda self: print('hello world', self) 
# 动态添加类属性方法， 所有实例得到这个方法

def sing(self): print("%s lalala" % self.name)

s1 = Student()

# MethodType(fun, 实例)   给方法 绑定 实例，获得 self
s1.sing = MethodType(sing, s1)

s2 = Student()
s1.sayHi()
s2.sayHi()
s1.sing()
# s2.sing() # s2 未绑定 sing
    

class Obj():
    __slots__=('name', 'age')   # 可以拓展的 属性方法名

obj = Obj()
obj.name = 'weibin'
obj.gender = 'male' # error has no attribute 'gender'