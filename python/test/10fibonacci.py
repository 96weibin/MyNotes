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

def printFibList(n: int) -> list[int]:
    """ 输出fib 的几位
    
    """
    if(n < 0):
        print('should greate than 0')
        return 'type error'
    a, b = 0, 1
    fibList = [a, b]

    for i in range(0, n):
        if(len(fibList) < n):
            a, b = b, a+b
            fibList.append(b)
        print(fibList[i])


printFibList(11)