import types

def testFun():
    pass
doubFun = lambda x: x *2
l1 = [1,2,3]
t1 = (1,2,3)
d1 = {'name': "weibin"}
s1 = {1, 3, 'number'}

print(type(True) == bool)
print(type(123) == int)
print(type(3.14) == float)
print(type("123") == str)
print(type(l1) == list)
print(type(t1) == tuple)
print(type(d1) == dict)
print(type(s1) == set)
print(type((2*x for x in range(1,2))) == types.GeneratorType)
print(type(abs) == types.BuiltinFunctionType)
print(type(testFun) == types.FunctionType)
print(type(doubFun) == types.LambdaType)
print(type(None) == types.NoneType)
print('-------------------------')

class Foo():
    pass
class Son(Foo):
    pass

foo = Foo()
son = Son()

print(isinstance(foo, Foo))
print(isinstance(son, Foo))
print(isinstance(foo, (Foo, Son))) # 元祖多个类型