# EcmaScript6

## 变量定义

1. var, const, let 的区别

符号 | 特点 | 作用域
-|-|-
var | 定义的**变量**可被修改，且不需初始化，默认undefined | 函数作用域
const | 定义**常量**， 且需要初始化，只读 | 块级作用域
let | 定义**变量**， 不可重复声明, 声明不提升 | 块级作用域

## 解构赋值

- 左侧 定义变量，匹配 右侧的值，进行快速赋值。

```js
//数组
let [a,b,c] = [1,2,3,4]       // a=1, b=2, c=3

//对象

let {x: width, y: height} = {   //匹配: 声明
    x: 100,
    y: 200,
    z: 300
}   // width = 100, height = 200
```

## 箭头函数

- 箭头函数 this 指向父级
- 箭头函数没有arguments

1. 函数声明

```js
    // var fun = (形参) => {函数体};
    var add = (a = 1, b = 2) => a + b; //默认值
    // 函数体返回对象   因为函数体括号 和 对象括号相同，需要小括号 扣起来简写

    var f = arr =>({name: arr.find(a=>a.name =="weibin").name, age: arr.find(a=> a.name == "weibin").age}); //返回 {name: xx, age:xx}
```

2. 简写规则

条件 | 简写 |
-|-|-
只有一个形参 | 省略形参括号() | var fun = a => {return a + 1};
函数体只有一句  | 省略 函数体括号{} 和 return | var fun = a => a*2;

## 拓展运算符 ...arr

- 表示将数组展开  [1,2,3,4]  => 1,2,3,4

1. 常见用法

    1. 拓展参数
    
    ```js
    let show = (a,b,...args) =>{
        //a,b 以外的所有传参  存储在  args 这个数组中
    }
    show(1,2,3,4,5)     // a = 1, b = 2, args = [3,4,5]
    ```

    2. 数组拼接， 拓展

    ```js
    var arr1 = [1,2,3];
    var arr2 = [4,5,6];
    arr1.push(arr2); //  [1,2,3,[4,5,6]]   长度为4的数组
    arr.pop()
    arr1.push(...arr2)   //[1,2,3,4,5,6]    长度位6的数组
    ```


## 数组方法

方法 | 功能 | 返回值
-|-|-
forEach(callback, thisArr?) | 对数组每一项 运行callback | 无
map(callback, thisArr?) | 对数组每一项 运行callback | callback 组成的数组
filter(callback, thisArr?) | 对数组每一项 运行callback | 由返回true的item组成

- 类数组转化成数组

```js
Array.from(arrayLike)
```

## JSON 

1. 简写
    1. k v 同名 可以只写一个
    2. v 是function 可以不写function

```js
var json ={a,b}   //  ==> {a: a, b: b}

var json = {fun(){}}    // ==> {fun: funciton(){}}
```

## 模板字符串

```js
`my name is ${json.name}`
```
## 面向对象

1. class 面向对象

```js
class Person{       //类不可重复声明，类声明不提升。
    constructor(name, age, job){  //构造函数, 接受new传的参数, 创建时执行函数体
        this.name = name;
        this.age = age;
        this.fun = ()=>{
            return '实例方法';
        }
    }

    showName(){     //原型方法， 可以继承
        return `my name is ${this.name}`;
    }
}

let p = new Person('weibin', 18, 'farmer');
p.showName();   // my name is weibin
```

2. extends 继承

```js
class Worker extends Person{
    constructor(name, age , job){
        super(name, age);
        this.job = job;
    }
    showJob(){
        return `my job is ${this.job}`;
    }
}

let w = new Worker('gaomu', 18 , 'taitai');
w.showJob(); //my job is taitai
w.fun();  //实例方法
w.showName();   //my name is gaomu
```

## bind

> bind 无法改变箭头函数this指向， bind 并不执行

```js
    class Person {
        constructor(date, name) {
            this.date = date;
            this.name = name;
        }
        sayHello() {    //普通函数简写  sayHello: function(){}
            console.log(`hello ${this.name} today is ${this.date}`);
        }
        sayName = ()=>{ //箭头函数
            console.log(`hello my name is ${this.name}`);
        }
    }

    let p = new Person('2022-01-03', 'weibin');

    let box = document.querySelectorAll('.box');
    box[0].onclick = function (e) {
        p.sayHello();   //hello weibin today is 2022-01-03
        //p 实例调用 方法， this指向实例P
        p.sayName();     //my name is weibin
    }
    box[1].onclick = p.sayHello;     //hello undefind today is undefind
    //dom事件 this指向dom对象  没有name date

    box[2].onclick = p.sayHello.bind(p); //hello weibin today is 2022-01-03
    //bind 改变了 this 指向 p

    box[3].onclick = p.sayName; //hello my name is weibin
    //箭头函数  this 指向 函数sayName的父级作用域 Person
    box[4].onclick = p.sayName.bind(window);//hello my name is weibin
    //bind 无法改变 箭头函数的this bind 无效
```

## promise 语法糖

1. Promise ------ 捕获异步的  回调

```js
//创建  Promise
let p = new Promise((reslove, reject)=>{
    $.ajax({
        type: "Get",
        url: "http://127.0.0.1:8888",
        success: function (response) {
            reslove(response);  //请求成功 reslove 结果
        },
        error: function (err) { 
            reject(err);        //请求失败 reject 结果
        }
    });
})

p.then(res => {                  //捕获 reslove
    console.log('success ' + res);
})

p.catch(err=>{                  //捕获 reject
    console.log('fild' + err)
})
```

2. promise的使用

    1. 简易延时
    ```js
    function sleep(s) {
        return new Promise (reslove=>{
            setTimeout(()=>{
                reslove();
            }, s * 1000)
        })
    }
    ```

    2. promise.all

        - 管理多个promise对象，

        ```js
            Promise.all([  
            $.ajax('http://127.0.0.1:8080/1.txt'),  //$.ajax 的返回值也是  promise
            $.ajax('http://127.0.0.1:8080/2.txt'),
            $.ajax('http://127.0.0.1:8080/3.txt'),
        ]).then((arr)=>{//都请求 成功触发 
            let [d1,d2,d3] = arr; 
        },(err)=>{
            console.log(err)
        })
        ```
    
    3. async ,await 异步解决方案

    ```js
    (async function load() {
        try {
            let data1 = await $.ajax({url:'http://127.0.0.1:8080/1.txt'});
            //要等 await reslove 结果了才会继续向下执行  
            if(data1.a +  data1.b > 10){
                let data2 = await $.ajax({url:'http://127.0.0.1:8080/2.txt',dataType:'json'});
                alert(data2[0])
            } else {
                let data3 = await $.ajax({url:'http://127.0.0.1:8080/3.txt',dataType:'json'});

                console.log(typeof data3)
                alert('hello ' + data3.name)

            }
        } catch (e) {
        // throw new Error('报错异常')
            console.log(e)
        }
    })()
    ```
## 模块化

```js
    //导出
    export default class {	//default方式 导出整个模块
        constructor (name,age){
            this.name = name;
            this.age = age;
        }
        show(){
            console.log(`我叫${this.name},今年${this.age}`)
        }
    }

    //导入
    import mod1 from './mod1'		//导入整个模块
    let p = new mod1('blue', 18);
    p.show()

    //导出
    export let mod1 = function(){}	//将模块分部分导出
    export let mod2 = function(){}


    //导入
    import {mod1,mod2} from './mod1'	//以结构的方式导入模块的部分
```