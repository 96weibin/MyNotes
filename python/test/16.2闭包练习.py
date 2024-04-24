# 累加器

# const counter = createCounter();  
# console.log(counter()); // 输出: 1  
# console.log(counter()); // 输出: 2  
# console.log(counter()); // 输出: 3

import inspect


def createCounter():
    count = 0
    def counter():
        nonlocal count      # python 需要额外 声明 nonlocal
        count += 1
        return count

    return counter


counter = createCounter()
print(counter())
print(counter())
print(counter())
print(counter())

# 科里化
# function sum(a, b, c) {  
#   return a + b + c;  
# }  
  
# const curriedSum = curry(sum);  
# console.log(curriedSum(1)(2)(3)); // 输出: 6

def carry(fn):
    """ 将函数 科里化

    获取形参函数形参长度  len(inspect.signature(fn).parameters)
    可变形参 *xx 将参数 转成了 元组

    元组， 数组 可以直接 通过 + 进行拼接

    """

    if(not callable(fn)):                   # not callable 就不是函数
       return "fn shoulde be a function"
    fnParamsLen = len(inspect.signature(fn).parameters)

    def carryiedFn(*args):
        print(args)
        if len(args) >= fnParamsLen:
            res = fn(*args)
            return res
        else:
            return lambda *newArgs : carryiedFn(*(args + newArgs))
    return carryiedFn

def sum(a, b, c):
    return a + b + c

carryiedSum = carry(sum)
print(carryiedSum(1)(2)(3))