# Aurelia
 
- mvvm 框架

## 安装

1. cli 安装
    ```shell
    $ npm i -g aurelia-cli
    ```
  
    ``` shell
    $ au new 
    ## select your option
    ```
2. 运行

    ```shell
    $ au run --open # 通过cli 启动
    # 或者  npm 添加参数启动
    $ npm start -- --open --host 127.0.0.2 --port 8888 
    ```
## main

1. base  配置启动、安装插件 等
    
    ```ts
    //默认配置函数  configure
    export function configure(aurelia:Aurelia){
        aurelia.use
            .standardConfiguration()  //使用默认配置
            .developmentLogging()    // 以debug模式启用控制台输出日志
            .globalResources('resources/my-component');  //全局资源
        aurelia.start().then(()=>aurelia.setRoot()); //aurelia.start()启动  返回 promise
        //aurelia.setRoot()  渲染根组件   app
        
        // 自定义根组件   my-root.html/my-root.ts  将内容注入到  #some-element标签下
        aurelia.start().then(()=>{aurelia.setRoot('my-root',document.getElementById('some-element'))})
    }
    ```
2. global资源

   1. globalResources
  
    ```ts
    aurelia.use
        .globalResources('resources/my-component')
    ```

    1. feature 多个resouces组成一个功能
    
    ```ts
    //main
    aurelia.use
        .feature('my-feature')
    ```
    ```ts
    //my-feature.ts
    export function configure(config){
        config.globalResources(['my-component1','my-component2','my-component3','etc'])
    }
    ```
3. plugin

    ```ts
    aurelia.use
        .plugin('my-plugin',pluginConfiguretion)
    ```


## 组件

1. 定义组件
    - 新建同名的 ts, html 会做为一个组件
    - 组件的view html 全部内容需要写在 templete 标签内
    - require 组件需要手动引入css
    ```html
    <template>
        <require from="./hello.css"></require>
        <h1>Hello page</h1>
        <div>${msg}</div>
        <input type="text" value.bind="msg">
    </template>
    ```
    ```ts
    // 需要注意  export class  而不是 export default class
    export class Hello{
        constructor(public msg:string){
        }
    }
    ```
2. 引入组件

    - require 不写拓展名 表示作为组件
    - 组件名子 hello 和 ./hello.ts 的类名相关
    - html 标签不区分大小写
    ```html
    <template>
        <require from="./hello"></require>
        <hello></hello>
    </template>
    ```

3. 命名中使用中划线与下划线

  1. 文件命名  可以用**中划线** 和 下划线, 推荐中划线 
  2. ts 导出的类名  不能用划线
     1. 类名不支持中划线，html标签不支持下划线
     2. 类名使用驼峰类似css 属性名可以将 驼峰和中划线相关联
  3. 推荐 
     1. 文件中划线
     2. 类名驼峰
     3. 标签中划线

4. 组件传值

    1. 子组件vm @bindable attr 声明属性
    2. 子组件v  ${attr} 属性插值
    3. container <xxx attr = 'xxx' 给子组件传值

    ```ts
    import { bindable } from 'aurelia-framework';
    export class BindTest {
        @bindable to = "world"
        public msg = "hello"
        constructor(public ableFlag:boolean){
        }
        leave(){
            this.msg = 'Goodbye'
        }
    }
    ```
    ```html
    <template>
        <h2>${msg} ${to}!</h2>
        <button click.trigger="leave()"></button>
    </template>
    ```
    ```html
        <require from="./bind-test"></require>
        <bind-test to="jackson"></bind-test>
    ```

    - @bindable 传值 和 复用函数

    位置 | 传值 | 传函数 | 对比
    -|-|-|-
    container | art="xxx" | fun.bind="xxx" | 
    vm | @bindable art | @bindable fun | 




5. 注册组件    TODO  2,3,4 版本问题都不能用
   
    1. 普通的组件 require 
    2. 在mail.js引入的 公共组件   

        ```ts
        import {xxx} from './xxx'
        Aurelia.register(xxxx)
        ```
        TODO 文档这么写，可是不能这么用
    3. 统一入口组件文件夹
        - comment/registry.ts
        ```ts
        export * from './xxx'
        export * from './yyy'
        export * from './zzz'
        ```
        - main.ts
        ```ts
        import * as globalComponents from './compment/registry'

        Aurelia.register(globalComponents)
        ```
    4. 给组件改名字  @customElement
        
        ```ts
        import { bindable, customElement } from 'aurelia-framework';
        import template from './com-header.html'
        @customElement({
            name:'newName',
            template
        })
        ```
        - 当前版本  只传 string新名字
        ```ts
        @customElement('newName')
        ```

TOTO @watch  local Template


### 组件生命周期

- 洋葱模型   >>>>.<<<<

    生命周期 | 说明 | 通常用法
    -|-|-
    constructor | 构造函数 | 初始化代码
    define | 类似@customElement 阶段 | 组件引入时
    hydrating | 添加DI注册 | 。。。。
    hydrated | 
    -| 构建过程完成 |-
    created | 构建完成 | 
    binding | 组件绑定属性后，视图渲染之前 | 
    bound | 组件与视图绑定后 | 
    attaching | 组件的html 被调用 | 
    **attached** | 组件 挂在完毕子组件 | 对组件进行操作
    detaching | 组件删除被调用 | 
    unbinding | 解除数据绑定 与创建时相对应 | 
    dispose | 组件从内存中清除 | 


