# Vue 3

## SFC语法规范

## class style

- 拆分vue的ts 作为类引入， data为class的属相，method 为class 的成员方法， 其他Option 提供

### demo

1. parent 

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
2. child
    - .vue
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
    - .ts
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