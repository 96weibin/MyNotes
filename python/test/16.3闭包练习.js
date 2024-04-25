// 第一题 
// # const counter = createCounter();  
// # console.log(counter()); // 输出: 1  
// # console.log(counter()); // 输出: 2  
// # console.log(counter()); // 输出: 3

function createCounter(){
    let count = 0;
    return function(){
        return  count +=1
    }
}

counter = createCounter()
console.log(counter())
console.log(counter())
console.log(counter())
console.log(counter())


// 第二题 carr用ing
// function sum(a, b, c) {  
//     return a + b + c;  
//   }  
    
//   const curriedSum = curry(sum);  
//   console.log(curriedSum(1)(2)(3)); // 输出: 6

function sum(a, b, c) {
    return a + b + c;
}

function curry(fn) {

    return function carriedFn(...args) {
        if(args.length >= fn.length) {
            return fn.apply(this, args)
        } else {
            return function(...args2) {
                return carriedFn.apply(this, args.concat(args2))
            }
        }
    }
}

curriedSum = curry(sum);
console.log(curriedSum(1)(2)(3))    // 6

// const counterObject = createCounterObject();  
// counterObject.increment();  
// console.log(counterObject.getCount()); // 输出: 1  
// counterObject.increment();  
// console.log(counterObject.getCount()); // 输出: 2

function createCounterObject(){
    count = 0
    class CounterObject{
        count = 0
        constructor(){};
        increment(){
            this.count ++;
        }
        printCount(){
            console.log(this.count)
        }
    }
    
    return new CounterObject()
}

const counterObject = createCounterObject();   
counterObject.increment(); 
counterObject.printCount()
counterObject.increment(); 
counterObject.printCount()
counterObject.increment(); 
counterObject.printCount()
// const obj = {  
//     value: 10,  
//     handler: function(event) {  
//       console.log(this.value, event);  
//     }  
//   };  
    
//   const eventEmitter = createEventEmitter();  
//   eventEmitter.addEventListener('event', obj.handler, obj);  
//   eventEmitter.trigger('event', 'data'); // 输出: 10 'data'


// function greet() {  
//     console.log('Hello!');  
//   }  
    
//   const loggedGreet = logDecorator(greet);  
//   loggedGreet();  
//   // 输出:  
//   // Before greet  
//   // Hello!  
//   // After greet