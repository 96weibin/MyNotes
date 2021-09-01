let a:number = 123;

function fn(flag:boolean, msg:string):string{
    
    if(!flag){
        let msg = "false ya"
        return msg
    }
    return msg
}

console.log(fn(false,'true ya'))