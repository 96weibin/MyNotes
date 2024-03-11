d1 = {'name': 'weibin', 'age': 18, 'gender': True}

# 可迭代的对象 list dict tuple
s1 = set(d1)    # key 的 set
s1.add('some')
s1.update(('grid', 'prop'))
s1.pop()    # 随机删除一位  不知道啥用
s1.remove('some')   # 不存在则会报错
s1.discard('some') # 不存在不会报错

print(s1)