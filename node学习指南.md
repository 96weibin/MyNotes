# node学习指南读书笔记

## 第一章 node.js启动与运行

    node特点 ： 单线程、异步io、事件驱动
    传统apache服务器，每次接收到一个用户请求就开启一个进程||线程进行处理。

### hello World

```js
    var http = require("http");     //请求内置http模块
    let server = http.createServer((req,res)=>{ //调用方法开启服务器
        res.writeHead(200,{'content-Type':'text/plain'});   //http响应头  设置项客户端发送数据类型
        res.write('I say ')       //  想页面写
        res.end('hello world')  // 必须有 end   end 会输出一次结果   还可以传第二个参数  设置编码集(未找到应用实例) 
    }).listen(1234)         //1234端口监听
```
### readFile

```js
    let http = require('http');
    let fs = require('fs');
    let server = http.createServer((req,res)=>{
        fs.readFile("./helloworld.js",'utf8',(err,data)=>{
            res.writeHead(200,{'Content-Type':'text/plain'});
            if(err) {
                res.end('can`t read file')
            } else {
                res.end(data)
            }
        })
    }).listen(1234)
    console.log('server listen in port 1234')
```
## 第二章 Node 与 Repl

gitbash 输入 node  开启 repl
可编写代码  与 js 一样   未闭合的 大括号小括号   可以通过 . 来表示不闭合
_下划线  代表上一个表达式  可以 通过 _ 对上一个表达式进行操作

```js
var obj = {
...
...
...
}  //闭合后 执行
```

## 第三章 node核心库

### 全局对象 global、process、buffer

    node 有3个全局对象  global process buffer

#### global


