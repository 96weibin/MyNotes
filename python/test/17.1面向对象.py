class Student():
    def __init__(self, name, score):  # 初始化函数
        self._name = name
        self.__score = score
    
    def printScore(std):
        print('name %s score: %s' % (std._name, std.__score))

s1 = Student('weibin', 17)  # 构建实例
s1.printScore()
s1._name = 'lulu'
print(s1._name)     # _仍可被 读写

# print(s1.__score)   # __ 不能被访问
s1.__score = 70     # 不推荐

print(s1.__init__)  #内部函数 也可以被调用
