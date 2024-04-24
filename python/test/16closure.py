def cals_sum(*args):
    all = 0
    for item in args:
        all += item
    return all

sum = cals_sum(1,2,3,4,5)
print(sum)


def lazy_sum(*args):
    def sumFn():
        all = 0
        for i in args:
            all += i
        return all

    return sumFn
f1 = lazy_sum(1,2,3)
f2 = lazy_sum(4,5,6)
print(f1(), f2())    # 6 15


def count():
    fs = []
    for i in range(1,4):
        def f():
            return 2 * i
        
        fs.append(f)
    return fs

fs1, fs2, fs3 = count()
print(fs1(), fs2(), fs3())  # 6 6 6 


def closure_count():
    fs = []
    for i in range(1,4):
        def f(j):
            def doubleF():
                return j * j
            return doubleF
        fs.append(f(i))
    return fs

fs1, fs2, fs3 = closure_count()
print(fs1(), fs2(), fs3()) #1 4 9



def closure_count_shot():
    def f(i):
        return lambda  : i * i
    return map(f, range(1,4))

fss1, fss2, fss3 = closure_count_shot()
print(fss1(), fss2(), fss3())  # 1 4 9
