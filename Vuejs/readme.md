# vue笔记

## 发展介绍

1. 框架顺序

    最先有  angular 然后有了  vue、react

2. vue特点

    1. 不要直接操作dom
    2. 数据为中心

## 简单使用

- 页面引入vue.js

```html
    <div class="box">
        姓名{{name}}    
        <!-- 双大括号输出data -->
    </div>

    <script>
        let vue = new Vue({
            el:'.box',   //管那个元素
            data:{
                name:'weibin'
            }
        })
    </script>
```

## 数据绑定 {{}}、 v-model、v-bind

1. 单向 {{}}        数据  => 视图   只能在标签内容输出
2. 双向 v-model     数据 <=> 视图
3. 属性 v-bind:     在标签属性位置输出

```html
    <div class="box">
        <input type="text" v-model='txt'>
        <span v-bind:title="txt">在title里输出</span>
        <!-- v-bind: 简写 : 属性上输出 -->
        <span>{{txt}}</span>
    </div>
    <script>
        let vue = new Vue({
            el:'.box',   //管那个元素
            data:{
                txt:''
            }
        })
    </script>
```


## vue 指令

指令 | 功能 | 简写 | 注意
-|-|-|- 
{{}} | 标签内输出 | | 仅在标签内有效
v-text | 输出字符串 | |
v-html | 输出html | | 
v-bind | 属性上输出 | : | json写style、arr写class
v-bind:[attr] | 绑定属性名是变量 | :[] | 变量 不能用表达式
v-model | 双向数据绑定 |  | 只有有value的标签才有用
v-on | 事件 | @ | 事件处理函数放在vm的methods
v-for | 遍历 | | 可以循环json、arr并且key、val两个参数
v-show | 显示、隐藏 | | diplay隐藏 false
v-if | 有、没有 | | 删除false 表单 display:none仍能提交
v-else | 
v-else-if | 

- :class、 :style 是vue 内部特殊处理了  JSON.Stringfy  join(' ')
- :class 可以设置  为对象 {active : isActive}，并且可以与 原生class并存
- v-model="checked" 多选  是否选中  true/false
- v-model="checkedName"  多选 选中的数组
- v-model="picked"  单选选中的 value值
- v-model="selected"  选择框 选择结果

## 事件 @

```html
    <div class="box">
                     <!-- v-on:click="sayHello" -->
        <div class="btn"  @click="sayHello">click me</div>
    </div>
    <script>
        window.onload = ()=>{
            let vm = new Vue({
                el:'.box',
                data:{

                },
                methods:{   //事件函数
                    sayHello(){
                        alert('hello');
                    }
                }
            })
        }
    </script>
```

### 修饰符

修饰符 | 功能
-|-
.stop  | 阻止冒泡
.capture | 捕获
.self | 点击自身生效
.prevent | 阻止默认事件
.once | 执行一次
.passive | 不阻止默认事件

---

按键修饰符 | 功能
-|-
.enter | 
.tab |
.delete | 
.esc |
.space | 
.up |
.down |
.left |
.right |
.ctrl |
.alt |
.shift |
.meta | window键
---

鼠标修饰符 | 功能
-|-
.left | 
.right | 
.middle | 

```html
    <form action="#" class="form" method="GET" @submit.prevent="stop">
                                        <!-- 阻止form的submit事件 -->
        <input type="text" name="user">
        <input type="pass" name="pass">
        <input type="submit" value="提交">
    </form>
    <script>
        new Vue({
            el:'.form',
            methods : {
                stop(){
                    console.log('click')
                }
            }
        })
    </script>
```

## 遍历 v-for :key

- v-for="val,key in arr" :key=""
- v-for="val,key in json" :key=""
- 可以对数组、json进行遍历
- 尽量都提供key  性能高

