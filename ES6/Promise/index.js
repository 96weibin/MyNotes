const p = new Promise((reslove, reject)=>{
    // setTimeout(() => {
    //     reslove(100)
    // }, 100);
    reslove(100)
})

p.then(x => {
    console.log(x)
},2)
console.log(p)

setTimeout(() => {
    console.log(p)
}, 300);
