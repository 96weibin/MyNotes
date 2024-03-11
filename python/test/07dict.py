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