let promise = new Promise((reslove, reject) => {
    setTimeout(() => {
        reslove('success, get data')
    }, Math.random() * 1000);
    setTimeout(() => {
        reject('time out')
    }, 500);
})
console.log(promise)
promise.then(reslove => {
    console.log('resloved', reslove)
}, reject =>{
    console.log('reject', reject)
}).then(res => console.log(res))