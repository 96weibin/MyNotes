# for in

listOod = list(range(0, 100, 2))
for n in listOod:
    print(n)

# while
    
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