```html
 <ul class="oUl">
        <li v-for="user,index in users" :key="user.id">
            <!-- :key设置数据id给Vue利于dom操作，提高性能 
                id 与 dom 关联 
            -->
           <i>{{index}}</i> 姓名:{{user.name}}-年龄：{{user.age}}
           <!-- 遍历users 的 val、key -->
        </li>
    </ul>

    <script>
        let vm = new Vue({
            el:'.oUl',
            data:{
                users : [
                    {id:8, name:'weibin1',age:'18'},
                    {id:9, name:'weibin2',age:'19'},
                    {id:11,name:'weibin3',age:'20'}
                ]
            },
        })

    </script>
```

## 显示隐藏 v-show、v-if

- v-if 控制是否存在dom
- v-show 控制dom的display   如果displaynone的表单仍会被提交

```html
    <div class="box">   
        <input type="button" @click="showBox" value="click">
                      <!-- v-if="flag" -->
        <div class="block" v-show="flag"></div>
    </div>

    <script>
        let vm = new Vue({
            el : '.box',
            data : {
                flag : true,
            },
            methods : {
                showBox(){
                    this.flag = !this.flag;
                }
            }
        })
    </script>
```

## 模块组件

- 全局组件     Vue.component   先声明再new
- 局部组件  var item = {temp....}     实例{components:{item:item}}

```html
    <todo-item></todo-item>
    <!-- 使用模块组件 -->

    <script>
        Vue.component('todo-item',{ //声明组件
            template:'<h2>item组件</h2>'  //组件模板
        })
        let app = new Vue(....)    //先声明后new
    </script>
```

- 组件传参     v-bind 传入   props 接收

```html
    <div id="app">
        <ul>
            <li v-for="student in students">
                <detail :student='student'></detail>    
                <!-- 给模块传入 student -->
            </li>
        </ul>
    </div>

    <script>
        Vue.component('detail',
        // detail模块
            {
                template:`<div><h1>{{ student.name }}同学</h1><h2>{{ student.age }} 岁了</h2></div>`,
                props:['student']
                //接收 student 作为参数
                data:funciton(){    //组件data为闭包对象  相互隔离
                    return {
                        count : 0 
                    }
                }

            }

        )
        let app = new Vue({
            el:'#app',
            data:{
                students : [
                    {
                        name:'xiaoming',
                        age:15
                    },
                    {
                        name:'xiaohong',
                        age:16
                    },
                    {
                        name:'xiaozhang',
                        age:17
                    }
                ]
            },
        })
```

### 组件间传值 

- :abc = "abcd"  ->   props:['abc']   父传向子
- @click = $emit('dosome') -> @dosom="fDosom($event)"  子传向父
- 组件内部 触发 组件上的事件  改变父级的变量  $emit

```html
    <div id="app">
        <div :style="{fontSize : oFontSize + 'px'}">
            <item :abc='title' v-on:dosome="change($event)"></item>
        </div>
    </div>
    <script>
        Vue.component('item',{
            template:`  <div class="item">
                            <h2>{{abc}}</h2>
                            <button v-on:click="$emit('dosome',1)">plus</button>
                        </div>
                        `,
            props:['abc'],
        })

        let app = new Vue({
            el:"#app",
            data:{
                title:'世界真美好',
                oFontSize:24
            },
            methods: {
                change(){
                    this.oFontSize += 1
                }
            },
        })
    </script>

```

#### v-model        做了好多事

- v-model   不需要 :value  和  props :[value] 
- 也不需要   @input="dosome"   

```html
    <div id="app">
        <div>
            <custom-input v-model = "searchtext"></custom-input>
            {{searchtext}}
        </div>
    </div>
    <script>

        Vue.component('custom-input',
        {
            template:`<div>
                <input @input="$emit('input',$event.target.value)">
            </div>`,
        })

        let app = new Vue({
            el:"#app",
            data:{
                searchtext:''
            },
        })
    </script>
```

## filter

- 过滤 转变  简单的计算

