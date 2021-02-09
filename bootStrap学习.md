# bootStrap4

## 基本架构

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MO</title>
  <link rel="stylesheet" href="./dist/css/bootstrap.min.css">
  <link rel="stylesheet" href="./dist/css/index.css">
  <!-- 低于IE9的IE 加载下面两个js  分别时 支持Html5 支持媒体查询 -->
  <!--[if lt IE9]-->
    <script src="./dist/js/html5shiv.min.js"></script>
    <script src="./dist/js/respond.min.js"></script>
  <!--[endif]-->
</head>
<body>
  <header id="header">
     <div class="container-fluid">
        <div class="row">
            <div class="col-lg-4 left">left</div>
            <div class="col-lg-4 col-lg-offset-4 right">right</div>
          </div>
    </div>
  </header>
  <nav>
  <script src="./dist/js/jquery.min.js"></script>
  <script src="./dist/js/bootstrap.min.js"></script>
  <script src="./dist/js/index.js"></script>
</body>
</html>
```

## bootStrap中的标签

### 容器 container, container-fluid

  bootStrap4支持两种 container

  容器 | 长度
  -|-
  container | 两边留余地
  container-fluid | 父级宽度100%

### row col

  container 包 row 包 col

### 代码标签

```html
<pre>
  a
    a
      a
</pre>
<!-- pre 保持格式输出 -->

<code>aaa</code>

<!-- code inline形式输出 -->
```

### 表单

## bootStrap中的类

### col 类的 媒体查询范围以及container最大尺寸

类前缀 | 查询范围 | container最大宽度
-|-|-
.col | <576px | auto
.col-sm- | ≥576px | 540px
.col-md- | ≥768px | 720px
.col-lg- | ≥992px | 960px
.col-xl- | ≥1200px | 1140px

### 栅格 类

col的class | 说明
-|-
.col-ms-2 | 在12份中占几分
.col | 在12份中出去设置固定份数的其余部分，如果多个.col则平分剩余部分
.col-lg-offset-4 | 大屏位移4

栅格支持类似flex布局的 属性

row的class | 说明
-|-
.justify-content-start | 水平 贴左侧边框
.justify-content-center | 水平 居中
.justify-content-end | 水平 贴右侧边框
.justify-content-around | 水平 元素间距平均分 元素与边框间间距小一倍
.justify-content-between | 水平 贴两侧边框 其余间距平均分

### 排版类

类 | 说明
-|-
.lead | 使段落突出显示
.small | 设定小文本 (设置为父文本的 85% 大小)
.text-left | 设定文本左对齐
.text-center | 设定文本居中对齐
.text-right | 设定文本右对齐
.text-justify | 设定文本对齐,段落中超出屏幕部分文字自动换行
.text-nowrap | 段落中超出屏幕部分不换行
.text-lowercase | 设定文本小写
.text-uppercase | 设定文本大写
.text-capitalize | 设定单词首字母大写
.initialism | 显示在 \<abbr\> 元素中的文本以小号字体展示，且可以将小写字母转换为大写字母 (没有用)
.blockquote-reverse | 设定引用右对齐
.list-inline | 将所有列表项放置同一行
.pre-scrollable | 使 \<pre\> 元素可滚动，代码块区域最大高度为340px,一旦超出这个高度,就会在Y轴出现滚动条

### 表格类

#### table标签的类

类 | 说明
-|-|-
.table | 添加横向分割线
.table-hover | tbody悬停任意行hover
.table-striped | tbody 隔行换色
.table-bordered | 所有单元格添加border
.table-condensed | 表格变紧凑

#### tr、th、td的类

- 没啥用，就是一个公共的语义化的颜色类

类 | 说明
-|-
.active | 将悬停的颜色应用在行或者单元格上
.success | 表示成功的操作
.info | 表示信息变化的操作
.warning | 表示一个警告的操作
.danger | 表示一个危险的操作

### 表单类

#### 表单布局类

  向form与form组件添加类，控制排版。

  **优先移动端**从这里就可一看出来，默认的form组件的排列是纵向的，
  传统的pc端是横向的。

- 基本(垂直)布局

  ```html
  <!-- 这几个类是 bt的基本表单布局类 -->
  <form role="form">  
    <div class="form-group">  <!--调整间距-->
      <label>name</label>
      <input class="form-control"> <!--组件美化-->
    </div>
  </form>
  ```

- 水平布局

  ```html
  <form role="form" class="form-inline">  
      <div class="form-group">  <!--调整间距-->
        <label>name</label>
        <input class="form-control"> <!--组件美化-->
      </div>
    </form>
  ```

## bootStrap按钮

作用于 \<a\> \<button\> \<input\> 元素上

类 | 功能
-|-
---基础类--- | .btn
.btn | 按钮
---颜色类--- | .default,.primary,.success,.info,.danger,
.btn-default | default 默认标准样式按钮
.btn-primary | 原始样式按钮 深蓝色
.btn-success | 成功样式按钮 绿色
.btn-info | info样式 浅蓝色
.btn-danger | 危险样式 红色
---大小类--- | .btn-lg,.btn-sm,.btn-xs
.btn-lg | 大按钮
.btn-sm | 小按钮
.btn-xs | 超小按钮
---状态类--- | --
.btn-link | 链接样式的按钮  hover下划线。
.btn-block | 块级按钮(width100%)
.active | 被点击状态
.disabled | 禁止点击状态

## 下拉菜单 dropdowns

类 | 说明
-|-
.dropdown | 下拉菜单wrapper
.dropdown-menu | 下拉按钮
.dropdown-menu-right | 下拉按钮右对齐
.dropdown-header | 下拉菜单标题
.dropup | 指定向上弹出菜单
.disabled | 禁止项
.divider | 分割线
.open | 默认展开

### 下拉插件

- data-toggle="dropdown"  使下拉菜单可以下拉。

```html
<div class="dropdown">
  <button class="btn " type="button" id="#" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
        地址下拉
        <span class="caret"></span>
      </button>
  <div class="dropdown-menu" aria-labelledby="#">
    <a class="dropdown-item" href="#">abc</a>
    <a class="dropdown-item disabled" href="#">def</a>
    <h6 class="dropdown-header">h6</h6>
    <a class="dropdown-item" href="#">high</a>
    <div class="dropdown-divider">dirver</div>
    <a class="dropdown-item" href="#">opq</a>
  </div>
</div>
```

### 暂时先看这么多吧，

```js
  经过实践测试,感觉用bootstrap写一个项目还不是很好的感觉，因为要页面内大量的嵌套，以及设置响应式的大小，在需求响应式的项目里应该还不错
  不过在我现在的项目里不需要响应式，不如好好利用  css js 。ui框架 暂时先不用了。
```

```js
  bootstrap-select --- select组件
  bootstrap-datetimepicker --- 日历组件
```