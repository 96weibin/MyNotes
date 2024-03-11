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