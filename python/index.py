class Foo:
    'father class'
    __prop = 'wo shi ni die'
    sons = 0
    def __init__(self, msg):
        self.msg = msg
        Foo.sons += 1
        print('''
Foo init 
              my name hhh
        ''')
        pass

    hobys = ['羽毛球', '网球','太极']

    def play(self, hoby): 
        Foo.hobys.append(hoby)

    firstName = 'zhao'
    age = 27
    # def sayName(lastName):
    #     name = firstName + lastName
    #     return name
    def sayhobys(self):
        for hoby in Foo.hobys:
            print(hoby)
    def sayHi(self):
        print('hello ')
    
class Child (Foo):
    
    'child'
    def __init__(self, msg):
        print("child inint", self.__doc__)
        self.sayHi()



# fater = Foo('完美世界')
# fater.play("电子镜子")
# fater.play("摩托")
# fater.sayhobys()
# fater.sayHi()

children = Child('son son sonß')
children.play('玩泥巴')
# fater.sayhobys()
print(children.firstName, children.sons, children.sayhobys())
