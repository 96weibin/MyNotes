# [Python3](https://www.liaoxuefeng.com/wiki/1016959663602400/1017434209254976)

- 解释型语言， 交互式语言， 面向对象
- 缩进 代码块
- 动态语言

## 环境搭建

- macOs 

    ```shell
    $ brew inst

    - read evaluate print loop
    all python
    # 需要安装Homebrew
    ```

## python REPL

## python 基础 Diff


### string

    ```py
    # r'' 不转义
    print(r'不转义 no trans ,,.."""""')

    # ''' pre 
    print('''
            my
        format
            pre
    ''')
    #  格式化
    PI = 3.1415

    str1 = "hello world"
    str2 = 'Hi %s, do you have $%d' % ('weibin', 1000)
    str3 = 'hello {0} and {1:.2f}'.format('xiao ming', 12.345)
    str4 = f'Pi = {PI} about {PI:.2f}'
    ```

### boolean

- and or not

    ```py
    flag1 = True
    flag2 = False
    str1 = "hello"
    num1 = 1
    emp = None  # 空 None

    # 与或非 and or not
    print(flag1 and flag2)  
    print(flag1 or flag2)
    print(not str1)
    print(not emp)

    # 动态语言 弱类型 str => int
    if True :
        str1 = 9    
    print(type(str1))       
    #->False
    #->True
    #->False
    #->True
    #-><class 'int'>
    ```

### List 和 tuple

- [] 数组 () 元组

    ```py
    # list
    classmates = ['weibin', 'bob', 'henry']
    classmates.append(1)
    print(classmates, classmates[-1], len(classmates))
    classmates.pop()
    classmates.clear()
    classmates.copy()
    classmates.extend(['mengling', 'cairy', 112])
    classmates.index(112) # find index 不转换类型
    classmates.remove(112)
    classmates.reverse()
    classmates.sort()
    classmates.insert(1, 'bob')
    
    ood = range(0, 100, 2) 
    listOod = list(ood) # 生成 100以内 偶数list

    # tuple 元组一旦初始化不能修改
    onT = (1,)  # 只包含一个 需要 逗号
    montons = ('xiamlaya', 'qiaogeli') # 无法修改
    hoby = ('游泳', ["篮球", "羽毛球"], " 田径")
    hoby[1][1] = '乒乓球'
    # 嵌套 引用类型 即可修改 引用类型的 属性

    ```

### dict set

- 字典

    ```py
    # dictionary

    d = {'name': 'weibin', 'age': 18}
    d['gender'] = 'male'
    if 'gender' in d:       # key是否存在
        print(d['gender'])

    print(d.get('thomas')) # 不存在 返回 None
    print(d.get('thomas', 'not found')) # 不存在返回 'not found'

    for item in dict.fromkeys(d):
        print(item)
    d.pop('gender')
    print(d.keys())
    print(d.items())
    ```
- set

    ```py
    d1 = {'name': 'weibin', 'age': 18, 'gender': True}
    # 可迭代的对象 list dict tuple
    s1 = set(d1)    # key 的 set
    s1.add('some')
    s1.update(('grid', 'prop'))
    s1.pop()    # 随机删除一位  不知道啥用
    s1.remove('some')   # 不存在则会报错
    s1.discard('some') # 不存在不会报错
    print(s1)
    ```

### 条件判断

- 条件判断
    
    > 三元运算 msg = "true msg" if xxx else "false msg"

    ```py
    # if else
    ages = input("age: ")
    age = int(ages)
    if age > 18:
        print("hello man")
    else:
        print("hello boy")

    # 用ifelse 的 三元运算 替代
    msg = "hello man" if age > 18 else "hello Boy"
    print(msg)
    ```

### 匹配

