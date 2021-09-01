//给一组数据 赋予更好的名字

//用奇怪的方式声明了一个类数组.....
enum Collor{red,green,blue}    //类数组
console.log(Collor)
//{ '0': 'red', '1': 'green', '2': 'blue', red: 0, green: 1, blue: 2 }
let c:Collor = Collor.green    //访问
console.log(c)  // 1
let collorName = Collor[2]
console.log(collorName) //blue