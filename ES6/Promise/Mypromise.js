

const FULFILLED = 'fulfilled'
const PENDING = 'pending'
const REJECTED = 'rejected'

class MyPromise{
    
    PromiseState = PENDING;
    _value = undefined;
    _microTaskQueue = []
    
    /**
     * 
     * @param {any} data reslove data
     */
    _reslove(data) {
        this._changePromiseState(FULFILLED, data)
    }

    _reject(reason) {
        this._changePromiseState(REJECTED, reason)
    }

    /**
     *  
     * @param {Function} onfulfilled 成功回调
     * @param {Function} onrejected 失败回调
     */
    then(onfulfilled, onrejected) {
        //添加回调  到队列  等 state change 执行
        this._microTaskQueue.push({handler: onfulfilled, state: FULFILLED })
        this._microTaskQueue.push({handler: onrejected, state: REJECTED })
        // queueMicrotask(x => )
    }

    _excutHandlers() {
        this._microTaskQueue = this._microTaskQueue.filter(x => x.state == this.PromiseState)
        while(this._microTaskQueue[0]) {
            if(typeof this._microTaskQueue[0].handler === 'function') {

                queueMicrotask(() =>this._microTaskQueue[0].handler())
            }
            this._microTaskQueue.shift();
        }
    }

    _changePromiseState(state, value) {
        if(this.PromiseState !== PENDING) return;
        this.PromiseState = state;
        this._value = value;
        this._excutHandlers();
    }

    constructor(executor) {
        executor(this._reslove.bind(this), this._reject.bind(this))
    }
}

let myP = new MyPromise((reslove, rejeect) => {
    setTimeout(() => {
        reslove("123")
        rejeect('reason')
    }, 100);

})
myP.then(data => {
    console.log('成功', data)
}, reason => {
    console.log('失败', reason)
})
myP.then(data => {
    console.log("成功2 ", data)
})