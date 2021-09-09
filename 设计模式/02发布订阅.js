// 基础发布订阅     订阅了全部事件,不能针对不同的发布执行订阅事件


// let event = {
//     clientList : [],
//     subscrib(fn){
//         this.clientList.push(fn)
//     },
//     publish(){
//         this.clientList.forEach((fn)=>{
//             fn.apply(this, arguments)
//         })
//     }
// }
// event.subscrib(function(price,squareMeter){
//     console.log('价格' + price)
//     console.log('平方米' + squareMeter)
// })
// event.subscrib(function(){
//     console.log('订阅cb执行')
// })
// event.publish(2000000,88)
// event.publish(10000,10)、


//

let event = {
    clientlist : {},
    subscribe(clientId,cb){
        if(!this.clientlist[clientId])
        this.clientlist[clientId] = [];
        this.clientlist[clientId].push(cb)
    },
    publish(clientId){
        if(!this.clientlist[clientId].length)
        return
        this.clientlist[clientId].forEach(cb => {
            cb.call(this)
        });
    }
}


event.subscribe('80',()=>{console.log('80平米的房子到了快来买')})

event.publish('80')