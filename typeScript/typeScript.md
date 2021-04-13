# TypeScript

- 微软开发的js的超级,编译时检测

## 优劣

- 优点
    - 强类型语言，严谨
    - 补充了js没有的类型、抽象、接口
    - 修饰符、
    - 泛型
    - 抽象和接口

- 缺点

## 安装

1. npm

    ```shell
    $ npm i -g typescript
    ```

2. tsc

    ```js
    $ tsc xxx.ts
    ```

## 类型

- any、number 、boolean 、string 、number[]、enum 、 valid、 null、nudefind、never、HTMLElement

- never 函数不会执行结束 throw Error

1. 显式声明

    ```ts
    let  stra:string;

    function add(a:number,b:number):number{  //变量、函数返回值确定类型
        return a + b;   //类型不对 编译报错
    }

    let a:(number|string);      //联合类型
    let arrA:(number|string)[] = [1,2,3,'4']

    let arrB:[number,boolean] = [1,true] //元祖类型

    let objA:{a:string,b:number} = {a:'你好',b:18}

    //枚举  -- 列举有限的可能性
    enum Gender{Male,Female}
    let gender:Gender  = Gender.Male
    //TODO
    console.log(gender)

    ```
2. 隐式声明

    ```ts
    let a = 12;
    //此时a 变量只能存储 数字类型,赋值其他类型报错
    ```
## 类

- 类内属性需要声明，
- 修饰符   public、private（仅自身）、 protected  （自身和子集）

```js
class Person {
    private name:string;        //类里面的变量，需要先声明
    protected age:number;
    constructor(name:string, age:number){
        this.name = name;
        this.age = age;
    }

    show():void{     //public 函数
        console.log(this.name + this.age)
    }
    
}

class Staff extends Person {        //继承
    private job:string;             //声明自身类型的 属性
    constructor(name:string,age:number,job:string){    
        super(name,age)     //super  只能在constructor 内调用
        this.job = job      
    }
    show():void{
      super.show()
      console.log(this.job)  
      console.log(this.age)     //访问父级的 protected 属性
    }
}

let p:Person = new Person('weibin',17);
p.show()
let weibin:Staff = new Staff('weibin',18,'工程师');
weibin.show()
```

- 简写

```ts
class Person {
    constructor(private name:string, protected age:number){}
    show():void{     //public 函数
        console.log(this.name + this.age)
    }
}
```

### 修饰符

1. static 静态成员，无需实例化即可调用 
    
    ```js
    class Person {
        public static videoName:string = '你好李焕英'
        constructor(){
        }
    }
    //无需实例化即可调用
    console.log(Person.videoName) 
    ```
2. const 只读成员，不能修改

//TODO

### Accessors 存取器 get/set

- 设置读取 对象属性，   不支持ES3/4

    ```ts
    class Person {
        constructor(protected gender:string, public age:number, private _name:string){
        }
        public get name() : string {
            return this._name
        }
        public set name(v : string) {
            if(v.length < 8){       //set 可以进行判断
                throw new Error('名字不能少于8位')
            } else {
                this._name = v;
            }
        }
        
        
    }

    let p:Person = new Person('male',18,'weibin')

    // console.log(p._name)    //报错   无法访问私有变量

    console.log(p.name)
    p.name = '伟斌的名字很长很长'       //存取器   读写  私有变量
    console.log(p.name)
    console.log(p.age)
    ```

    ```shell
    $ tsc -t es5 .\test.ts  #-t 设置target es5
    ```


### 抽象&接口

- 许多对象有公共的特征，通过  继承 或 接口完成,实现对子类的规范

#### abstract 抽象

- 只能作为父级，无法实现，子级继承  必须实现父级的所有抽象方法

    ```ts
    abstract class Sharp{           //抽象类
        abstract draw(gd):void;     //抽象方法
        abstract area():number;
    }

    class Circle extends Sharp{     //继承抽象类
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

    //一个 父类可以是现成  不同的子类，且子类的类型与父类相同，----多态
    ```

####  interface接口 

- interface 定义接口, implements 实现接口
- 通过接口实现的类必须 实现接口的全部方法
- 实现类 不是继承 没有 super

    ```ts
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

    let c1:Circle = new Circle(10)
    console.log(c1.area())
    let r1:Rect = new Rect(10,20)
    console.log(r1.area())
    ```

## tsloader 