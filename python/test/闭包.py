# 实现累加器

def plusOneFac():    
    start = 1
    def addOne():
        start = start + 1
        return start
    return addOne

addFn = plusOneFac()

print(addFn(),addFn(),addFn())