```html
<template lang="html">
    <span title="时间">{{this.data.time|cDate}}</span>
</template>
<script>
export default {    
    filters:{
        cDate(t){       //time 转 date
        let d = new Date(t);
        return d.toLocaleDateString();
        }
    },
}
</script>
```



## 计算后数据computed

- 有缓存,重复的不需要再次计算,性能略高,计算数据同时又get、set,绑定在data上 this
- 当data与computed的变量名重复，computed失效
- computed 内容为空时视图渲染  v-if  阻止渲染即可

```html
    <div class="box">
        姓:<input type="text" name="first" v-model="first"><br>
        名:<input type="text" name="last" v-model="last"><br>
        姓名:<input type="text" name="name" v-model="name"><br>
        <!-- 可以用v-model绑定计算数据 -->
    </div>
    <script>
        new Vue({
            el:'.box',
            data:{
                first: '',
                last : '',
            },
            computed:{
                //简写模式 仅 get
                // name(){ 
                //     return this.first + this.last
                // }
                name:{
                    set : function(name){
                        this.first = name[0];
                        this.last = name.substring(1);
                    },
                    get : function(){
                        return this.first + this.last
                    }

                }
            }
        })
    </script>
```

## 监听watch

- 监听变量的变化,监听函数传参 旧新 参数值
- vm.$watch(attr,(nval,oval)=>{})

    ```html
    <div class="box">
        <input type="text" name="" id="" v-model="a">
    </div>
    <script>
        new Vue({
            el:'.box',
            data:{
                a:''
            },
            watch:{ //监听数据变化
                a(nVal,Oval){
                    console.log('从',oVal,'变到',nVal)
                }
            }
            
        })
    </script>
    ```

## 路由vue-router

- 引入 vue.js vue-router.js
- 根据不同的地址调用不同的组件
- spa

关于路由

1. 由hash完成
2. router-link 就是一个a标签
3. router-view 是个容器站位标签
4. 一个组件也是一个完整的vm data要写成函数 return json
5. 激活的router-link 有专属的class  router-link-active
6. $route 路由信息
7. this.$router   路由事件动作


### 基础使用

```html
<router-link to="/user">买家平台</router-link>
<router-link to="/company">卖家平台</router-link>
<!-- 
    实际是a标签
    <a href="#company">卖家平台</a> 
    to path
    <router-view>  是一个空站位
-->
<router-view></router-view>

<script>
let router = new VueRouter({
    routes : [  //路由表
        {
            path : '/user', //router-link的路径
            component : {   //component也是一个vm
                template : `<div>买家{{count}}<span @click="sayHi">sayHi</span></div>`,
                data: function(){
                    return {
                        count:'120'
                    }
                },
                methods:{
                    sayHi(){
                        alert('hello 买1件')
                    }
                }
            }
        },
        {
            path : '/company',
            component : {
                template : `<div>卖家{{count}}<span @click="sayHi">sayHi</span></div>`,
                data: function(){
                    return {
                        count:'12'
                    }
                },
                methods:{
                    sayHi(){
                        alert('hi 卖10件')
                    }
                }
            }
        },
    ]
})
let vm = new Vue({
    el : '.box',
    router : router
})
</script>
```

### 路由带参数 

- /a/:id
- $route.params.id

```html
<div class="box">
    <router-link to="/article/1">文章1</router-link>
    <router-link to="/article/2">文章2</router-link>
    <router-link to="/article/3">文章3</router-link>
    <router-view></router-view>
</div>

<script>
    let router = new VueRouter({
        routes:[
            {
                path:'/article/:id',
                component:{
                    template:`<div>文章ID:{{$route.params}}</div>`
                    // $route 当前路由的信息
                }
            }
        ]
    })

    let vm = new Vue({
        el:'.box',
        router 
    })


</script>
```


### 监听路由 watch $route 或 beforeRouteUpdata

    监听$route 的变化

- watch

