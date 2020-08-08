# node 

## 常用模块

### Assert 断言
- 常用于函数传参检测

    ```js
        const assert = require('assert');

        function add(a,b){
            assert(arguments.length == 2,'必须穿两个参数')
            assert(typeof a === 'number','第一个参数必须是数字')
            assert(typeof b === 'number','第二个参数必须是数字')
            return a + b
        }
        add(5)
        //不满足判断 就报后面的错误
    ```
### cluster、process、childProcesses、os 多进程

os.cpus()

### crypto 签名

- 签名

    ```js
        const crypto = require('crypto');

        function md5 (p){
            if(typeof p == 'string'){
                let obj = crypto.createHash('md5');//或sha1 算法
                obj.update(p)       //传入进行计算的数据p
                return obj.digest('hex');  //返回  16进制摘要 加密后的密码
            }
        }

        console.log(md5('123456'))
    ```
- 与 秘钥 混合多次加密  增加破译难度

### dns 域名解析

- 将域名解析成ip地址

    ```js
        dns.resolve('www.baidu.com',(err,data)=>{if(!err){console.log(data)}})
    ```

### events  自定义事件

- evenets 模块的 EventEmitter

    ```js
        const EventEmiter = require('events').EventEmitter   //
        let ee = new EventEmiter()
        ee.on('msg',(a,b)=>{
            console.log('msg事件触发',a,b)
        })
        ee.emit('msg',12,8)
    ``` 
### http 

- http服务模块

    ```js
    const http = require('http');
    let server = http.createServer((req,res)=>{

        // 读取请求头
        // req.headers   请求头信息
        // req.url        请求的url parse获取数据


        // 设置返回头
        // res.writeHead(200,{'返回头':'返回体',...})
        // res.setHeader('name','val')
        // res.write('返回内容')
        // res.end()           断开http请求
    })
    server.listen(8080)
    ```


### path 路径解析
- 目录处理

    ```js
        const path = require('path');

        const oPath = 'file:///D:/File/MyNotes//index.html'
        let obj = path.parse(oPath);
        console.log(obj)    //dir、base、ext、name
        console.log(path.dirname(oPath))//目录名
        console.log(path.extname(oPath))//拓展名
        console.log(path.basename(oPath))//文件名
    ``` 

### url queryString 链接解析

- queryString 模块对url中?后面的数据进行解析，功能被url模块涵盖
- url模块 解析rul

    ```js
        const url = require('url');
        const oPath = 'http://www.baidu.com:8080/sousuo/index.html?name:weibin&age:18&gender:male'
        let obj = url.parse(oPath,true);    //true则将query解析成对象
        console.log(obj)    
    ```

    ```js
    Url {
        protocol: 'http:',
        slashes: true,
        auth: null,
        host: 'www.baidu.com:8080',
        port: '8080',
        hostname: 'www.baidu.com',
        hash: null,
        search: '?name:weibin&age:18&gender:male',
        query: [Object: null prototype] {
            'name:weibin': '',
            'age:18': '',
            'gender:male': ''
        },
        pathname: '/sousuo/index.html',
        path: '/sousuo/index.html?name:weibin&age:18&gender:male',
        href: 'http://www.baidu.com:8080/sousuo/index.html?name:weibin&age:18&gender:male'
        }
    ```


### fs File System  文件

- 文件读写

    ```js
        const fs = require('fs');

        fs.readFile('1.txt',(err,data)=>{   //异步读
            if(err){
                console.log(err);
            } else {
                console.log(data)
            }
        })
        var buffer = fs.readFileSync('1.txt')  //同步读

        fs.writeFile('2.txt',buffer,(err)=>{    //异步写
            if(err){
                console.log(err)
            } else {
                console.log('成功')
            }
        })
        fs.writeFileSync('3.txt','asjldkfjaslkd')//同步写
        fs.appendFile('1.txt','追加在最后'(err)=>{})       //异步追加
    ```
- 流

    ```js
        let rs = fs.createReadStream(`./www/${pathname}`);  //读取流
        rs.on('error',(err)=>{  //error、data等状态事件
            console.log(err)
        })
        rs.pipe(res)    //pipe到res返回数据
            
        let ws = fs.createWriteStream(`./upload/${uuid()}`); //写入流
        ws.on('finish',()=>{
            //写入完成
        })

    ```
