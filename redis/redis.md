# redis

- 开源免费
- k-v 数据库
- 高性能持久化  ： 断电存储在宿主机
- 多数据结构
- 支持事务

> 数据库的操作，可以先缓存在内存中，过一会一次搞进数据库

## 使用场景

1. 缓存
2. 计数，  高并发


## 安装 

1. docker-compose.yml  文件配置

    - docker-compose.yml

    ```yml
    version: "3"    # docker-compose 版本
    services:
      redis-test:   # 名
        image: "redis"
        restart: always     # 自动重启
        container_name: "redis-test"   # 便于管理的名字
        ports:
            - 15001:6379     # 端口映射
        volumes:      # 将容器内数据 映射到宿主机
            - /home/redistest:/data
        command: ["redis-server","--requirepass","123456"]  # 设置密码

    ```

    - 运行 compose
    ```shell
    $ docker-compose up -d   # 根据yml文件  下载执行
    ```

    - 查看log 

    ```shell
    $ docker logs -f redis-test
    ```

    ```shell
    $ docker exec -it redis-test /bin/bash
    # 对redis-test 交互式终端

    $ redis-cli
    # 启动命令工具
    $ auth  123456
    # 用户密码  连接
    $ quit # 退出命令行
    $ exit # 退出容器

    ```
  

2. 或者通过docker run 命令

    ```shell
    $ docker run -itd --restart=always --name redis-test -p 15001:6379 -v /home/redistest:/daat redis redis-server -requirepass 12345
    ```


## [Redis Cli](http://doc.redisfans.com/)

- connect相关

    cli | demo | 功能
    -|-|-
    select | select num | 切换数据库 默认 0-15
    auth | auth xxx | 通过密码登录
    --- | config set requirepass xxx | 设置密码xxx

- key相关

    cli | demo | 功能
    -|-|-
    keys | keys abc* | 查找abc相关的key
    del |  del key [key ...] | 通过key删除数据
    exists | exists key  | 判断是否存在

- String相关 

    cli | demo | 功能
    -|-|-
    append | append k v | 尾部追加 kv   
    set | set k v | 设置kv
    get | get k | 获取k的v
    incr | incr k | k num 自增
    decr | decr k | k num 自减

    - 没有初始化的数据,append、incr 都会予以初始化

    ```js
    client.set('key', 'value' , 'EX',100) //100秒过期
    ```

- Hash相关

    - 很像json   不过hash value 不能再是hash

    cli | demo | 功能
    -|-|-
    hset | hset key field value [field value ...] | 设置hash表
    hget | hget key field | 获取 hash 某个field对应值
    hgetall | hgetall key | 获取hash 全部 kv kv kv kv
    hmset | 
    hmget | 


- List相关

    - 很像数组,允许重复

    cli | demo | 功能
    -|-|-
    lpop | | 左删
    rpop | | 右删
    lpush | | 左插
    lpushx | | 左插 ，没key 不执行
    rpush | rpush k v[v...] | 右侧插入
    rpushx | rpushx k v[v...] | 右侧插入、没有k 则不执行


- set相关

    - 集合中 member 

    cli | demo | 功能
    -|-|-
    sadd | sadd k member[member ...] | 向集合中添加
    smembers | smembers key | 查看对应集合
    scard | scard key | 返回集合length
    sdiff | sdiff key1 key2 [key ...] | 返回 除去 key1 集合 与 key2集合 交集  的剩余

- pub/sub 发布订阅

    cli | demo | 功能
    -|-|-
    publish | | 发布 
    subscribe | | 订阅

- 事务

    cli | demo | 功能
    -|-|-
    multi | multi | 事务开启标志
    exec | exec | 执行与multi之间所有命令
    discard | discard | 取消与multi之间所有命令


- 服务器相关 

    cli | demo | 功能
    -|-|-
    config | | 
    client | client list | 查看
    ---| client kill hp | 关闭hp对应链接 
    slowlog | | 查询日志
    flushdb | | 清空当前db
    flashall | 慎用 | 删除全部db

## 备份恢复

bgsave 

## GUI

- [another redis desktop manager](https://github.com/qishibo/AnotherRedisDesktopManager)


## 集成node  [redis模块](https://www.npmjs.com/package/redis)

- conf/redisConfig.js
    
    - 配置文件
        ```js
        module.exports = {
            host:'106.13.116.236',
            port : '15001',
            password:'weibin',
            detect_buffers:true,
            retry_strategy: function(options) {
            if (options.error && options.error.code === "ECONNREFUSED") {
                // End reconnecting on a specific error and flush all commands with
                // a individual error
                return new Error("The server refused the connection");
            }
            if (options.total_retry_time > 1000 * 60 * 60) {
                // End reconnecting after a specific timeout and flush all commands
                // with a individual error
                return new Error("Retry time exhausted");
            }
            if (options.attempt > 10) {
                // End reconnecting with built in error
                return undefined;
            }
            // reconnect after
            return Math.min(options.attempt * 100, 3000);
            }
        }
        ``` 
    - option 常有用属性 

        属性 | 默认值| 功能 
        -|-|-
        detect_buffers | false | true 返回回调
        retry—strategy | fun | 配置超时、断开等提示

- lib/redis.js

    ```js
    const redis = require('redis')
    const {promisify} = require('util')
    const option = require('../conf/redisConfig')


    const client = redis.createClient(option); 
    const getAsync = promisify(client.get).bind(client);
    const getHAllasync = promisify(client.hgetall).bind(client);

    //字符串
    const getValue = (k)=>{
        return getAsync(k)
    }
    //hash
    const getHValue = (k)=>{
        return getHAllasync(k)
    }
    //字符串 && hash
    const setValue = (k,v)=>{
        if(typeof k !== 'string' || v === null || v === ''){
            console.log(v)
            return "arguments error please send key:sting,value"
        }
        if(typeof v === 'string'){
            client.set(k,v)
        } else if(typeof v === "object"){
            Object.keys(v).forEach((item)=>{
                client.hset(k, item, v[item], redis.print)
            })
        }
    }
    module.exports = {
        client,
        getValue,
        getHValue,
        setValue
    }
    ```

   