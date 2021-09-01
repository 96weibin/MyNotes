interface Sharp{           //接口    不需要class 声明类
    draw():void;
    area():number;
}
class Circle implements Sharp{     //实现接口
    constructor(private r:number){  //实现类  没有super
    }
    draw(): void {           //接口实现的类，必须实现左右接口的方法
        console.log('画圆')    
    }
    area(): number {
        return Math.PI * Math.pow(this.r,2)
    }
    
}
class Rect implements Sharp{
    constructor(private width:number, private height:number){
    }
    draw(): void {
        console.log('画方块')
    }
    area(): number {
        return this.width * this.height
    }
}

let c1:Sharp = new Circle(10)
console.log(c1.area())
let r1:Sharp = new Rect(10,20)
console.log(r1.area())