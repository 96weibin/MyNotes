# [Vue 3](https://cn.vuejs.org/guide/introduction.html)

- [options](#options)
- [composition](#composition)
- [class style](#classStyle)

## 安装

```shell
$ npm init vue@latest
```
> node > V16.0.0

## 模板语法

- 页面插值， 表达式， 调用函数， 插入html， bind, 事件, 修饰符

1. 一次绑定多个值

    ```html
    <script setup lang="ts">
    const obj = {id: "only", class: "many"}
    </script>
    <template>
    <div v-bind="obj">div1</div>
        <!-- 
        <div id="only" class="many">div1</div>      
        -->
        <!-- 简写不可以 -->
    </template>
    ```
2. 动态属性方法

    ```html
    <script setup lang="ts">
    import { ref } from 'vue';


    const event = ref("click");
    const sayHi = ()=>{
    console.log(event.value);
    }
    </script>
    <template>
    event: <input type="text" v-model="event">
    <button @[event]="sayHi()">{{event}}</button>
    </template>
    ```
    > [] 中括号使用变量当作 属性，方法名

3. Directives 指令



## API 风格

### Options API 选项是API <span id="options">

- options API, 2.0
    ```html
    <script>
    export default {
    // data() 返回的属性将会成为响应式的状态
    // 并且暴露在 `this` 上
    data() {
        return {
        count: 0
        }
    },

    // methods 是一些用来更改状态与触发更新的函数
    // 它们可以在模板中作为事件监听器绑定
    methods: {
        increment() {
            this.count++
        }
    },

    // 生命周期钩子会在组件生命周期的各个不同阶段被调用
    // 例如这个函数就会在组件挂载完成后被调用
    mounted() {
        console.log(`The initial count is ${this.count}.`)
    }

    props{      //接受父级bind的值，
        msg: String,    //生命属性
    }
    }
    </script>

    <template>
    <button @click="increment">Count is: {{ count }}</button>
    </template>
    ```
    > props 接受父级bind的值

### Composition API 组合式API <spen id="composition">


- composition API 3.0

    ```html
    <script setup>
    import { ref, onMounted, computed } from 'vue'

    // 响应式状态
    const count = ref(0)

    // 用来修改状态、触发更新的函数
    function increment() {
    count.value++
    }

    // 生命周期钩子
    onMounted(() => {
    console.log(`The initial count is ${count.value}.`)
    })

    //computed 返回集合
    const forms = computed(()=>{})

    //监听 prop 执行回调
    const prop = ref(true);
    watch(prop, ()=>{})

    //接受父级bind值
    defineProps({       //defineProps 编译时宏 无需引入，
        msg: String,    //声明了 msg 变量
        obj: Object
    })
    </script>

    <template>
    <button @click="increment">Count is: {{ count }}</button>
    </template>
    ```


    >1. setup 标记
    >2. 生命周期需要  引入执行
    >3. defineProps 接受父级bind的值

### [class style](https://class-component.vuejs.org/) <span id="classStyle">

- 拆分vue的ts 作为类引入， data为class的属性，method 为class 的成员方法， 其他@Option 提供

1. Parent.vue

    ```html
    <template>
        <div id="app">
            <el-aside :class="{ expend: isOpenAside, close: !isOpenAside,  }">
                <Aside :msg="msg" @changeAside="changeAside"></Aside>
            </el-aside>
        </div>
    </template>

    <script setup lang="ts">
    import Aside from "./components/Aside/Aside.vue";   //setup 在不需要component 中声明
    import { computed, onMounted, shallowRef, reactive, ref, watch } from "vue";
    import { useStore } from "vuex";

    let isOpenAside = ref(true);    //响应变量
    let msg = "home msg"
    let $store = useStore();    //$store

    const changeAside = ()=>{       //emit callback
        isOpenAside.value = !isOpenAside.value
    }

    watch($store.state, (n, o) => {     //watch store
        switch (n.currentTab) {
            case Tabs.overview:
            componentId.value = Overview;
            break;
            case Tabs.boards:
            componentId.value = Boards;
            break;
            case Tabs.pipelines:
            componentId.value = Pipelines;
            break;
            default:
            break;
        }
    });
    </script>
    ```
2. Child
    - Child.vue
    ```html
    <template>
    <div class="aside">
        <div class="navs">
            <div class="navBtn" @click="onChangeTab(btn.id)" v-for="btn of btns" :key="btn.id">
                <div class="mainNav">
                <img :src="btn.url" alt="btn.label" />
                <span>{{ btn.label }}</span>
                </div>
            </div>
        </div>
        {{msg}} 
        <!-- //父组件传来 -->
        <button class="extend" @click="onExpand">>></button>
    </div>
    </template>

    <script lang='ts'>
    import Aside from './Aside'     //拆分的ts
    export default Aside            //需要export 给 template使用
    </script>
    ```
    - Child.ts
    ```ts
    import { Vue, prop, Options } from 'vue-class-component';   //干活的组件
    import { Store, useStore } from 'vuex';
    import { Tabs } from "../../services/homeService";

    @Options({
        props: {        //props 单向的 不要用来修改
            msg: string     //接受从父级传来的  msg string 
        },
        emits: ['changeAside']  //$emit 事件
    })
    export default class Aside extends Vue{ //需要继承 Vue
        public msg: string = "";    //props 定义了仍需要 声明 可以赋默认值
        public btns:any[] = [];     //变量  即视为 data
        private $store: Store<any> = useStore();    //store
        onExpand() {            //成员方法 即 视为 methods
            this.$emit('changeAside')      //$emit 不需要声明 直接触发自定义事件
        }
        onChangeTab(tab) {
            this.$store.dispatch("tabAction", tab);     //store dispatch
            console.log("change to tab" + tab)
        }

        //各种生命周期钩子
        beforeCreate(){        
            console.log("before create")
        }
        created(){
            console.log('created')
        }
        beforeMount(){
            console.log('beforeMount')
        }
        mounted(){
            this.initNavBtns();
        
        }

        initNavBtns(){
            this.btns = [
                {
                    url: require("@/assets/imgs/overview.png"),
                    label: "overview",
                    id: Tabs.overview,
                },
                {
                    url: require("@/assets/imgs/boards.png"),
                    label: "boards",
                    id: Tabs.boards,
                },
                {
                    url: require("@/assets/imgs/pipelines.png"),
                    label: "pipelines",
                    id: Tabs.pipelines,
                },]
        }
        beforeUpdate(){
            console.log("beforeUpdate")
        }
        updated(){
            console.log("updated")
        }
        activated(){
            console.log("activated")
        }
        deactivated(){
            console.log("deactivated")
        }
        beforeUnmount(){
            console.log("beforeUnmount")
        }
        unmounted(){
            console.log("unmounted")
        }
    }
    ```

## SFC single file component 语法规范

## 响应式

### options API 

- options 模式的 data, methods 就是响应式的

### composition API 

- reactive 

```html
<template>
  <div class="about">
    <h2>{{state.count}}</h2>
    <button @click="addCount()">addCount</button>
  </div>
</template>

<script lang="ts">
import { reactive } from 'vue';
export default{
  setup() { //特殊生命周期
    const state = reactive({count: 0})  //reactive 创建响应式对象或数组
    const addCount = ()=>{
      state.count ++;
    }
    return {
      state,  //暴露出 方法和  变量
      addCount
    }
  } 
}
</script>
```
> setup 函数内定义的变量，方法都要返回到外边使用

- \<script setup\>

```html
```


## 组件间传值

1. 父->子
    - props
    - v-mode: e="" --- $emit(update:e, xxx)
    - slot

2. 子->父
    - emit

> prps 设计上  单项数据流， 但传递的 数组对象 是可以被修改的， Vue 期望不要修改它， 而是通过 emit 实现