- match case 

    > 数组 匹配， 或匹配， 条件匹配， 匹配值可做变量， default _

    ```py
    source = input("source: ")
    match source:
        case "A":
            print("hello A")
        case '11' | '12' | '13':    # | 或
            print("hello tean")
        case x if int(x) > 50:      # if 条件
            print("hello old man")
        case _:                     # default
            print('hello any one')                                                         
    ```

    ```py
    args = ['gcc', 'hello.c', 'world.c', 'I','like you']
    # args = ['gcc', 'hello.c']
    # args = ['clean']
    # args = ['clean', 123]     # invalid
    # args = ['gcc']
    match args:
        case ['gcc']:           # 只有 gcc的数组
            print('missing options')
        case ['gcc', file1,  *files]:   # 第一位 gcc, 第二位 作为变量 file1, 多位可选变量作为 files
            print('gcc pompile: ' + file1 + ','  + ','.join(files))
        case ['clean']:
            print("clean")
        case _:
            print('invalid command.')
    ```

### 循环 

- for in

    ```py
    listOod = list(range(0, 100, 2))
    for n in listOod:
        print(n)
    ```

- while

    ```py
    sum = 100
    while sum > 0:
        #dosomething
        sum-=2
        print(sum)
        if sum%3 == 0:
            continue
        if sum < 50:
            break
    print('end')
    ```

## 函数

- 常用内置函数

    函数 | 功能 | exmple
    -|-|-
    int | 类 | int("123")
    float | 型 | float("123.34")
    str | 转 | str(True)
    bool | 换 | bool(0)
    len | 长度 | len(obj)
    type | 查询类型 | type(123)
    help | 查看帮助 | help(abs)
    abs | 绝对值 |
    mas | 
    min | 
    sum | 


- 自定义函数

    ```py
    import random
    from typing import Union

    # 自定义函数  函数约束（非强制）
    def my_abs(x: float, format: bool = True) -> Union[int, float]: 
        x = x if x >= 0 else -x
        if format:
            return int(x)
        return x

    print(my_abs(-random.random() * 100, False))

    # 自定义空函数
    def emp_fun():
        pass
    ```

- 求斐波那契数列第n项（递归）

    ```py
    # 0, 1, 1, 2, 3, 5, 8

    def fibonacci(n : int) -> int:
        if n < 0:
            return 'please type pos int' 
        elif n == 0:
            return 0
        elif n == 1: 
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n-2)

    print(fibonacci(7))
    ```

## 高级特性

### 切片

- 操作集合 的快捷方法

    ```py
    L = list(range(100))
    s = "hello wrold"

    # [start : end ?: step]

    l10 = L[:10]   # 0-10
    print(l10)


    ls10 = s[-10:] # 后10
    print(ls10)

    ood10 = L[:10:2] # 0-10 step =2
    print(ood10)

    copys = s[:] # copy
    print(copys)
    ```

    ```py
    def trim(s: str) -> str:
        if s[:1] == ' ':
            return trim(s[1:])
        elif s[-1:] == ' ': 
            return trim(s[:-1])
        else:
            return s
        
    hello = "   hello world    "
    print(trim(hello))
    ```
### 迭代

- for in
- isInstance(xxx, Iterable)
- 可以结构item 


    ```py
    from collections.abc import Iterable

    d1 = {
        'name': 'weibin',
        'age' : 17,
        'gender' : "maile",
        # 'hobys': ('bascateball', 'football')
        }

    if isinstance(d1, Iterable):
        for k in d1 :   # 遍历 key
            print(k)
        for v in d1.values(): 
            print(v)    # 遍历 Val
        for k,v in d1.items(): # 同时遍历 k v
            print(k, v)

    s1 = [(1,1,2), (2,2,3), (3,3,4)]

    if isinstance(s1, Iterable):
        for x, y, z in s1:  # 可以对 item 解构
            print(x, y, z)

    ```
### 列表生成式

- [表达式 for x in list 条件]
    ```py
    # 快速生成 有一定规则的 list
    # [表达式 多个 Iterable condition]

    l1 = [x*x for x in range(1, 10)]
    print(l1) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

    l2 = [x * 2 for x in range(1, 10) if x % 2 == 0] # 有判断条件
    print(l2) # [4, 8, 12, 16]

    l3 = [(a + b).lower() for a in 'XYZ' for b in "ABCD"] # 多个迭代
    print(l3) # ['xa', 'xb', 'xc', 'xd', 'ya', 'yb', 'yc', 'yd', 'za', 'zb', 'zc', 'zd']

    ```

