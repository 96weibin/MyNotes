//接口类  属性

/*
interface Obj{
    readonly mimi ?: string;  //只读
    name:string;            //必须项
    age?:number;             //可选项
}

let obj09 = {
    name:'weibin',
    // age:18
    gender:'male'
}

function fn (arg09:Obj):void{
     console.log(arg09.name + arg09.age)
}

fn(obj09)

 */


//接口类 函数

/**
interface FnInterface{
    (x:number,y:number):number;
}

let add:FnInterface = function(h,i){
    return h + i;
}
console.log(add(3,5))
 */


// 接口属性  可索引
/**
interface StringArray {
  [index: number]: string;
}

let myArray: StringArray;
myArray = ["Bob", "Fred"];

let myStr: string = myArray[0];
console.log(myStr)

 */

interface Shape10{
    color:string
}

interface Square10 extends Shape10{
    length:number
}

let obj10:Square10 = {
    color:'red',
    length:10
}