```html
    新闻
    <div class="box">
        <router-link to="/news/1">国内新闻</router-link>
        <router-link to="/news/2">世界新闻</router-link>
        <router-view></router-view>
    </div>


    <script>
        let router = new VueRouter({
            routes:[
                {
                    path:'/news/:id',
                    component:{
                        template:'<div>{{$route.params}}</div>'
                    }
                }
            ]
        })

        let vm = new Vue({
            el : '.box',
            router,
            watch:{
                $route(nVal,oVal){
                    console.log('从',oVal.params,'到',nVal.params)
                }
            }
        })
```

- beforeRouteUpdata

```html
    世界新闻
    <div class="box">
        <router-link to="/news/china">国内新闻</router-link>
        <router-link to="/news/tokio">日本新闻</router-link>
        <router-view></router-view>
    </div>

    <script>
        let router = new VueRouter({
            routes: [      //这里是routes
                {
                    path: '/news/:place',
                    component: {
                        template: `
                        <div>{{$route.params.place}},今天的新闻是。。。</div>
                        `,
                        beforeRouteUpdate(to, from, next) {
                            if (confirm('离开本页面更改将不会被保存')) {
                                next()  //很像promise
                            }
                        }
                    }
                },

            ]
        })

        let vm = new Vue({
            el: '.box',
            router
        })
    </script>
```

### 嵌套路由   children[]

    多级路由，使用router的嵌套实现,上级路由 <router-view>

```html
    <div class="box">
        <router-link :to={name:'hello'}>用户信息</router-link>
        <!-- t -->
        <router-link to="/user/img">用户头像</router-link>
        <router-link to="/company/info">公司信息</router-link>
        <router-link to="/company/img">公司头像</router-link>
        <router-view></router-view>
    </div>

    <script>
        let router = new VueRouter({
            routes : [
                {
                    path:'/user',
                    component:{
                        template:'<router-view></router-view>',
                    },
                    children:[
                        {
                            path:'info',
                            name:'hello',   //命名为hello的二级路由
                            component:{
                                template:'<div>用户信息</div>'
                            },
                        },
                        {
                            path:'img',
                            component:{
                                template:'<div>用户头像</div>'
                            }, 
                        }
                    ]
                },
                {
                    path:'/company',
                    component:{
                        template:'<router-view></router-view>',
                    },
                    children:[
                        {
                            path:'info',
                            component:{
                                template:'<div>公司信息</div>'
                            },
                        },
                        {
                            path:'img',
                            component:{
                                template:'<div>公司头像</div>'
                            },
                        }
                    ]
                },
            ]
        })

        let vm = new Vue({
            el:'.box',
            router

        })

    </script>
```

### 命名路由

- 例 见上
- 只能简化拼写,容易产生误会搞错，暂先不用
- :to{name:'', params:{},query:{}}



## vue2

### 创建webpack、vue-cli项目

### 安装 

```shell
# vue3 
npm i -g @vue/cli webpack
## 创建项目目录
vue create my-project   # 项目名不能大写

# vue2
npm i -g vue-cli webpack
## 创建项目目录
vue init webpack my-project

npm i -g @vue/cli-service-global
# 运行单个vue 文件
```

### 模板创建

- 使用Vue.component  或 直接在vue实例中写 component
- 使用porps为组件声明{{变量}},
- 在组件上通过 行间 变量=xx  或 :变量=xx 进行赋值

```html
    <div id="app">
        <panda here="china"></panda>
        <!-- 通过行间  here="" 给panda模板赋值 -->
    </div>

    <div id="app2">
        <panda v-bind:here="message"></panda>
        <!-- 通过 : 将data中的值 传至模板 -->
    </div>


    <script type="text/javascript">
        var app=new Vue({
            el:'#app',
            components:{
                "panda":{
                    template:`<div style="color:blue;">Panda from {{ here }}.</div>`,
                    props:['here'], //组件 有一个变量  here

                },

            }
        })

        //使用v-bind指令获取数据
        var app2=new Vue({
            el:'#app2',
            data:{
                message:'SiChuan'
            },
            components:{
                "panda":{
                    template:`<div style="color:red;">Panda from {{ here }}.</div>`,
                    props:['here']
                }
            }
        })
    </script>
```

