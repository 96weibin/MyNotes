# [koa](https://koa.bootcss.com/)

- 洋葱工作原理  

    1. 根据app use 的先后顺序, 中间件 依次执行next之前的代码
    2. 最后 再从内向外  反向执行    next 后面的代码
    
    - 可以把一些日志、回调等放在next 后面执行

    ```js
        const Koa = require('koa')
        let app = new Koa()
        const middleware1 = async (ctx, next)=>{
            console.log('middleware1  start')
            next()
            console.log('middleware1   endding')
        }
        const middleware2 = async (ctx, next)=>{
            console.log('middleware2  start')
            next()
            console.log('middleware2  endding')
        }
        const middleware3 = async (ctx, next)=>{
            console.log('middleware3  start')
            next()
            console.log('middleware3   endding')
        }
        app
            .use(middleware1)
            .use(middleware2)
            .use(middleware3)
        app.listen(8888)

        //-------->>>>>>>>
        //middleware1  start
        //middleware2  start
        //middleware3  start
        //middleware3   endding
        //middleware2  endding
        //middleware1   endding
    ```

## helloword 

- new 

    ```js
        const Koa = require('koa')
        let app = new Koa()
        app.use(ctx =>{
            ctx.response.body = 'hello word'
        })
        app.listen(8888)
    ```

## 丰富的中间件


### 路由 [@koa/router](https://www.npmjs.com/package/koa-router)

- 原名koa-router  

    ```js
        const Koa = require('koa')
        const Router = require('@koa/router');

        let app = new Koa()
        let router = new Router()
        //get 、 post 、 put
        router.get('/router',ctx=>{
            ctx.body = 'hello router'
        })
        router.get('/api',ctx=>{
            ctx.body = 'hello api'
        })
        app
            .use(router.routes())
            .use(router.allowedMethods())  //筛选允许访问的方法
        app.listen(8888)
    ```

### koa-body 和 @koa/cors

- koa-body 与bodypasser 基本一样
- @koa/cors 设置跨域的中间件

    ```js
        const Koa = require('koa');
        const koaBody = require('koa-body');
        const Router = require('@koa/router');
        const cors = require('@koa/cors') 

        let app = new Koa();
        let router  = new Router()

        router.post('/post',ctx=>{
            let {body} = ctx.request;
            console.log(body)
            ctx.body = body
        })
        app
            .use(koaBody())     //要先body处理
            .use(cors({
                origin:'http://192.168.1.230:8080'  //允许跨域 的域名 
                //还可以设置方法等 
            }))         
            .use(router.routes())
            .use(router.allowedMethods())
        app.listen(8888)
    ```

### koa-combine-routers 路由整合、 static 静态文件 、 helmet 安全请求头

- 优雅的 整合多个router

    - app.js

        ```js
        //app.js
        const koa = require('koa');
        const router = require('./router/routers')  
        const path = require('path');
        const koaHelmet = require('koa-helmet');
        const koaStaticCache = require('koa-static-cache');
        const koaBody = require('koa-body')

        let app = new koa();

        app.use(koaHelmet()) //安全相关请求头
        app.use(koaStaticCache(path.join(__dirname,'./assets'),{
            maxAge:'60 * 60 * 24',  //path.join  比 reslove 好用
            gzip:true
        }))
        app.use(router())
        app.listen(8888)
        ```

    - router.js 

        ```js
        //router.js   整合router 
        const combineRouters = require('koa-combine-routers');

        const aApi = require('../api/aApi');
        const bApi = require('../api/bApi');
        const router = combineRouters(
            aApi,
            bApi
        )
        module.exports = router
        ```
    - api.js   

        ```js
        const Router = require('@koa/router');
        const controllerA = require('../controller/aController')

        let router = new Router()
        router.get('/a',controllerA)


        module.exports = router
        ```

### 包管理 npm-check-updates

- 检测package.json  内依赖是否有更新

    ```shell
    $ npm install -g npm-check-updates
    $ ncu --timeout=100000   # 这里ncu 总超时
    $ 
    ```


## 工作目录设计

1. 按照功能模块区分

    - src/
        - api/  
        - controller/
        - router/
        - app.js

## kao webpack配置

1. nodemon 热加载

    ```shell
    $ npx nodemon .\src\index.js  # npx 能直接遭到nodemon包
    ```

    - package.json 启动语句

    ```js
    "start": "nodemon src/index.js"
    // 启动语句 可以不写npx
    ```
2. ES6 语法支持     

----  参考webpack    以后再配置吧
