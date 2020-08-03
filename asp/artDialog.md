# artDialog

- 经典、优雅的网页对话框控件

## 引入

``` html
    <script src="jquery.js"></script>
    <script src="dialog.js"></script>

```
- artDialog 是基于jquery的 可以如上  直接引用 
  或使用npm安装 在引用

```node.js
$ npm install --save-dev art-dialog
```

```js
var dialog = require("art-dialog");
```

## 总结

### 属性

```html
title      ：        : 标题
content    ：        : 内容
statusBar  : string  : 状态条


quickClose ：boolean : 点击空白关闭       
autofocus  : boolean : 是否自动获取焦点

okValue    : string  : 对话框ok的标识字符
ok         : fun     : ok执行的函数 如果设置返回值false则导致按钮将不会被关闭 且只有返回false可以保持不被关闭
cancelValue:         : 对话框取消的标识字符
cancel     : fun     : cancel执行的函数 如果设置返回值false则导致按钮将不会被关闭
cancelDisplay: bool  : 是否显示 取消按钮  

width      : str/num : 设置宽度
height     : str/num : 设置高度
skin       : str     : 设置 class
id         : str     : 设置i-id   dialog.get() 进行获取
apdding    : str     : 设置padding
fixed      : boolean : 设置是否相对视口定位   默认 false
align      : str     : 设置对话框其他元素的  对其方式

onshow     : fun     :
onclose    : fun     :
onbeforeremove: fun  : 在remove之前
onremove   :  fun    : 
onfocus    : fun     : 焦点事件
onreset    : fun     : 对话框重置事件



button     : array   : 可以包含多个按钮  每个按钮是一个 对象，对象的属性如下

 名称        类型          描述
    value       string      按钮显示文本
    callback    function    回调函数 this指向 dialog对象 ，执行完毕默认关闭与注销对话框，
                            close->remove 若return false 组织关闭与注销
    autofocus   boolean     默认false 是否自动聚焦
    disabled    boolean     默认 false 是否禁用

```

### 方法   this.

```html
close()    : 关闭  有返回值可继续链式调用
remove()   : 移除  没有返回值
show()     : 展示 传参为dom则对话框 吸附到 dom上，若在事件中show传参为 event则根据event.pageX&&pageY进行定位
showModal(): 以模态框展示
content()  : 设置 内容  支持  html  string htmlElement
title()    : 设置 标题  支持 string
width()    : 设置 宽度
height()   : 设置 高度
reset()    : 手动刷新对话框位置
focus()    : 聚焦
blur()     : 失交
addEventListener() : 添加事件
removeEventListener() : 删除事件
dialog.get() : 获取 某个ID的 对话框
dialog.getCurrent() : 获取当前的对话框
```


## 例子

### 简单实例

#### 普通对话框

- dialog传入对象包含参数  对于基础对话框可以设置 title content 分别是 弹出框的标题  和内容  之后 dialog.show();来执行
```js
    var d = dialog({
        title:"欢迎";
        content:"欢迎使用artDialog对话框";
    })
    d.show();
```

#### 状态对话框

- 模态框  dialog函数传参还是一样的,不同的是在执行的时候  调用.showModal();

```js
    var d = dialog({
        title:"message",
        content:"<input autofocus>"
        });
    d.showModal();
```

#### 气泡浮层

- 可以点击空白从而  使对话框关闭  可以给html添加 id为 quickref-bubble 这样  气泡浮层就会出现在这附近 
```js
    var d = dialog({
        content:"hello world",
        quickClose: true //点击空白处关闭
    })
    d.show(document.getelementById('quickref-bubble'));
```
#### 添加按钮

- 可以设置  okValue 与 cancaleVale 根据点击情况分别执行 ok 与 calcel函数

```js
    var d = dialog ({
        title : '提示',
        content : '按钮毁掉函数返回false 则不许关闭',
        okValue : '确定',
        ok : function(){
            this.title('提交中..');
            return false;
        }
        cancaleValue : "取消";
        cancel : function(){
            alert("取消了啊")
        }
    })
    d.show();
```
#### 控制对话框关闭

- 可以设置  d.close().remove() 来取消对话框 ,例如在定时器中使用延时关闭对话框

```js
    var d = dialog({
        content : '对话框将在两秒内关闭',
    })
    d.show()
    setTimeOut(function(){
        d.close().remove();
    },2000)
```

#### 添加复选框

- 添加复选框  statusbar 状态条

```js
    var d = dialog({
        title: '欢迎',
        content: '欢迎使用 artDialog',
        ok : function(){},
        statusbar : '<input type="checkbox">不再提醒'
    });
    d.show();
```

#### 点击按钮不关闭对话框

- 事件return false可以不关闭 对话框, 任然可以调用 .close().remove()来结束

```js
    var d = dialog({
        title : "标题",
        content : "content",
        ok : function() {
            var that = this;
            this.title("submitting...");
            setTimeout(function(){
                that.close().remove()
            },2000);
            return false
        },
        cancel : function() {
            alert("不能关闭");
            return false;
        }
    })
```