#### 父子组件间通信

- 父组件   可以传函数给子集像闭包

```html
<template>
    <div class="">
        已选中：{{count}}件
        <ul>                    
            <ListItem v-for="(item, i) in items" :data="item" :key="i" :add="addOne" :remove="removeOne"></ListItem>
            <!--  :data、:add、:remove会传递给子组件,子组件通过this.$attrs.来获取 -->
        </ul>
    </div>
</template>
<script>
    import ListItem from './list_item'  //引入子组件
    export default {
        data() {
            return {
                count:0,
                items:[
                    {name:'玩具',price:80,sales:850},
                    {name:'衣服',price:280,sales:600}
                ]
            }
        },
        components:{
            ListItem
        },
        methods:{
            addOne(){   //通过闭包传递参数给子组件
                this.count ++
            },
            removeOne(){
                this.count --
            }
        }
    }
</script>

<style scoped>

</style>
```

- 子组件

```html
<template>
    <li>
        <h3>
            <!-- checkbox双向绑定 true、false再点击时会响应 -->
            <input type="checkbox" v-model="flag" >
            {{flag}}{{data.name}}
        </h3>
        <span>¥{{data.price}}</span> 
        <span>月售{{data.sales}}件</span>
    </li>
</template>

<script>
    export default {
        // props:['item'],
        data() {
            return {
                data:{},//类似于初始化，名字随意
                flag:false,
            }
        },
        mounted(){
            //this.$attrs.xxx 获取父级传给子集的内容
            this.data = this.$attrs.data;
            console.log(this.$attrs);
        },
        watch:{
            flag(n){
                if(n){
                    //传递add 是函数、利用闭包 使子集向父级发数据
                    this.$attrs.add();
                } else {
                    this.$attrs.remove();
                }
            }
        }
    }
</script>

<style lang="css" scoped>
</style>
```


### 生命周期钩子

- 即应用的创建、销毁、等等状态触发的函数。。。。名字叫的很玄乎

事件顺序|钩子函数|监听
-|-|-
0 | beforeCreate | 创建之前
1 | created | 创建之后
2 | beforeMount | 挂在之前(挂载el)
3 | mounted | 挂在之后
4 | beforeUpdate | 虚拟dom渲染前
5 | updated | 虚拟dom渲染后
6 | beforeDestroy | 销毁之前
7 | destroyed | 销毁之后

### [axios](http://www.axios-js.com/zh-cn/docs/#axios-post-url-data-config)

- 安装

    ```shell
    $ cnpm i -S axios #生产环境需要
    ```

- 使用
    可以在main.js内将axios对象放在Vue对象的protoype上,在其他模块内通过this.axios进行调用,axios是一个promise对象

    ```js
    //基础使用           //success,err
    axios.get('url').then(res=>{},res=>{})//res会根据服务器返回头自动解析 json数据

    //try catch、 async await、 生命周期一起使用
    async mounted() {
        try {
            this.items = (await this.axios.get('http://127.0.0.1:8081/list')).data;
        } catch (error) {
            alert("数据加载失败请刷新重试")
        }
    },
    ```
- post请求  

    post请求  前台会   先发送一个  options 请求,导致  跨域问题
    需要设置  严格跨域头

    - 后台跨域设置

    ```js
    server.use(async (ctx,next)=>{      //允许跨域
        console.log(ctx.request.url)
        ctx.set('Access-Control-Allow-Origin','*')
        // ctx.set('Access-Control-Allow-Methods','*')
        ctx.set('Access-Control-Allow-Headers','*')
        // ctx.set('Access-Control-Allow-Headers', 'X-Requested-With');
        // ctx.set('Access-Control-Allow-Headers', 'Content-Type');
        // ctx.set('Access-Control-Allow-Headers', 'mytoken');
        ctx.response.status = 200;
        await next()
        })
    ```
    
    - 发送post请求

    ```js
    this.axios.post('http://127.0.0.1:8090/sendMail',{
        //第二个参数可以直接传body
      data:{
        to:'1643960119@qq.com',
      }
    })
    ```


