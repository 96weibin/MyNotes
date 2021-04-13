# [mongo](https://www.mongodb.com/2)

- noSQL数据库 异构数组-----数据结构随便
- 性能低  数据限制少  验证工作量大

## [安装](https://www.runoob.com/mongodb/mongodb-linux-install.html)
    
- [使用docker 安装](https://hub.docker.com/_/mongo)

    1. 拉去镜像

        ```shell
        $ docker pull mongo
        ```
    2. docker run 

        ```shell
        $ docker run mongo
        ```

    1. 通过 .yml文件配置安装

    ```yml
    version: '3.1'
    services:

      mongo:
        image: mongo
        restart: always
        container_name: "mongo-test"
        ports:
          - 10050:27017
        environment:
          MONGO_INITDB_ROOT_USERNAME: root
          MONGO_INITDB_ROOT_PASSWORD: rootpass
    ```

    2. 运行yml文件

    ```shell
    $ docker-compose up -d  # -d在后台运行
    ```

    3. 停止容器

    ```shell
    $ docker-compose stop
    ```
## 常见的场景设计方法

1. 内嵌

    - 数据可以使嵌套式的json
    - 减少了关联表的使用
    - 对不常变得属性使用

2. 父子引用

    - 一对多  父存子id


3. 反范式

    - 通过直接在父里面   冗余子  
    - 根据实际情况设计


## 运行

- windows服务 运行服务端

    ```shell
    $ # 注意运行命令的终端需要有  管理员权限

    $ ./mongod.exe --port 8091 --logpath D:\db\log.txt --logappend --noauth --install --serviceName weiBin_Mongo_8091 --serviceDisplayName "weiBin's Mongo" --serviceDescription 'a mongodb for weibin' --dbpath D:\db --directoryperdb

    $ #cmd service 查看服务    首次启动服务
    ```

- node 客户端链接

    ```js
    const MongoClient = require('mongodb').MongoClient;
    const url = 'mongodb://localhost:8091';
    //url 须是mongodb协议
    const dbName = 'test';
    MongoClient.connect(url, function(err, client) {
    const db = client.db(dbName);
    //promise                        条件, 处理函数
    db.collection('usersTable').find({},(err,data)=>{
        data.toArray((err,data)=>{
            console.log(data)
        })
    })
    client.close();
    });

    ```

- koa saync 链接

    ```js
    const Koa = require('koa');
    const MongoClient = require('mongodb').MongoClient;
    (async function(){
        let data;
        try {
            let client = await MongoClient.connect('mongodb://localhost:8091')
            let db = client.db('test')
            // find   toArray 都是异步 返回promise
            data = await (await db.collection('usersTable').find({})).toArray()
        } catch (error) {
            console.log('连接错误')
        }
        server.use(async (ctx,next)=>{
            ctx.response.body = data;
        })
    }())
    let server = new Koa();
    server.listen(8888);
    ```

## 运行指令 

- mongod.exe 服务端

    参数 | 功能 | 详情
    -|-|- 
    --port | 端口设置 | 
    --bind_ip | 绑定网卡对应ip | 多网卡时使用
    --maxConns | 最大连接数 | 
    --logpath | 日志文件地址 | 
    --logappend | 设置追加日志 | 重启服务等
    --pidfilepath | pid文件 | 防止启动多次
    --noauth | 登录不需要认证 |
    --httpinterface | 开http接口 | 
    --rest | restful接口 | restful 基于http
    --install | 安装windows服务 | 自动后台运行
    --remove | 删除windows服务 |
    --serviceName | 服务名 | 不能重复
    --serviceDisplayName | 对外展示服务名 | 随意
    --serviceDescription | 服务描述 | 
    [集群模式]() |----负载均衡-----|-------------------
    --master | 主节点 | 主节点不工作只分配
    --slave | 从节点 | 
    --source | 主节点地址 | 从指定主 ip:port
    --keyfile | pem文件地址 | 主从节点公钥 证书
    [安全相关]() | |
    --sslMode | 加密模式 | 
    --sslPEMKeyFile  | pe7文件地址 |
    [存储选项]() | |
    --dbpath |数据存储地址|
    --directoryperdb | 每个库一个文件 | 方便移动
    -noprealloc | 每个库是否预留空间 |
    --nssize | ns节点 命名节点大小 |
    --quota | 每个库大小的上限 | 
    --upgrade | 数据库升级 | 
    --repair | 修复数据 | 

- mongo.exe 客户端

    ```shell
    $ #登录
    $ .\mongo.exe localhost:8091
    ```

    参数 | 功能 | 详情
    -|-|- 
    use | 创建库 | 
    db | 当前数据库
    db.xxx | 创建表 | collection
    db.xxx.find() | 查找 | 
    db.xxx.insert() | 插入 | 
    db.xxx.delete() | 删除 | 
    db.xxx.update({条件},{变量}) | 更新 | 
    
    - 通过 Many One 来规范查询  deleteOne 、updateMany。。。


- 查询规则

    规则 | mongo | sql
    -|-|-
    与 , | {name:'x',age:'y'} | name = 'a' AND age = 'y'
    或 or | {$or:[xxx,yyy,zzz]} | xxx OR yyy OR zzz
    小于 $lt |{age:{$lt:17}}) | age < 17
    小于等于 $lte |  |
    大于 $gt | |
    大于等于 $gte |  |
    不等于 $ne | |

    - 判断不会进行类型转换


