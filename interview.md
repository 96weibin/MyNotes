# interview

## 1. 检测一个变量str是不是字符串类型

```js
	Object.prototype.toString.call(str)	=== "[object String]";

	typeof(str) === "string";

	str.constructor === String;
```

## 2. 用js去除字符串空格

```js
	str.trim()

	str.replace(/\s+/,'');
```

## 3. 获取url中查询字符串的参数
< http://127.0.0.1/staff/?username=hello&password=world>

```js
	var str = location.href;
		urlArr = str.split("?")[1].split("=").toString().split("&").toString().split(","),
		obj = {};
	for (var i = 0; i < urlArr.length; i += 2) {
		obj[urlArr[i]] = urlArr[i + 1];
	}
	console.log(obj)
```

## 4. 列举常见的字符串函数

```js
	str.concat('str1','str2'....) 	拼接多个字符串
	str.charAt(/[qwe]r/);			返回匹配项第一次出现的位置
	str.charCodeAt(1)				返回str[1]的ASCII编码

	str.subString()					传一个参数4是 截取str[4]之前的  小于0 的作为 0
									传两个参数 小的作为起始     截取留头去尾

	str.subStr()					传一个参数4 截取 str[4]之前的   
									传两个参数 第一个参数是起始位置 第二个参数是截取长度  并返回截取下来的,
	
	str.slice()						传一个参数4 截取 str[4]之前的   并返回 如果传参小于0 则从后向前查
									传两个参数 前始后终 留头去尾

	str.match(reg) 					返回匹配reg的 一个数组

	str.replace("reg",function(){}) 替换str中符合reg的，替换结果为Function的返回值   分组替换

	str.indexOf("o") 				返回o在str第一次出现的位置

	str.lastIndexOf("o")            返回o在str中最后一次出现得位置

	str.trim()						出去str左右两边的空格

	str.trimLeft() 					删除左边的空格

	str.trimRight()					删除右边的空格

	str.toUpperCase()				将字符串转换成大写

	str.toLowerCase()				将字符串转换成小写

	str.split(",")					以 , 分割 字符串每一段作为数组的一项

```

## 5. 怎么添加、移除、移动、赋值、创建和查找节点

```js
//创建节点
document.createElement()
document.createTextNode()
document.createDocumentFragment()

//添加、移除、替换、插入
appendChild()
removeChild()
replaceChild()
insertBefor()

//查找
document.getElementById()
document.getElementsByClassName()
document.getElementsByTagName()
document.querySelector()
document.querySelectorAll()

```

## 6. 写出3个使用this的经典应用

```html
<body>
    <button onclick="new Init()">构造函数</button>
    <script>

    function Init(){
		this.mgs = 'hello world';
		this.initHead();
	}

	Init.prototype.name = 'zhao',
	Init.prototype.str = '世界真美好',
	Init.prototype.age = '12',

	Init.prototype.sayHello = function(){
        alert('hello world!')
    }
	Init.prototype.initHead = function(){
		var that = this;
		setTimeout(function(){
			alert(that.str)
		},2000)
	}
	new Init().sayHello()	//构造函数
    </script>
</body>
```

*this*的指向

```js
普通的函数、自执行函数			 window
定时器、计时器		   			window
事件						    dom对象	
构造函数					  对象实例
闭包						   上次执行的环境
call、apply					强制转换this指向
```
a.call(b)	 a使用 b 的this 执行

## 7. 比较 typeof 和 instanceof 的区别

```html
	typefo 
		是 typeof(value)	返回以个字符串  类型有 number string boolean undefind objec function
		对于 具体是那种Object 不能确定   且null的类型是 object
	instanceof
		是根据原型链来判断 a实例 instanceof b构造函数  a实例 的原型链上是否有 b构造函数, 返回true/false
		instanceof可以判断 具体是那种引用类型,但是对于 原始类型的数据就不可以了,因为原始类型的数据没有原型链
		a实例 如果是引用类型 它的原型最顶端  一定是  Object 所以 判断Object总会返回true
```

## 8. 如何理解闭包

## 9. 什么是跨域 跨域的请求资源的方式有哪些

	跨域就是数据  不同源   协议、域名、ip、端口 任何一项不想同就不是同源的数据,这时出现不能访问的现象
	跨域就是 在不同源的 地方取数据等操作

	跨域请求  有ajax jsonp等
	jq的ajax可以解决跨域的问题
	jsonp 是利用 script标签、img标签等有 src 的标签可以不受同源策略限制 进行数据的读取
	且script标签默认支持 json且 json可以表示复杂数据 所以可以用jsonp解决跨域问题

	

*简单的*jsonp跨域
*index.html*
```js
	var flightHandler = function(data) {
		console.log(arguments);
		alert("班级票价:" + data.price + '班机号:' + data.code);
	}
	var script = document.createElement("script");
	script.setAttribute("src","http://127.0.0.1/interview/jsonp.js");
	document.querySelector("head").appendChild(script)
```
jsonp.js

```js
flightHandler({
    'code':'CA1988',
    'price' : 1780,
    
})
```

上面这种   感觉就是请求来一个 js文件  而这个js 文件有一定的数据

### 封装

index.js
	
```js
function jsonp(url, callbackName, callback) {
	window[callbackName] = callback;
	var script = document.createElement('script');
	document.body.appendChild(script);
	script.src = url;
	document.body.removeChild(script);
}


jsonp("http://127.0.0.1/interview/jsonp.js",'fun',function(data){
	console.log(data)
})

```

jsonp.js

```js
var data = '123';
fun(data);
```

*这种的感觉就像通过  script标签 将callback拿到了jsonp.js里面执行*

 ## 类型转化

 ```js
	var a = [1,2];
	var b = [3,4];
	console.log(a+b)
 	=>1,23,4
	// 因为+ 先看左右是否可以相加 、转化类可以向家么 之后 String（） 后拼接了
 ```