- 上传文件

    |enctype|功能|
    -|-
    text/plan | 纯文本
    application/x-www-form-urlencoded | url编码
    multipart/form-data | 文件内容

- 文件状态 

    ```js
        fs.stat
    ```

#### formData

- form表单 multipart/form-data   自己new

    ```js
        /**formData 创建 增删改查**/
        //let data = new FormData()
        //set(key,val)      同key会覆盖    
        //append(key,val)   同key多值
        //get(key)          获取一个
        //getAll(key)          获取
        //delete 
    ```
    [express formdate 拖拽上传demo](https://www.cnblogs.com/96weibin/p/12169016.html)

### uuid

- 文件随机数命名

    ```js
        const {v4} = require('uuid')
        console.log(v4())//cd0bf902-afdb-4075-aecd-74def7b55fdc
    ```


### Buffer

- 二进制数据操作  不破坏文件

    ```js
        let bf1 = Buffer.from('abcdefg')   //创建Buffer
        let bf2 = Buffer.from('hijklm')
        console.log(bf1.indexOf('b'))    //1
        console.log(bf1.slice(1,3).toString())    //bc 留头去尾

        let arr = [];
        arr.push(bf1)
        arr.push(bf2)    //post接受块push进数组
        let bfArr = Buffer.concat(arr)  //buffer数组 重组buffer
        console.log(bfArr)
    ```
- 简易封装 split

    ```js
    Buffer.prototype.split = Buffer.prototype.split || function(cut){
        let arr = [];
        let start = 0;
        let len = cut.length;

        let index = 0;
        //start     从0开始,   = index + len
        //indexOf   从start向后
        while(this.indexOf(cut,start) != -1){
            index = this.indexOf(cut,start);
            arr.push(this.slice(start,index));
            start = index + len
        }
        arr.push(this.slice(start))
        return arr
    }
    ```

### zlib 压缩 gz

- 压缩文件

    ```js
        let rs = fs.createReadStream(`./www/${pathname}`);
        let gz = zlib.createGzip()  //压缩  读写流
        rs.on('error',(err)=>{
            res.writeHead(404);
            res.end('no such file')
        })
        let ws = fs.createWriteStream(`./upload/${pathname}.gz`)
        ws.on('finish',()=>{
            res.setHeader('content-encoding','gzip')  //gz的返回头
            
            rs.pipe(gz).pipe(res)
            res.end('完成')
        })
        rs.pipe(gz).pipe(ws)
    ```

### 交互

- get

    ```js
        let {query,pathname} = url.parse(req.url,true)
    ```

- post

    ```js
        let arr = []
        req.on('data',(data)=>{
            arr.push(data)
        })
        req.on('end',()=>{
            let query = Buffer.concat(arr)
            let data = queryString.parse(query)
            //校验、数据库处理
        })
    ```

### 缓存

- last-modified 判断最后修改时间读取缓存

    ```js
        const http = require('http');
        const url = require('url');
        const fs = require('fs');
        const zlib = require('zlib');

        let server = http.createServer((req,res)=>{

            let {pathname} = url.parse(req.url);
            let gz = zlib.createGzip('gzip');
            fs.stat(`./www/${pathname}`,(err,data)=>{
                if(err){
                    console.log(err)
                    res.writeHead(404)
                    res.end('no such file');
                } else {
                    let {atime,mtime,ctime} = data;
                    //atime     access 访问时间
                    //mtimg     modify 修改时间
                    //ctime     change 修改时间
                    let modifiedTime = Math.floor(new Date(req.headers["if-modified-since"]).getTime()/1000);
                    let fileTime = Math.floor(new Date(mtime).getTime()/1000)
                    //因为 toUTCString()的时候损失精度   所以/1000并向上取整进行比较

                    let rs = fs.createReadStream(`./www/${pathname}`);
                    if(!req.headers["if-modified-since"] || modifiedTime < fileTime){
                        //没有 头  或者 过期  返回文件
                        res.setHeader('content-encoding','gzip');
                        res.setHeader('last-modified',new Date(mtime).toUTCString());  
                        //核心  缓存头
                        rs.pipe(gz).pipe(res)
                    } else {
                        res.writeHead(304)  //浏览器读取缓存
                        res.end()
                    }
                }
            })
        })
        server.listen(8080)
    ```
### cluster、os 多进程

- 多进程

    ```js
        //一个Cpu处理处理一个进程效率高
        //这些进程公用一个端口
        //其中一个进程宕了 不影响其他进程的
        
        const http = require('http');
        const cluster = require('cluster');
        const os = require('os')

        if(cluster.isMaster){   //主进程 则分裂进程
            for(var i = 0; i < os.cpus.length; i++){
                cluster.fork()
            }
        } else {
            http.createServer((req,res)=>{
                //do some thing 多线程
            }).listen(8080)
        }
    ```

### 链接数据库

- mysql

    ```js
        const mysql = require('mysql');
        let connection = mysql.createConnection({
            host:'111.229.241.56',
            port:'2020',
            user:'root',
            password:'root123',
            database:'test'
        })
        connection.connect()
        connection.query('select * from user',(err,res)=>{
            if(err){
                console.log(err)
            } else {
                console.log(res)
            }
        })
    ```

- 连接池

    ```js
    let pool = mysql.createPool({
        connectionLimit : 10,   //默认创建10个 一般够用
        host:'111.22.21.56',
        port:'3366',
        user:'root',
        password:'root',
        database:'test'
    })
    pool.getConnection((err,connection)=>{
        connection.query('select * from user',(err,res)=>{
            if(err){
                console.log(err)
            } else {
                console.log(res)
            }
        })
    })

    ```
### net

- 原生网络模块   http、tcp、websocket 的原型

    ```js
    //前台
    let ws = new WebSocket('ws://127.0.0.1:8080')

    //后台
    let netServer = net.createServer(socket=>{  //创建net

    })
    netServer.listen(8080)

    ```

### webscocket

- h5多端即时通信

    ```js
        //<script src="http://localhost:8080/socket.io/socket.io.js"></script>
        //let socket = io.connect('ws://127.0.0.1:8080');  //socket 服务
        //socket.emit('msg',xxx);       向后台发送
        //socket.on('msg',data=>{})     监听后台
        
        let socket = io.connect('ws://127.0.0.1:8080');
        let addMsg =  (msg)=>{......}
        $('.send').click((e)=>{
            let msg = $('#msg').val();
            if(msg){
                //向后台发送
                socket.emit('msg',msg);
                addMsg(msg)
            } else {
                return;
            }
        })
        socket.on('msg',str=>{
            addMsg(str)
        })
        socket.on('disconnect',()=>{
            $('#warning').css('display','block')
        })
        socket.on('connect',()=>{
            $('#warning').css('display','none')
        })

       
    ```

    ```js

        //socket.lisetn(http)   基于http搭建socket
        //socket.emit
        //socket.on 自定义、内置事件

        //connection链接成功
        //disconnect断开连接


        const http = require('http')
        const socket = require('socket.io');

        let server = http.createServer((req,res)=>{}).listen(8080);
        let socketServer = socket.listen(server)
        let wsos = []       //多个socket对象
        socketServer.on('connection',(socket)=>{
            console.log('链接成功' ,process.pid)
            wsos.push(socket)
            socket.on('msg',(str)=>{    //
                wsos.forEach((s)=>{
                    if(s != socket){
                        s.emit('msg',str)   
                    }
                })
            })
            socket.on('disconnect',()=>{
                console.log('断开连接',process.pid)
                let index = wsos.indexOf(socket)
                if(index != -1){
                    wsos.splice(index,1)
                }
            })
        })
    ```

### npm node package manager

- 安装、卸载 

    ```sql
    npm init           --初始化 package.json
    npm i              --根据package.json  下载项目需要的包 
    npm i -g package  --全局安装
    npm i -D package  --开发依赖安装 webpack打包等
    npm i -S package  --生产依赖安装 pm2等运行时需要的包

    npm uninstall package  --卸载包  可以-S -D 等
    npm update package     -- 更新包
    ```