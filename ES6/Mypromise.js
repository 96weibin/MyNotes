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
    _state = pendding;
    _value = undefined;
    _reslove = (data) => {
        this._onStateChanged(fulfilled, data)
    };
    _reject = (data) => {
        this._onStateChanged(rejected, data)
    }
    _onStateChanged = (state, data) => {
        if(this._state != pendding) return;
        this._state = state; 
        this._value = data;
        console.log(this._state, this._value)
    }
    then(onFulfiled, onRejected){
       return new MyPromise()
    }
    constructor(executor){
        executor(this._reslove.bind(this), this._reject.bind(this));
    }
}


let my = new MyPromise((res, rej)=>{
    let data = 'my data'
    setTimeout(() => {

        res(data);
    }, 100);
})

console.log(my)