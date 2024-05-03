class Student():
    def __init__(self, name, age, score) -> None:
        self.__name = name 
        self.__age = age
        self.__score = score
    
    def groupup(std):
        std.__age += 1
        print('name %s age %d' % (std.__name, std.__age))

    def get_name(std):
        return std.__name
    
    def set_score(std, age):
        if(age < 0): 
            return "invalid"
        std.__age = age


s1 = Student('weibin', 18, 100)
s1.groupup()
print(s1.get_name())
# print(s1.__name)    __上下划线 不能被访问