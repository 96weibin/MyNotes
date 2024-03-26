# 快速生成 有一定规则的 list
# [表达式 多个 Iterable condition]

l1 = [x*x for x in range(1, 10)]
print(l1) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

l2 = [x * 2 for x in range(1, 10) if x % 2 == 0] # 有判断条件
print(l2) # [4, 8, 12, 16]

l3 = [(a + b).lower() for a in 'XYZ' for b in "ABCD"] # 多个迭代
print(l3) # ['xa', 'xb', 'xc', 'xd', 'ya', 'yb', 'yc', 'yd', 'za', 'zb', 'zc', 'zd']