### 生成器

    ```py
    g1 = (2*x for x in range(1, 10))
    next(g1)
    ```


## 函数式编程

-  高阶函数

    ```py
    # map

    from functools import reduce

    def f(x: int) -> int:
        return x * x

    m1: map = map(f, range(1,10))
    print(m1)
    l1: list = list(m1)
    print(l1)
    # <map object at 0x000001995BE7B550>
    # [1, 4, 9, 16, 25, 36, 49, 64, 81]

    # reduce

    def f2 (t, s) -> bool:
        return str(t) + str(s)
    c1 = reduce(f2, l1, "")
    print(c1)  # 149162536496481

    # filter
    def isOdd(n):
        return n % 2 == 0
    f2 = filter(isOdd, l1)
    print(list(f2))     # [4, 16, 36, 64]
        
    # sorted
    l2 = [-19,8,12,7, -8,2,12]
    s2 = sorted(l2, key=abs, reverse= True)
    print(list(s2))
    ```

- 闭包
    
    > 函数1 返回 函数2执行， 函数2的执行 返回 函数1的值
    ```py
    def count():
        fs = []
        for i in range(1,4):
            def f():
                return 2 * i
            fs.append(f)
        return fs

    fs1, fs2, fs3 = count()
    print(fs1(), fs2(), fs3())  # 6 6 6 


    def closure_count():
        fs = []
        for i in range(1,4):
            def f(j):
                def doubleF():
                    return j * j
                return doubleF
            fs.append(f(i))
        return fs

    fs1, fs2, fs3 = closure_count()
    print(fs1(), fs2(), fs3()) #1 4 9



    def closure_count_shot():
        def f(i):
            return lambda  : i * i
        return map(f, range(1,4))

    fss1, fss2, fss3 = closure_count_shot()
    print(fss1(), fss2(), fss3())  # 1 4 9

    ```

- 匿名函数

    ```py
    getValue = lambda x, y: x + y       # 多个行参用 ， 分割

    print(getValue(1,2))
    ```

- 装饰器
    - @xxx 
    - 调用 装饰器装饰的函数， 会先执行 装饰器， 将装饰函数 作为参数传入
    - [三层装饰](./test/16.6装饰器.py)

    ```py
    # 2 层 Decorator
    def logD (func) :
        def wrapper(*args, **kw):
            print(args, kw)
            print("calling " + func.__name__)
            return func(*args, **kw)
        return wrapper


    @logD
    def sayHi(where):
        print('hello' + where)

    sayHi('beijing')
    ```

## 模块

### 自定义模块 
- 标准自定义模块

    ```py
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    ' a test module '
    __author__ = 'Weibin Zhao'

    import sys

    def test():
        args = sys.argv
        if len(args)==1:
            print('Hello, world!')
        elif len(args)==2:
            print('Hello, %s!' % args[1])
        else:
            print('Too many arguments!')

    if __name__=='__main__':
        test()
    ```
    - 不需要写 export
    - python 没有强制 private 只是变量名规范
    - xxx 表示public
    - _xxx 表示   私有
    - \__xxx__ 表示 特殊 


### 第三方模块