## 备份和恢复

- 备份  mongodump

    ```shell
    $ docker ps | grep mongo   # 查看启动的mongo服务  some-mongo

    $ docker exec -it some-mongo mongodump -h  -u -p -d -o /temp/test
    #                               端口  用户 密码 数据库 输出目录  
    # 备份出来的 文件在docker容器内

    $ docker cp 3ac745b2a7e7:/temp/test /tmp/test
    # 从docker 容器3ac745b2a7e7  中拷贝出来
    ```

- 恢复 mongorestore

    ```shell
    $ docker exec -it some-mongo mongorestore -h localhost --dir /tmp/test
    # 需要把  备份文件拷贝到  docker容器内  恢复
    ```



## mongoose


- 说明

    - mongoose  类似 hibernate  定义类型模板   schema

    - schema  是 规定表   字段、类型的类

    - model 是表


- 使用

    ```js
    const mongoose = require('mongoose')
    
    mongoose.connect('mongodb://106.13.116.236:10050/test', {useNewUrlParser: true, useUnifiedTopology: true});

    //连接数据 mongodb://用户名:密码@106.13.116.236:10050/test

    //不知道为什么  还要添加 ?authSource=admin  难受
    const Cat = mongoose.model('Cat', { name: String });        //创建并链接connection
    const kitty = new Cat({ name: 'jiafei' });            
    kitty.save().then(() => console.log('meow'))   //save保存

    ```

- 开发配置

    - lib/mongoose.js

        ```js
        //数据库连接
        const mongoose = require('mongoose')
        const dbConfig = require('../conf/dbConfig');


        mongoose.connect(dbConfig.DB_URLL +'/test', {useNewUrlParser: true, useUnifiedTopology: true});

        mongoose.connection.on('connected',()=>{
            console.log('mongodb 链接成功')
        })
        mongoose.connection.on('error',(err)=>{
            console.log('mongodb 链接失败')
        })
        mongoose.connection.on('disconnected',()=>{
            console.log('mongodb 链接断开')
        })
        module.exports = mongoose
        ```

    - model/User.js

        ```js
        //定义 schema  导出 model
        const mongoose = require('../lib/mongoose')

        let Schema = mongoose.Schema;
        let userSchema = new Schema({
            name:String,
            age:Number,
            sex:Number,
            msg:String
        })

        let usersModel = mongoose.model('users',userSchema)

        module.exports = usersModel
        ```

    - CURD/test.js

        ```js
        //只需要引入 对应的model--collection  增删改查
        const usersModel = require('../model/User')
        // 新增
        let addUser = async(user)=>{
            let aUser = new usersModel(user)
            let res = await aUser.save()
            console.log(res)
        }

        let user1 = {
            name:'weibin',
            age:17,
            sex:1,
            msg:'世界真美好'
        };
        // addUser(user1)

        //删除
        let deleteOneUser = async(user)=>{
            let res = await usersModel.deleteOne({
                age:18
            })
            console.log(res)
        }
        deleteOneUser()
        //修改
        let mudateOneUser = async()=>{
            let res = await usersModel.updateOne({
                name:'weibin'
            },{
            age:18
            })
            console.log(res)
        }
        // mudateOneUser()
        //查找
        let findUser = async(user)=>{
            let res = await usersModel.find()
            console.log(res)
        }
        // findUser()
        ```