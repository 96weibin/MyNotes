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