- 安装方式 

    1. [pip](https://pypi.org/) 查找安装
        ```shell
        $ pip3 install Pillow
        ```
    2. [Anaconda](https://www.anaconda.com/) 集成
    
#### Pillow

Todo

## 面向对象

- \__init__(self, *args)

    ```py
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

    ```

### 访问权限

 - _ __ private
    - get_xxx 读取内部变量
    _ set_xxx 过滤更新

    ```py
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
    ```

### 继承多态

- 括号继承

    ```py
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
    ```

### 类型判断

- type() types 

    ```py
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
    ```

- instance 

    ```py
    class Foo():
        pass
    class Son(Foo):
        pass

    foo = Foo()
    son = Son()

    print(isinstance(foo, Foo))
    print(isinstance(son, Foo))
    print(isinstance(foo, (Foo, Son))) # 元祖多个类型
    ```

### [属性操作](./test/17.5属性操作.py)

- 万物皆对象
    - dir
    - hasattr , getattr, setattr

    ```py
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

    ```

### [类与实例的属性](./test/17.6类属性和实例属性.py)

- 可以动态修改类的属性

    ```py
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
    ```
### 面向对象高级

- 动态给类，实例 设置方法
    - MethodType - 实例方法
    ```py
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
    ```

- \__sloat__

    - 规定可拓展属性名

    ```py
    class Obj():
        __slots__=('name', 'age')   # 可以拓展的 属性方法名

    obj = Obj()
    obj.name = 'weibin'
    obj.gender = 'male' # error has no attribute 'gender'
    ```

- @property

    - getter setter 的简写

    ```py
    class Student():
        _scores = 0
        def __init__(self, name) -> None:
            self.name = name
        @property
        def scores(self):
            return self._scores

        @scores.setter
        def scores(self, value):
            if value > 100 or value < 0:
                raise ValueError('error score')
            else:
                self._scores = value

    xiaoming = Student('xiaoming1')
    print(xiaoming.scores)
    xiaoming.scores = 99
    print(xiaoming.scores)
    xiaoming.scores = 101
    ```

    - 多重继承 mixin

    ```py
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
    ```

    - 定制类 TODO

    - 枚举类

    ```py

    # 默认
    from enum import Enum

    status = Enum('status123', ('success', 'fild', 'pandding'))

    print(status.success.value)     # 1
    print(status.success.name)      # success
    print(status(1))                # status.success
    
    # 对应特殊值
    @unique         # 检查 名字唯一
    class Weekday(Enum):
        Mon = 1
        Tue = 2
        Wed = 3
        Thu = 4
        Fri = '周五'
        Sat = 6
        Sun = 7
        pass

    print(Weekday.Fri.name)     # Fri
    print(Weekday.Fri.value)    # '周五'

    ```

    - 元组类

    TODO

## Test & Debug

### [Exception](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)

> BasBaseExceptione 所有异常的基类

- 捕获异常

    ```py
    import logging


    def div10(n):
        return 10 / n

    def doubleN(n):
        return div10(n) * 2

    def main(n):
        return doubleN(n)

    try: 
        main(0)
    except ZeroDivisionError as e:
        logging.exception('ZeroDivisionError 错误 %s', e)  # ZeroDivisionError 错误 division by zero
    except BaseException as e:
        logging.exception('base 错误')
    finally:
        print('--------------finally a error logging------------split----------')


    print('End')        # try 捕获异常后 继续执行`

    ```

- 抛出异常

    ```py
    raise 'unexpected 自定义的异常'
    ```




### Debug

- print, **logging**, IDE


## IO 编程

### 读写文件

- open write read

    ```py
    
    def oldRead(path):
        try:
            f = open('./a.txt', 'rb', encoding='utf-8')  # encoding  设置字符集
            print(f.read())
        finally:
            if f:
                f.close()

    # oldRead('./a.txt')

    def withRead(path):     # with 写法不需要手动 close()
        with open(path, 'r',  encoding='utf-8') as f:
            print(f.read())

    def writeFile(path):
        with open(path,'w', encoding='utf-8') as f:
            f.write('整的挺不错')
    ```
    mode | 功能 | dsf
    -|-|-
    r | 只读 | 不存在报错
    w | 写入 | 覆盖， 不存在则 新建
    x | 文件不存在时 新建| 否则 报差错
    a | 追加 | 不存在 新建
    b | 二进制 | 
    t | 文本模式 | default
    \+ | 更新模式 | 和 其他组合  同时可读写

### StringIO 和 BytesIO

### 操作文件和目录

### 序列化

## 进程和线程

## 正则

## 常用内奸模块

## 常用第三方模块

## venv

## 图形界面

## 网络编程

## 电子邮件 

## 访问数据库

## web开发

## 异步IO

## 使用MicrosoftPython
