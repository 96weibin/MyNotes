// # const counter = createCounter();  
// # console.log(counter()); // 输出: 1  
// # console.log(counter()); // 输出: 2  
// # console.log(counter()); // 输出: 3

function createCounter(){
    let count = 0;
    return function(){
        count +=1
        return count
    }
}

counter = createCounter()
console.log(counter())
console.log(counter())
console.log(counter())
console.log(counter())


// function sum(a, b, c) {  
//     return a + b + c;  
//   }  
    
//   const curriedSum = curry(sum);  
//   console.log(curriedSum(1)(2)(3)); // 输出: 6
  

// const counterObject = createCounterObject();  
// counterObject.increment();  
// console.log(counterObject.getCount()); // 输出: 1  
// counterObject.increment();  
// console.log(counterObject.getCount()); // 输出: 2


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