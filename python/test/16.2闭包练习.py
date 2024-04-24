# const counter = createCounter();  
# console.log(counter()); // 输出: 1  
# console.log(counter()); // 输出: 2  
# console.log(counter()); // 输出: 3

def createCounter():
    count = 0
    def counter():
        nonlocal count      # python 需要额外 声明 nonlocal
        count += 1
        return count

    return counter


counter = createCounter()
print(counter())
print(counter())
print(counter())
print(counter())

# function sum(a, b, c) {  
#   return a + b + c;  
# }  
  
# const curriedSum = curry(sum);  
# console.log(curriedSum(1)(2)(3)); // 输出: 6
