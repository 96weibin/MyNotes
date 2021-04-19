# TypeScript

- 微软开发的js的超级,编译时检测

## 优劣

- 优点
    - 强类型语言，严谨
    - 补充了js没有的类型、抽象、接口
    - 修饰符、
    - 泛型  <number>
    - 抽象和接口

- 缺点

TODO 

泛型
--strictNullChecks
symbol
HTMLElement

## 特点

1. 预编译报错 一般错误仍能编译成js，且不影响报错后面的内容的编译
2. 

## 安装

1. npm

    ```shell
    $ npm i -g typescript
    ```

2. tsc

    ```shell
    $ tsc --init #ts配置文件
    $ tsc xxx.ts
    ```

## 类型

1. 类型断言 assert

    - <>   as

    ```ts
        let str:string = "abcdef"
        let len:number = (<String>str).length;
        console.log(len)
        len = (str as string).length
        console.log(len)
    ```


### 基础类型

    - boolean、 number、 string、null、undefined 与js相同

### 引用类型

1. 数组

    - 创建 

    ```ts
        let listNum:nummber[] = [1,2,3,4]  //字面量创建
        let listStr:string[] = ['1','2','3']

        let list:Array<number> = [1,2,3,4] //泛型
    ```

    - 元组 tuple 规定每一位的类型

    ```ts
        let x:[number,string] = [1,'2'] //规定每一个位置的类型
        x.push(3)  //push 必须在元组类型内
        console.log(x[2])  //tsc预编译报错  但是仍能编译成js
        console.log('4')   //上面 tsc 预编译错误不影响后面继续编译
        
        /**
         *  node xxx.js
        *
        *  3 
        *  '4' 
        /

    ```
3. 枚举 enum (对js类型的拓展)

    - 给一组数据 赋予更好的名字,用奇怪的方式声明了一个类数组.....

    ```ts
    enum Collor{red,green,blue}    //类数组
    console.log(Collor)
    //{ '0': 'red', '1': 'green', '2': 'blue', red: 0, green: 1, blue: 2 }
    let c:Collor = Collor.green    //访问
    console.log(c)  // 1
    let collorName = Collor[2]
    console.log(collorName) //blue
    ```

4. any、void 、never

    - any  类型判断 任意类型都可以 且可以赋值为其他类型
    - any  检查函数 必须  有返回值， 任意值都可以
    - void 检查函数 必须 没有返回值
    - never 检查函数 一定不会执行到完毕 throw Err

5. object  注意o小写

    - 常用于标识非 number,string,booolean,symbol,null,undefined 的类型


## 声明

1. 显式声明

    ```ts
    let  stra:string;

    function add(a:number,b:number):number{  //变量、函数返回值确定类型
        return a + b;   //类型不对 编译报错
    }

    let arr1:number[] = [1,2,3]     //基础数组
    let arr2:Array<number> = [1,2,3]    //泛型

    let a:(number|string);      //联合类型
    let arrA:(number|string)[] = [1,2,3,'4']
    let arrB:[number,boolean] = [1,true] //元祖类型  每个位置的类型已经确定
        //元祖  额外push类型被规定在联合类型内

        //元祖额外的类型 为 undefined  不能 arrB[3] 取



    let objA:{a:string,b:number} = {a:'你好',b:18}

    //枚举  -- 列举有限的可能性
    enum Gender{Male,Female}
    let gender:Gender  = Gender.Male
        //枚举还可以和下标关联

    //TODO
    console.log(gender)

    ```
2. 隐式声明

    ```ts
    let a = 12;
    //此时a 变量只能存储 数字类型,赋值其他类型报错
    ```

##  interface接口 

1. 接口类 约定传参

    ```ts
    //接口类  属性

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
    ```

2. 接口类 约定函数

    ```ts
    interface FnInterface{
        (x:number,y:number):number;
    }

    let add:FnInterface = function(h,i){
        //形参  不需要同名,但要匹配
        return h + i;
    }
    console.log(add(3,5))
    ```
3. 可索引的接口

    ```ts
    // 接口属性  可索引
    interface StringArray {
    [index: number]: string;
    }

    let myArray: StringArray;
    myArray = ["Bob", "Fred"];

    let myStr: string = myArray[0];
    console.log(myStr)
    ```
4. 继承接口

    ```ts
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
    //square 的实现需要包含两个
    ```

5. 接口使用

    - interface 定义接口, implements 实现接口
    - 通过接口实现的类必须 实现接口的全部方法
    - 实现类 不是继承 没有 super
    - 只要 两个类内部类型兼容，可以不需要 implements

    ```ts
    interface Sharp{           //接口    不需要class 声明类
        draw():void;
        area():number;
    }
    class Circle implements Sharp{     //实现接口
        constructor(private r:number){  //实现类  没有super
        }
        draw(): void {           //接口实现的类，必须实现所有接口的方法
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



## tsloader 