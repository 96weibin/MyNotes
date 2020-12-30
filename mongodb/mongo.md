# [mongo](https://www.mongodb.com/2)

- noSQL数据库 异构数组-----数据结构随便
- 性能低  数据限制少  验证工作量大

## 运行

- windows 运行服务端

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