## 模板语法 binding

### 插值

- ${}可以用在属性上， attr.bind
  
    类型 | 方法 | demo
    -|-|-
    文本 | ${} | 
    html | innerhtml.bind='xxx' | 
    属性 | prop.bind='xxx' 属性内也可以${} | 
    样式 | style.bind='xxx' | css 同vue以obj形式

### 事件绑定

- 事件类型

    元素 | 事件
    -|-
    inp | change 、 input
    other | click

- 绑定方式

    - 需要注意的 事件函数 需要 ()来执行

    绑定方式 | 特点
    -|-
    trigger | 绑定
    delegate | 委托(冒泡)
    capture | 捕获阶段

- 委托demo

    ```html
    <button click.trigger="sayHi()">sayHi</button>

    <ul click.delegate="numberOff($event)">
      <li>1</li>
      <li>2</li>
      <li>3</li>
      <li>4</li>
      <li>5</li>
    </ul>
    ```
### 函数绑定 @bindable

- 组件获取容器的方法，可以实现重写
  
  - app.ts
  
    ```ts
    //定义一个方法
    introduce(){
        console.log('here is app')
    }
    ```
  - app.html
  
    ```html
    <require from="./fn-bind-test"></require>
    <fn-bind-test som-fun.bind="introduce"></fn-bind-test>
    <!-- 将intrduce 方法 以 somFun 的 bindable 传入子组件-->
    ```

  - fn-bind-test.ts
    
    ```ts
    @bindable somFun;
    //这时子组件 就获得了 this.somFun = intrduce
    //获得到 父组件的函数  需要使用、重写等都不会影响  app.ts中的方法
    this.fomFun()
    ```

### ref

    - 感觉就是获取 xxx 的对象


1. element.ref
    
    - element.ref 可以简写成 ref="xxx"
    - 此元素的dom对象 可以直接在 html内调用，到ts里调用需要声明同名变量
    
    ```html
    <input type="text" element.ref="sss">${sss.value}
    ```
    
    ```ts
    //组件内接受 sss 需要声明来使用
    sss:HTMLInputElement;
    sayHello(){
        console.log(this.sss.value)
    }
    ```


2. view-model.ref, view.ref, controller.ref 获取组件的vm，v, c

    ```html
    <!-- 获取子组件上的对象 -->
    <o-head view-model.ref="myVM"  view.ref="myV" controller.ref="myC"></o-head>
    <button click.trigger="sayHi(myVM,myV,myC)">click</button>
    ```
   ```ts
    sayHi(...arg){
        console.log(arg)
    }
   ```

## 语句

1. 循环语句  repeat for 
   
   ```html
   <li repeat.for="friend of friends">${friend}</li>
   ```

    遍历类型 | demo | 注意
    -|-|-
    数组 | repeat.for = 'item of items' | fo in
    遍历数组通过index 进行操作 | repeat.for = 'i of items.length' | value.bind="$parent.items[i]" 进行操作
    遍历10次 | repeat.for = 'i of 10' | 


TODO json对象 不能遍历需要   一个转换器 没实现

    
### 绑定

1. 属性绑定

属性 | 功能 | 特点
-|-|-
.bind | 自动绑定属性 | form 双向，其他单向
.one-way | 单向绑定 | 
.two-way | 双向绑定 | 
.to-view | vm -> v |
.from-view | v -> vm | 
.one-time | 一次绑定 | 

## 上下文属性

属性 | 内容
-|-
$this | dom自己
$parent | dom parent
$event | dom事件
$index | 重复模板中的 索引
$first | boolean
$last | boolean
$even | b
$odd | b




## 生命周期

- 组件生命周期

阶段 | 功能
-|-
constructor() | 第一次调用 vm 的 constructor
created() | 创建
bind() | 数据绑定
attached() 附属| 组件被添加到 Dom中
detached() | 组件从dom中移除
unbind() | 组件移除后 


## injection

- static 的语法糖

- 注入依赖

    ```ts
    import ServiceClass from './ServiceClass'
    import {inject} from 'aurelia-framework'     // inject 注解

    export class App{
        constructor(public oS:ServiceClass){
        }
        attached(){
            this.oS.doSomething()
            //this.oS 是new 过的实例
        }
    }

    ```
    - inject 一个类,可以得到 实例

- 同时传入多个依赖

    ```ts
    import aService from './aService'
    import bService from './bService'
    import cService from './cService'
    import {inject} from 'aurelia-framework'
    @inject(aService,bService,cService)
    export class App {
        constructor(public aS:aService, public bS:cService,public cS:bService){
    }
    attached() {
        //以 inject 的顺序  传入 constructor
        this.aS.introduce()  //here is aService
        this.bS.introduce()  //here is bService
        this.cS.introduce()  //here is cService
    }
    ```
    - inject 的类会作为参数传入constructor 且是有序的




## compose  和  PLATFORM.moduleName

```ts

aurelia.use
    .featrue(PLATFORM.moduleName('url'))  //感觉类似 path.reslove  配合webpack 的模块路径   动态构建
```


```html         
<compose view-module.bind="oVM" view.bind="oV" ref="xxx" view-module.ref="yyy">

<compose view="../comment/com-header.html" ${view-model="../comment/com-header.ts"}></compose>


compse  获取 main 里定义的 
```


测试 view.bind  和 view-model.bind