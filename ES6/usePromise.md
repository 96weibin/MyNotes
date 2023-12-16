```js
/** 
 * 
 * use Promise
 * 
 */

var p = new Promise((reslove, reject) => {
    setTimeout(() => {
        // return 321;
        reslove('res 123');
    }, 100);
})
p.then(res => {
    console.log(res)
    return 'return 123'
}).then(res => {
    console.log(res);
    throw "throw 123"
}).catch(rej => {
    console.log(rej);
    return 'after catch then'
}).then(res => console.log(res));

```