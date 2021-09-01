let str:string = "abcdef"

let len:number = (<String>str).length;
console.log(len)
len = (str as string).length
console.log(len)