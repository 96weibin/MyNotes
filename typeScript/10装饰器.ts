function sayHi(value: boolean) {
    console.log('hello')
    return function(){
        console.log(value)
    }
}


@sayHi(false)
class AAASSS {
    constructor(){
    }
}

