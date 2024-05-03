# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：

class Student(object):
    count = 0
    def __init__(self, name) -> None:
         Student.count += 1 # 竟然可以动态修改 class
         self.name = name


# 测试:
if Student.count != 0:
    print('测试失败!1')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!2')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!3')
        else:
            print('Students:', Student.count)
            print('测试通过!')