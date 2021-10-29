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
    //接口类  约定对象属性

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
    console.log(myStr)  //Bob
    ```

4. 实现接口的类 的静态部分&实例部分

    - 静态部分问题
    
        - class implements interface 时会对class 是否全部实现 interface 进行检查(只检查实例部分，不检查静态部分)
        - class 的 constructor(){} 是这个类的静态部分
        - 所以 想用接口  约定 一个类 的时候不能直接实现

        ```ts
        interface PersonConstructor{
            new (n:string,a:number):any   //可以 new(n,a) 的一个东西   --- 就是一个构造函数嘛
        }

        class Staff implements PersonConstructor{
            constructor(n:string,a:number){}   //constructor是 静态部分,不进行检查, 所以会报错
            //Err ： 'Staff' provides no match for the signature 'new(n:string.....)'
        }
        ```

    - 实现接口约定类的方法

        ```ts
        interface PersonConstructor{
            new (n:string,a:number):PersonInterface;   //静态 
        }
        interface PersonInterface{
            tick():void   //实例部分
        }
        //interface设置 constructor
        class Staff implements PersonInterface{
            constructor(public n:string,public a:number){}   //静态部分 
            tick(){                                 //实例部分
                console.log('hhh')
            }
        }

        //
        function buildPerson (ctor:PersonConstructor,n:string,a:number):PersonInterface{
            return new ctor(n,a)            // 这里和Constructor 相关
        }

        let staff1:PersonInterface = buildPerson(Staff,'weibin',18)
        console.log(staff1) // Staff{n:weibin,a:18}
        staff1.tick()       //为什么   staff1 不能访问到n,a 属性

        ```

        ```ts
        //感觉还是不太能理解  为什么要像上面这么写
        let staff2 = new Staff('zw',16)
        console.log(staff2)
        console.log(staff2.n)
        ```

4. 接口继承接口

    - 实现继承的接口，必要实现 全部继承链 属性方法
    ```ts
    interface Person{
        gender:string;
        group():void;
    }

    interface Staff extends Person{
        assets:number;
        work():void;
    }

    class Weibin implements Staff{
        constructor(public assets:number,public gender:string){}
        group(){

        }
        work(){
            console.log('Im working')
        }
    }
    ```

5. 混合类型接口
    
    - 一个接口同时约定 对象、方法

    ```ts
    interface Counter {
        (start:number):string;  //接口作为函数接口
        interval:number;        //接口作为对象 设置属性
        reset():void;           //接口作为对象 设置方法
    }

    //混合模式，不通过implements 而是通过  function 模拟实现步骤实现
    // 混合模式  可以达成 一个接口既是方法，也是对象，
    // 但是  implements 的检查过程   个人不建议使用


    function getCounter():Counter{
        let counter = <Counter>function(start:number){};   //<Counter> 泛型 表明 fun是Counter接口类型的 
        counter.interval = 123;     //是否实现  接口的规定，都是可以的
        counter.reset = function(){}  //这么搞   接不接口  就没什么用了。
        return counter
    }
    let c = getCounter()
    console.log(c)
    ```

6. 接口继承类

    - 没太搞懂遇到再去官网看吧

    ```ts
    class Control{  //一个既有 publi 也有 private 的类
        private privateState:any;
        protected protectedState:any;
        public publicState:any;    
    }

    interface SelectableControl extends Control{
        select():void;      //接口继承类
    }

    /*

    try {// 直接实现接口测试  Err
        class Inp implements SelectableControl{  //Inp实现接口 
            public publicState = 'public';          //只有 public 的可以实现
            protected protectedState = 'protected';   //Inp 和 Control 不算子集关系  public 无法实现
            private privateState = 'private';       //private 就更不能实现了
            select(){}
        }
    } catch (error) {
        console.log(error)
    }

    */

    // 通过继承 Control 可以 实现protected  和 private 了
    class Button extends Control implements SelectableControl{
        select(){}
        sayHi():void{
            console.log(this.publicState)     //
            console.log(this.protectedState)
            // console.log(this.privateState)  //Err
        }
    }
    let b = new Button()
    b.sayHi()


    class TextBox extends Control{
        select(){}
    }
    let t = new TextBox()

    ```


7. 接口使用

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
- super 调用父级的构造函数
- 修饰符   public(默认)、private（仅自身）、 protected（自身和子集）、readonly

    ```js
    class Person {
        private name:string;        //类里面的变量，需要先声明
        protected age:number;
        constructor(name:string, age:number){  //构造函数
            this.name = name;
            this.age = age;
        }
        show():void{     //方法
            console.log(this.name + this.age)
        }
    }

    class Staff extends Person {        //继承
        private job:string;             //声明自身类型的 属性
        constructor(name:string,age:number,job:string){    
            super(name,age)     //super  只能在constructor 内调用,super调用父级的构造函数
                                //调用 super 必须在 this之前
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
- 提高对象读取的安全性

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

### abstract 抽象

- 只能作为父级，无法实现，子级继承  必须实现父级的所有抽象方法
- 函数签名  就是  抽象类中,abstract 的fn 也就是 interface 中没有{}的方法
- **与接口不同的，抽象只能对方法进行规定， 而接口还可以对参数、传参、类等进行限制**

    ```ts
    abstract class Sharp{           //抽象类
        abstract draw(gd):void;     //函数签名  抽象方法
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
        private Pi:string = '3.14'
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


    //一个 父类可以是现成  不同的子类，且子类的类型与父类相同，----多态
    ```

## 函数

- 函数定义类型

    ```ts
    //函数声明
    function add(a:number,b:number):number{
        return a + b
    }
    //函数表达式
    let sub = function(a:number,b:number):number{
        return a - b
    }
    // 完整的函数表达式
    let myAdd:(baseValue:number,increment:number) => number = function(x:number,y:number):number{
        //可以 : 函数的功能， 变量可以更好的描述
        
        return x + y
    }
    ```
- 传参 与 默认参数

    - ts函数传参个数严格要求
    - ? 可选参数需要在形参的最后, 未定义类型 则是any 
    - 参数默认值  gander = 'male' ,传入(undefined)触发
    - 剩余参数  与 ES6相同  ...args:string[]

    ```ts
    function buildName(first:string, last?:string):string {
        return first + last;
    }
    ```

- this 与 箭头函数




## 泛型

- 表示变量的类型

    - 泛型 比 any的优点  **可以限制函数进出类型一致**

    ```ts
    //泛型   
    function identity<T>(arg:T):T{return arg}
    //identity 接受两中参数  
    // 1 <> 中的表明类型的参数  感觉很像声明
    // 2 () 中的形参

    let output1 = identity<string>('hello word')
    let output2 = identity(2021)

    // output1 = 123;  //err
    // output2 = 'hello' //err


    //输入不同类型的变量  执行泛型函数 得到不同类型的变量
    ```
- 使用泛型变量

    ```ts
    function identity<T>(arg:T[]):T{
        //上面的例子中  arg 可以被认为是 any类型，没有明确的类型，对形参的操作就受限
        // 可以通过  T[] 的方式 进一步 描述 arg 的类型
        console.log(arg.length)
        return arg[0]
    }
    console.log(identity([1,2,34]))
    ```
- 泛型类型

    ```ts

    ```

## 命名空间

```ts
//定义
namespace Validation {
    export interface StringValidator {
        isAcceptable(s: string): boolean;
    }
}

//使用
let validators: { [s: string]: Validation.StringValidator; } = {};
```

## Decorators 装饰器

- 类， 方法，属性， 参数 装饰器   （访问符 get,set）
- 返回函数的函数，装饰器的形参会 传给 被返回的函数
- 

1. 启动装饰器

    - tsconfig.json
    ```json
        {
            "compilerOptions": {
                "target": "ES5",
                "experimentalDecorators": true
            }
        }
    ```
2. 声明装饰器
   
    ```ts
    function enumerable(value: boolean) {
        return function (target: any, propertyKey: string, descriptor: PropertyDescriptor) {
            descriptor.enumerable = value;
        };
    }
    ```
3. 使用装饰器

    ```ts
    class Greeter {
        greeting: string;
        constructor(message: string) {
            this.greeting = message;
        }

        @enumerable(false)
        greet() {
            return "Hello, " + this.greeting;
        }
    }
    ```

    ```ts   
        function sayHi(value: boolean) {
            console.log('hello')
            return function(){
                console.log(value)
            }
        }

        @sayHi(false)
        class AAASSS {
            constructor(){
            }
        }
        //hello
        //false
    ```

## 声明文件 .d.ts

- declear ， ts功能声明介绍的文件   代码版本的readme


## 基类&派生类，父类&子类， 继承&派生

1. 不同角度不同的叫法，其实 父类 == 基类 派生类 == 子类

2. 继承与派生

**继承**: 主要体现在对父类方法的重用
**派生**: 主要体现在对父类方法的补充 


## ?? || ?

1. ? 
   1. abc?.def     常用于读取, abc 为空时 不会调用.
2. || 
   1. 普通或操作，常用赋值 ，  如果为false  则不执行后面
3. ??
   1. 类似或，   区别:  如果为  空 则不执行后面，  0 可以