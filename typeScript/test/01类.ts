abstract class Sharp{           //抽象类
    abstract draw(gd):void;     //函数签名  抽象方法
    abstract area():number;
}

class Circle extends Sharp{     //继承抽象类
    public pi:string = '3.14'
    constructor(private r:number){  
        super()
    }
    draw(gd: any): void {           //每个实现类  都必须，实现抽象类的方法
        console.log('画圆')    
    }
    area(): number {
        return Math.PI * Math.pow(this.r,2)
    }
}

class Rect extends Sharp{
    constructor(private width:number, private height:number){
        super()
    }
    draw(gd: any): void {
        console.log('画方块')
    }
    area(): number {
        return this.width * this.height
    }
}
// let s:Sharp = new Sharp()  //报错  抽象类无法实现

let c1:Sharp = new Circle(10)
console.log(c1.area())
let r1:Sharp = new Rect(10,20)
console.log(r1.area())


// console.log(c1.Pi)      //Err c1:Sharp 后就只能放问 与 sharp 重合的部分
let c2:Circle = new Circle(11)
console.log(c2.pi)      //c2:circle 就可以访问到属性了