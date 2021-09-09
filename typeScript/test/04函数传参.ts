// 1. ts 中函数传参 要与声明严格相符，不能多传少传
// 2. 可选参数需要在形参的最后, 为定义类型 则是any 
// 3. 参数默认值  

function buildName(first='zhao', last:string, morney?):string {
    if(morney){
        return first + last + morney;
    } else {
        return first + last;
    }
}
// let res1 = buildName('zhao')   Err
let res2 = buildName('zhao','wei')   //ok 
// let res3 = buildName('zhao','wei','bin') Err
let res4 = buildName('weibin','zhao','infinity') 
let res5 = buildName(undefined,'zhao','infinity') 

console.log(res5)




