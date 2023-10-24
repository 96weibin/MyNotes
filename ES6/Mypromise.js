/** 
 * 
 * use Promise
 * 
 */

// var p = new Promise((reslove, reject) => {
//     setTimeout(() => {
//         // return 321;
//         reslove('res 123');
//     }, 100);
// })
// p.then(res => {
//     console.log(res)
//     return 'return 123'
// }).then(res => {
//     console.log(res);
//     throw "throw 123"
// }).catch(rej => {
//     console.log(rej);
//     return 'after catch then'
// }).then(res => console.log(res));


const pendding = "pendding"
const fulfilled = "fulfilled"
const rejected = "rejected"

class MyPromise {
    #PromiseState = pendding;
    #PromiseResult = undefined;

    

    

    constructor(executor){
        
    
        const reslove = (data) => {
            onStateChanged(fulfilled, data)
        };
        const reject = (data) => {
            onStateChanged(rejected, data)
        }
        const onStateChanged = (state, data) => {
            this.#PromiseState = state;
            this.#PromiseResult = data;
            console.log(this.#PromiseState, this.#PromiseResult)
        }
        executor(reslove, reject);
        
        
    }
}


new MyPromise((res, rej)=>{
    // rej(123)
    res(234);
})