### [fetch](https://developer.mozilla.org/zh-CN/docs/Web/API/Fetch_API/Using_Fetch)

- ES6原生，官方对ajax的封装,返回promise对象

    ```js
    //返回promise json方法也返回promise等待两次 获得结果
    this.items = await (await fetch('http://127.0.0.1:8081/list')).json()
    ```
    
    - post 请求， post请求时 同axios 需要后台设置  跨域

    ```js
    let res = await (await fetch('http://127.0.0.1:8090/sendMail',{
        method:'post',
        body:JSON.stringify({to:'1643960119@qq.com'}),  //body需要转格式
        headers: new Headers({  //注意json 格式需要设置请求头
        'Content-Type': 'application/json'
        })
    })).json()
    console.log(res)
    ```


### 状态管理 vuex

- vuex 官方工具

    - state     ---     存储状态对象, 全局唯一的数据对象
    - mutations(突变) ---     修改状态的操作  被vue监控,
    - actions(动作)   ---     提交mutation 通过this.$store.dispatch(act,arg)触发 
    - getters   ---     读取state里的值 可以通过getter dispatch 网络请求等
    - modules   ---     $store下分 state, action不分

- 安装

    ```shell
    npm i -S vuex
    ```

 - 使用

    - action 适合 其他异步操作 较少使用

        main.js

        ```js
        import Vuex from vuex;

        Vue.use(Vuex);  //先use再new
        const store = new Vuex.Stroe({  //创建store对象  
        //S 大写
            strict:true,    //严格模式,只能通过 mutation改变state
            state:{         //全局状态对象
                count:0
            }
            mutations:{     //修改函数
                addMutation(state,arg){     //mutation 可以直接调用state
                    state.count += arg
                }
            },
            actions:{       //触发修改函数
                addAction(store,arg){       //挂在Vue上的store对象
                    store.commit(' ',arg)//可以出发多个mutation
                }
            }
            getters:{

            }
        })
        new Vue({
            store,  //注册到vue对象
        })
        ```

        list_item.vue

        ```html
        <template>
            <input type="button" value="加5" @click="fnAdd">
            <input type="button" value="减2" @click="fnMinus">
        </template>

        <script>
            export default{
                methods:{
                    fnAdd(){
                        this.$store.dispatch('addCount',5); //分发给addCount,传参5
                    },
                    fnMinus(){
                        this.$store.dispatch('minusCount',2);
                    }
                }
            }
        </script>
        ```

        list.vue

        ```html
        <template>
            {{state.count}}
            <listItem"></listItem">
        </template>

        <script>
            import listItem from './list_item'
            export default{
                data:{
                    state:this.$store.state 
                    //可以监控对象的改变，不能再.cunt
                }
                components:{
                    listItem
                }
            }
        </script>
        ```

   - getter 适合 数据交互 
    
        vue内通过computed监控this.$store.getters.xxx的变化，直接使用计算值<br>
        getters 的 xxx参数state,而且可以调用store.dispatch进行异步操作的action<br>
        action 进行axios或fetch 得到数据 commit 到 mutation 对state进行修改

        main.js
    
        ```js
        const store = new Vuex.Store({  //new store 对象
        strict:true,  //严格模式,只能通过action触发mutation修改state
        state:{       //全局唯一共享的  状态对象
            arr:[]
        },
        mutations:{
            setArr(state,arg){
            state.arr = arg
            }
        },
        actions:{ 
            async loadArr(store,arg){
            let commit = store.commit;
            arg = await (await fetch('http://127.0.0.1:8081/a')).json();
            commit('setArr',arg)
            }
        },
        getters:{
            abc(state){
            if(state.arr.length === 0){
                store.dispatch('loadArr')//读取外面的store
            }
            return state.arr;
            }
        }
        });

        ```

        list.vue

        ```html
        <template>
            <div class="">
                <h3>{{getter}}</h3>
            </div>
        </template>
        <script>
            export default {
                data() {
                    return {
                    }
                },
                computed: { 
                    getter(){
                        return this.$store.getters.abc;
                    }
                }
            }
        </script>
        ```
    - module 拆分store


        ```js
        const store = new vuex.Store({
            strict:true,
            state:{},
            mutations:{},
            actions:{},
            getters:{},
            modules:{       //拆分user相关的store
                user : {
                    state:{
                        name:'weibin',
                        age:17
                    },
                    mutations:{
                        graw(state){
                            state.age ++;
                        }
                    },
                    actions:{
                        graw({commit}){
                            commit('graw')
                        }
                    },
                    getters:{
                        getName(state){
                            return state.name
                        },
                        getAge(state){
                            return state.age
                        }
                    }
                }
            }
        })
            
        ```
        ```html
        <template lang="html">
            {{name}}
            {{age}}
            <input type="button" value="涨一岁" @click="graw"/>
        </template>
        <script>
            computed:{
                name(){         //state内容需要加一层
                return this.$store.state.user.name;
                },
                age(){
                return this.$store.getters.getAge;
                }
            },
            methods:{
                graw(){     //action不需要加一层
                            //且 内外设置同名  action会都执行
                this.$store.dispatch('graw')
                }
            }
        </script>
        ```

