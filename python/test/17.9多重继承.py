class Animal:
    def run(self):
        print('I can run')
    pass


class Bird(object):
    def fly(self):
        print('%s I can fly' % self.__dir__.__name__ )
    pass


class MaqueFactory(Animal, Bird):   # 同时继承了  两个类  
    pass

maque1 = MaqueFactory()
maque1.fly()    
maque1.run()