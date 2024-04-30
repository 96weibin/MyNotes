# [Python3](https://www.liaoxuefeng.com/wiki/1016959663602400/1017434209254976)

- 解释型语言， 交互式语言， 面向对象
- 缩进 代码块

## 环境搭建

- macOs 

```shell
$ brew inst

- read evaluate print loop
all python
# 需要安装Homebrew
```

## python REPL

## 面向对象

```py

class 
```

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