#### 不显示关闭按钮

- 不显示某个按钮  直接将这个按钮赋值为  false  或者直接不用写就好了

```js
    var d = dialog({
        title : 'title',
        content : 'content',
        cancel : false,
        ok : function(){}
    })
```

#### 创建iframe内容

- 没看懂实例

```js
    require(['art-dialog/dist/dialog-plus'], window.dialog = dialog)
```

### 方法

- artDialog的方法都支持链式调用

#### show

```js
//支持传参 若为Dom 则 对话框吸附在  dom上
//若传参为event 则支持根据 pageX与pageY定位(即鼠标所点位置)  要在正常浏览器中,chrome模拟的移动端 不适用

var d = dialog({
    id : "api-show-dialog",
    quickClose : true,
    content : '右键菜单'
});
$(document).on("contextmenu",function(){
    console.log(event.pageX)
    console.log(event.pageY)
    d.show(event);
    return d.destroyed;
})
```

#### showModal

```js
//显示,模态框对话 传参与show相同  但是 在事件中showModal将不会以模态框的形式出现
var d = dialog({
    id : "api-show-dialog",
    quickClose : true,
    content : '右键菜单'
});
$(document).on("contextmenu",function(){
    console.log(event.pageX)
    console.log(event.pageY)
    d.show(event);
    return d.destroyed;
})
```

#### close

```js
//隐藏对话框,并不删除, 并且返回可以链式调用的  对象
```

#### remove

```js
//删除对话框 ， 返回空对象，将不能进行链式调用了
```

#### content

```js
//支持 html string htmlElement
```

#### title

- 设置标题

#### height

- 设置高度

#### reset

- 手动刷新对话框位置

#### button

- 自定义按钮

#### focus

- 聚焦对话框  置顶

#### blur

- 让对话框失去焦点

#### addEventListener(type, callback)

- 支持事件 show close beforeremove remove reset focus blur

#### removeEventListener(type, callback)

- 删除事件

#### dialog.get(id)

- 根据打开是的对话框实例     此方法为静态  不会动态更新

#### dialog.getCurrent()

- 获取当前置顶的对话框

### 配置参数

#### content

- 设置内容 支持 string 和 htmlElement

#### title

- 设置标题内容  支持string

#### statusbar

- 状态栏区域html代码   实现  类似  不在显示复选框等操作    注意必须有按钮才能实现

#### ok ， cancel

- ok cancel 对应的处理函数

#### okValue , cancelValue

- ok 和 cancel 的标识

#### cancelDisplay    boolean

- 是否显示取消按钮   搞不明白  , 既然不想让他显示  那还写他干嘛    
  并没有  okDisplay

#### button

```js
//可以使用数组 来定义一组按钮  

//  名称        类型          描述
/*  value       string      按钮显示文本
    callback    function    回调函数 this指向 dialog对象 ，执行完毕默认关闭与注销对话框，
                            close->remove 若return false 组织关闭与注销
    autofocus   boolean     默认false 是否自动聚焦
    disabled    boolean     默认 false 是否禁用
*/
dialog({
    button : [
        {
            value: '同意',
            callback : function(){
                this.content("你同意了");
                return false;
            },
            autofocus : true
        },
        {
            value :'不同意',
            callback: function(){
                alert("俺不同意");
            }
        },
        {
            id: 'button-disabled',
            value: '无效按钮',
            disabled: true
        },
        {
            value: '关闭我'
        }
    ]
}).show()
```

#### height

- 设置高度

#### skin

- *给按钮设置className*

```js
dialog({
    height:'20rem',
    skin: "min-dialog tips" //设置了像个class****************
}).show();
```

#### fixed  boolean

- 将状态框设置成相对于浏览器窗口定位的

####  align

- 设置对话框其他元素的对其方式

#### autofocus

- 自动聚焦

#### quickClose

- 点击空白关闭对话框

#### zIndex 

- 设置图层高度

#### onshow fun

- 对话框打开触发事件

#### onclose fun

- 对话框关闭触发事件

#### onbeforeremove

- 在对话框remove之前

#### onremove

- remove时

#### onfocus

- 对话框获取焦点时

#### onblur

- 对话框时区焦点事件

#### onreset

- 对话框重置事件

#### id

- 设置对话框的唯一标示  通过 dialog.get来获取 

```js
    dialog({
        id: 'id-demo',
        content: '再次点击试试看'
    }).show();
    dialog.get('id-demo').title('new title')
```

#### open

- 判断对话框是否被打开

#### returnValue

- 对话框返回值

```js
var d = dialog({
    title: 'msg', 
    id: 'id-demo',
    content: '输入<input id="haha">',
    ok: function(){
        var val = $("#haha").val();
        this.close(val);
        this.remove();
    }
}).show();
d.addEventListener("close",function(){
    alert(this.returnValue)
})
d.show()
```