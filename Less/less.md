# less

less是Css预处理语言 增加变量、mixin、函数等特性，使CSS更易维护和拓展

运行在 Node 或 浏览器端

## 使用

1. 客户端使用

    ```html
    <link rel="stylesheet/less" href="./css/index.less">
    <script src="less.js" type="text/javascript"></script>
    ```

2. 命令行使用

    - npm

    ```shell
    $ npm i -g less
    $ npm i -d less
    ```


    - 编译
    ```shell
    lessc styles.less
    # 将less编译成Css后 传递给stdout 保存
    ```

   ```shell
   lessc style.less > styles.css -x
   # 将 less 编译成Css 保存在 styles.css中 并压缩
   ```

## 特性

### 常量

- @定义变量

    ```less
        @red: #f40;     //常量
        @red-hover: darken(@red, 10%);  //表达式
        @font-size:12px;
        @selectorName: #box;  //选择器名
        @propertyName: border;  //属性名


        #header {
            color: @red;
            font-size: @font-size;
            @{propertyName}: 1px solid pink;
        }
        
        #footer {
            color: @red;
            font-size: @font-size * 2;  //表达式
        }
        @{selectorName}{
            color: pink;   
            background: $color;     // 变量当作 property
        }
        @{selectorName}:hover{
            color: @red-hover;
        }
    ```

- 编译后

    ```css
    #header {
        color: #f40;
        font-size: 12px;
    }
    #footer {
        color: #f40;
        font-size: 24px;
    }
    #box {      
        color: pink;
    }
    #box:hover {
        color: #cc3600;
    }
    ```

- 使用 @: 定义变量  在后面时候用这个定义的变量进行样式设置,之后重构直接更换 变量即可
- 而且 变量可以进行计算
- 支持 lazy, 不需要 在最前面定义变量 在使用。

### 混合

- 传参重构

    ```less
    .rounded-corners (@radius: 5px){

        /*
         可以传多个参数
         @arguments 获取到全部传参, 用@arguments 直接进行赋值
        */
        border-radius: @radius;
        -webkit-border-radius: @radius;
        -moz-border-radius: @radius;
    }

    #header {
        .rounded-corners;
    }

    #footer {
        .rounded-corners(10px);
    }
    ```

- 编译后

    ```css
    #header {
        border-radius: 5px;
        -webkit-border-radius: 5px;
        -moz-border-radius: 5px;
    }

    #footer {
        border-radius: 10px;
        -webkit-border-radius: 10px;
        -moz-border-radius: 10px;
    }
    ```

- 继承另一个 class 的全部css  

### 嵌套

- 层级嵌套,clearly

    ```less
        #header {
            h1{
                color:pink;
            }
            nav{
                width: 100px;
                height: 50px;
                .search {
                    background: blue;
                }
            }
        }
    ```

- 编译后
- 
    - 和dom结构一样的编写css  节省很多dom 选择器的冗余
    ```css
    #header h1{
        color:pink;
    }
    #header nav{
        width: 100px;
        height: 50px;
    }
    #header nav .search{
        background: blue;
    }
    ```
  
  ### & 代替父级选择器

  ```less
  .wrapper{
      .box1{    //.wrapper .box1
          //xxxx
      }
      &.box1{   //.wrapper .wrapper.box
          //zzzz
      }
      & .box1{  //.wrapper .wrapper .box
          //yyyy
      }
  }
  ```

### @import


```less
@import (inline, less, once,) './01变量名.less';
@import (once) './03public.less';
```

- reference: 引用变量 用来编辑 但不引入文件
- inline: 把import的文件放在最前面，不引用变量
- less : 当作less 文件，忽略拓展名
- css ： 当作css文件， 忽略拓展名
- once: *default* 只引入一次
- multiple： 多次引入
- optional： 可选择的， 文件没有加载不到就 continue， 宽容。


### extend & mixin

- extend 继承

    ```less
    .my-inline-block {
        display: inline-block;
        font-size: 0;
    }
    .thing1 {
        &:extend(.my-inline-block);
    }
    .thing2 {
        &:extend(.my-inline-block);
    }


    //----output----

    .my-inline-block,
    .thing1,
    .thing2 {
        display: inline-block;
        font-size: 0;
    }
    ```

- mixin 混合

    ```less
    .my-inline-block() {
        display: inline-block;
        font-size: 0;
    }
    .thing1 {
        .my-inline-block();
    }
    .thing2 {
        .my-inline-block();
    }

    //----output----

    .thing1 {
        display: inline-block;
        font-size: 0;
    }
    .thing2 {
        display: inline-block;
        font-size: 0;
    }
    ```
    - mixin 期望都有括号

- 函数形式 mixin

```less
@plugin "06less-plugin";
@themestr: theme();

.theme-mixin(light){
    background-color: white;
    color: black;
}
.theme-mixin(dark){
    background-color: black;
    color: white;
}

.ag-theme-balham{
    font-size: 30px;
    .theme-mixin(@themestr);    //mixin
}
```

### @plugin

- plugin

```js
module.exports =  {
    install: function(less, pluginManager, functions){
        functions.add('pi', function(){
            return Math.PI;
        })

        functions.add('theme', function(){
            // let theme = localStorage.getItem('theme');
            theme = 'dark';
            return '.' + theme;
        })
    }
}
```

- use plugin

```less
@plugin "06less-plugin";
@theme: theme();

.show-me-pi{
    value: pi();
}

.dark{
    background-color: black;
    color: white;
}

.light{
    background-color: white;
    color: black;
}
```