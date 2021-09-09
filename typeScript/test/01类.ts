abstract class Foo{
    constructor(public type:string){}
    abstract test():void;

}
class Son extends Foo{
    
    constructor(public type:string){
        super(type)
    }
    test(){
        console.log(this.type)
    }
}


let s = new Son('son')
console.log(s)