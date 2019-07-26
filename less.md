# less

less是Css预处理语言 增加变量、mixin、函数等特性，使CSS更易维护和拓展

运行在 Node 或 浏览器端

## 常量

```less
    @color:#f40;
    @font-size:12px;
    #header {
        color: @color;
        font-size: @font-size;
    }
    #footer {
        color: @color;
        font-size: @font-size * 2;
    }
```

>编译后——>>

```css
#header {
    color: #f40;
    font-size: 12px;
}
#footer {
    color: #f40;
    font-size: 24px;
}
```

- 使用 @: 定义变量  在后面时候用这个定义的变量进行样式设置,之后重构直接更换 变量即可
- 而且 变量可以进行计算

## 混合

```less
.rounded-corners (@radius: 5px){
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

>编译后 ——>>

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

## 嵌套

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

> 编译后——>>

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

- 和dom结构一样的编写css  节省很多dom 选择器的冗余

## 客户端使用

```html
<link rel="stylesheet/less" href="./css/index.less">
<script src="less.js" type="text/javascript"></script>
```

## 命令行使用

### npm安装

```shell
npm i -g less
npm i -d less
```

### 编译

```shell
lessc styles.less
```

- 将less编译成Css后 传递给stdout 保存

```shell
lessc style.less > styles.css -x
```

- 将 less 编译成Css 保存在 styles.css中 并压缩