## build

npm run build webpack 编译出dist 目录 将dist目录放入 服务器即可完成上线


## 一些注意点

1. 全局libs
```html
    src/libs/comment.js 内写公用的方法，filter等，在需要的地方  import， 使用
```

2. 加载数据报错

```html

跨组件传参时，template 先加载，temp中调用 this.$attrs的属性再调用的时候就会报错

v-if="data"  数据未加载不引入temp

```

3. lazyload   异步模块

```js
    components:{
        detail:()=>import('./detail') 
    }
    //这样detail 模块  不会被和其他模块打包到一起，
    //在需要时现加载
```

## 动画

- 动画 可以钩子配合transition

类名 | 功能
-|-
*-enter{} | 初始样式
*-enter-active{} | 过程样式
*-enter-to{} | 结果样式
*-leave{} |
*-leave-active{} |
*-leave-to{} |

- 使用animate npm i -S vue2-animate
- transition-grop 只能控制里面一层过度 name 设置过渡效果

```html
<template>
  <div id="app">
    <input v-for="(list,index) in anList" type="button" :value="'show' + index" :key="index" @click="cBox(index)">
    <transition-group name="fadeLeft" >     
    <!-- 左侧淡出过度效果 -->
      <div class="box" v-for="(list,index) in anList" :key="index" v-show="list.show">{{index}}</div>
    </transition-group>
  </div>
</template>
<script>
import 'vue2-animate/dist/vue2-animate.min.css'
//引入css webpack自动编译
export default {
  name: 'App',
  data() {
    return {
      anList : [
        {show:true},
        {show:true},
        {show:true},
        {show:true},
        {show:true}
      ]
    }
  },
  methods:{
    cBox(i){
      this.anList[i].show = !this.anList[i].show
    }
  }
}
</script>
```

## 测试

1. 单元测试 unit   - 一个vue组件
2. 端到端测试 e2e - 整个程序
3. 代码覆盖率


## Vue3

- 优化
    dom渲染优化
    ssr 服务器渲染 优化
    tree shaking
    由ts重写

vue template Explorer


### 项目升级  vue add vue-next 

### custom  renderer

```js
//通过  引入 @vue/runtime-core   引入 各种vue3相关组件
    import {createRenderer} from '@vue/runtime-core'

        const {crateApp} = createRender({

    })

    //结合canvas     使vue生成的      渲染到canvas上
```

- createElement\ insert \ pathProp