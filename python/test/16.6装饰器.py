
# 2 层 Decorator
def logD (func) :
    def wrapper(*args, **kw):
        print(args, kw)
        print("calling " + func.__name__)
        return func(*args, **kw)
    return wrapper


@logD
def sayHi(where):
    print('hello' + where)

sayHi('beijing')


# 3层 

def discount(app):
    youhui = 1
    match app:
        case 'taobao':
            youhui = youhui * .8
        case 'duoduo':
            youhui = youhui * .6
    def decorator(func):
        def wrapper(*args, **kw):
            res = func(*args, **kw) * youhui 
            return res
        return wrapper
    
    return decorator

selected = [1,2,3,4,5]
@discount('duoduo')
def getAllPrice(selected, youhui1):
    # print(selected)
    allPrice = 0
    for s in  selected:
        allPrice = allPrice + s
        print('all: {0}, s: {1}'.format(allPrice, s))
    # allPrice = allPrice if youhui1 == None else allPrice * youhui1
    return allPrice

print(getAllPrice(selected, 7))