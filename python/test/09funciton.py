import random
from typing import Union

# 自定义函数  函数约束（非强制）
def my_abs(x: float, format: bool = True) -> Union[int, float]: 
    """ 三双引号 文档字符串 介绍函数 

    空一行 描述 
    
    """
    x = x if x >= 0 else -x
    if format:
        return int(x)
    return x
print(my_abs.__doc__)   # 查看文档字符串
print(my_abs(-random.random() * 100, False))

# 自定义空函数
def emp_fun():
    pass