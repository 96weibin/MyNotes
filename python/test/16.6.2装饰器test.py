import logging


def bindable(fun):
    def wrapper(*args):
        print(args)
        print("calling" + fun.__name__)
        return fun(*args)
    return wrapper

class MyClass:
    def __init__(self) -> None:
        self.__myName = 'jjj'
        pass

    @property
    def myName(self):
        return self.__myName
    
    @myName.setter
    def myName(self, val):
        print(val)
        self.__myName = val
    
    @bindable
    def printSayHi(self):
        print("printSayHi" + self.myName)


mc = MyClass()
mc.myName = "邯郸"
mc.printSayHi()

