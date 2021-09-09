# 设计模式

- 设计模式是面向对象编程开发人员长时间实验总结出来的solution，设计模式是软件工程的基石。

## 设计模式的类型

## 设计模式的六大原则

TODO 上面的两项还不能很好的理解暂时不写

## 单例模式 singleton pattern

- Vuex 类似全局唯一实例减少命名冲突，降低重复定义减少资源浪费，

- 判断实例是否已经创建过，实力已经被创建过,则返回将实例返回

```ts
    class Single {
        constructor(name){
            this.name = name;
            this.instance = null;
        }
        static getInstance(name){
            if(!this.instance){
                this.instance = new Single(name)
            } 
            return this.instance;
        }
    }

    console.log(Single.getInstance('zme'));     //Single { name: 'zme', instance: null }
    let d = Single.getInstance('BL');           
    console.log(d)                              //Single { name: 'zme', instance: null }
```

## 发布订阅模式

- DOM事件，也是一种发布订阅

