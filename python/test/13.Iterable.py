
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
