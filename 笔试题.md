# web前段工程师招聘试题

## Css部分

1. span标签添加了样式"menu" 时显示为一个菜单图形如 '≡' ,span 标签添加了样式 "close" 时显示为一个关闭图标  如 "X" (不要调整HTML,不要使用图片,通过对形状的位移或旋转来绘制图形)

* 我的答案
```css
.menu{
    display: block;
    width: 20px;
    height: 20px;
    box-sizing: border-box;
    border-top: 1px solid black;
    border-bottom: 1px solid black;
    background: #ddd;
}
.menu::after{
    content: '';
    display: inline-block;
    width: 1px;
    height: 20px;
    background: black;
    transform-origin: 0 0;
    transform: rotate(-90deg);
    position: relative;
    top: 10px;
}


.close{
    display: block;
    width: 20px;
    height: 20px;
    background: #ddd;
}
.close::before{
    content: "";
    display: inline-block;
    box-sizing: border-box;
    width: 1px;
    height: 28px;
    background: black;
    transform-origin: 0 0;
    transform: rotate(-45deg)
}
.close::after{
    content: "";
    display: inline-block;
    width: 1px;
    height: 28px;
    box-sizing: border-box;
    background: black;
    position: relative;
    left: 19px;
    transform-origin: 0 0;
    transform: rotate(45deg)
}
```
```html
<span class="menu"></span>
<span class="close"></span>
```
![](http://96weibin-blog.oss-cn-beijing.aliyuncs.com/18-11-2/25942628.jpg)

2. 居中对齐：固定宽高的容器如 
```html
<ul id="gallery">
    <li style="width:200px;height:200px;"></li>
</ul>
```
要放置宽高比未知、宽高未知(小于容器宽高)的图片,怎么让图片在父容器水平和垂直方向均居中,(加分表现：兼容IE8)

* 我的答案

```css
#gallery li{
    display: flex;
    justify-content: center;
    border: 1px solid black;
    align-items: center;
}
```
```html
<ul id="gallery">
    <li style="width:500px;height:500px;">
        <img src="./pic.jpg" alt="">
    </li>
</ul>
```
![](http://96weibin-blog.oss-cn-beijing.aliyuncs.com/18-11-2/26000301.jpg)




