# interview question

## 1.作用域、预编译、函数执行、优先级、new构造函数

```js
//题目
function Foo() {
	getName = function() {alert(1)};	//语句1
	return this;
}
Foo.getName = function() {alert(2)};		//语句2
Foo.prototype.getName = function(){alert(3)};	//语句3
var getName = function() {alert(4)};		//语句4
function getName () {alert(5)};			//语句5

//请写出一下的输出结果

//预编译时的AO对象
//Foo    	function Foo() {getName = function() {alert(1)}; return this}
//getName	function getName () {alert(5)};


//运行到这里的时候后的AO对象
//Foo    	function Foo() {getName = function() {alert(1)}; return this}
//			.getName = function() {alert(2)};
//			.prototype.getName = function(){alert(3)};
//
//getName   function() {alert(4)};


Foo.getName();	
//结果：2	
//原因：函数未执行不能获取函数内的方法，因为存在本身的静态方法(语句2)
//所以以不需要从原型链上找,从而调用函数的静态方法(语句2执行)

getName();	
//结果：4	
//原因：预编译时 函数声明整体提升 ao对象里的 getName是 语句5,
//执行时自上至下，先遇到函数表达式 语句4  会将ao对象中 通过语句5 函数声明的 getName的函数体覆盖 
//再向下执行,遇到 语句5 他是函数声明,已经在预编译过程执行了，提升了 所以被忽略 
//所以最终 ao对象中的getName是语句4  所以返回4

Foo().getName();
//结果：1	
//Foo 函数执行 因为全局存在 getName 且此getName并不是变量声明的
//所以 此getName赋值会更改window对象中的 getName,之后return this 
//因为Foo是普通函数执行 所以this是weindow 也就是最后执行了window上的getName
//所以返回 1
getName();	
//结果： 1
//原因：经过上面的执行  window中的getName已经改变 所以再次执行 任然返回1

new Foo.getName();	
//结果：2
// 此为考优先级 先 Foo.getName 即语句2  再 new 语句4() 
// 因此的到结果 2		--->优先级   . = new(传参) > new 不传参
new Foo().getName();
//结果：3
// 因为 new Foo() 有括号是 有参数列表的  所以与 . 同优先级 
//所以从左至右依次执行， new Foo()   --> Foo {} 
//这里要注意了   new Foo ()的时候 new的操作  只是  在执行function时 隐式创建 //this 并在最后return this  在 new Foo的时候跟 Foo的静态方法 语句2没有关系 所以new的结果为 Foo{}
//再执行  .getName() 因为自身没有  所以根据Foo的prototype指针去原型链上找 从而找到了 语句3 所以返回3


new new Foo().getName()
//结果： 3
//这道题  依旧是优先级   先 new Foo() --> Foo{}之后   .getName --> function(){alert(3)} 之后  new new Foo().getName() -->  alert3 结果为 {}

```
执行过程

	预编译(声明提升)---->执行(忽略声明)

优先级

优先等级|结合情况|运算类型|例子
-|-|-|-
19	|		|	圆括号			|(···)
18	|左结合	|成员访问		|···.···
 	|左结合	|需计算的成员访问 |···[···]
 	|		|new(带参数列表) 	|new ··· (···)
17  |左结合	| 函数调用		|···(···)
 	|右结合	| new 无参数列表	| new ···
16	|		|后置递增			|···++
	|		|后置递减			|···--
15	|右结合	|逻辑非			|!···
	|右结合	|按位非			|~···
	|右结合	|一元加			|+···
	|右结合	|一元减			|-···
	|右结合	|前置递增			|++···
	|右结合	|前置递减			|--···
	|右结合	|typeof				|typeof···
	|右结合	|void				|void···
	|右结合	|delete				|delete···
14	|左结合	|*					|···*···
	|左结合	|/					|···/···
	|左结合	|%					|···%···
13	|左结合	|+					|···+···
	|左结合	|-					|···-···
12	|左结合	|按位左移 <<		|···<<···
	|左结合	|按位右移 >>		|···>>···
	|左结合	|无符号右移			|···>>>···
11 	|左结合	|小于					|···<···
	|左结合	|小于等于			|···<=···
	|左结合	|大于					|···>···
	|左结合	|大于等于			|···>=···
	|左结合	|in					|···in···v
	|左结合	|instanceof			|···instanceof···
10	|左结合	|等号=				|···=···
	|左结合	|不等号!=				|···!=···
	|左结合	|全等 ===				|···===···
	|左结合	|不全等 !==			|···!==···
9	|左结合	|按位与 &				|···&···
8	|左结合	|按位异或 ^				|···^···
7	|左结合	|按位或				| ···\|\| ···
6	|左结合	|逻辑与 &&				|···&&···
5	|左结合	|逻辑或 \|\|			|···\|\|···
4	|右结合	|三目运算符?:;			|···?···:···;
3	|右结合	|赋值					|...=...
	|			|					|...+=···
	|			|					|...-=···
	|			|					|...*=···
	|			|					|.../=···
	|			|					|...%=···
	|			|					|...<<=···
	|			|					|...>>=···
	|			|					|...>>>=···
	|			|					|...&···
	|			|					|...^=···
	|			|					|...\|\|=···
2	|右结合	|yieId				|yieId···
	|右结合	|yieId*				|yieId*···
1	|			|展开运算符 ...		|...···
0	|左结合	|逗号					|···,···
	
## 2. 闭包 、作用域链

```txt
作用域：

因为在ES6之前 是没有块级作用域的,只存在函数作用域。 函数可以访问的变量要在其所在的作用域链上,一个函数就相当于一层，当执行到一个函数的时候，将这个函数推进作用域链中，这个函数就可以访问作用域链上的内容了，当函数执行完毕作用域链会将这个函数弹出。所以在函数外面是无法访问函数内的变量的。

闭包：

闭包是 可以在函数外部访问函数内部的变量的一种手段

闭包的过程：

在一个 外层函数 内返回 内层函数  这个内部函数  可以访问 外层函数内的变量, 从而在 外层函数 的外部 能够使用 外层函数 里面 的变量 这也使得外层函数的 这个作用域  不会被销毁  一直被闭包保存着

内存泄漏、闭包释放：

这样就会导致  内存泄漏。所以  闭包不用了之后  要将 闭包赋值为null 来删除闭包

闭包解决了什么：

缓存了上级作用域、使js打破了 函数作用域这样  就如ajax中的回调函数，就可以访问整个上级作用域

闭包应用场景：

ajax的成功回调、绑定事件的回调函数、setTimeout的延时回调等
```

## 3 get 与 post的区别

```txt
get 方法是xhr.open()	一个字符串
post是 xhr.open()	再 xhr.send(字符串)

get 方法会将请求显示在浏览url中  ? key & value....
post 不会显示出来   

post 请求长度不受限制
get  请求数据长度被限制

```

## 4 优先级

```js
console.log(1 + - + + + - + 1);
	//2
	//这就是 1 + 1两次取负 4次一元加
```

## 5 ， 用于负值  多重复值 返回最后一个

```js
var a = 10,
	b = 20,
	c = (a++, b++, 100)
console.log(c)
	//, 位多重赋值  无论多少个, 结果都是最后一个值
```

## 6 实现函数输入参数返回是否为质数

```js
function isPrimeNumber (num) {
	if(isNaN(num)) {
		return '输入的参数不可以转化成数字';
	} else if (num == 1) {
		return "输入的1不是质数";
	} else {
		num = +num;
		var count = 0
		for (var i = 1 ; i < num; i++) {
			if(num % i === 0) {
				count ++
			}
			if(count > 1) {
				return "输入的" + num + "不是质数";
			}
		}
		return "输入的" + num + "是质数";
	}
}

```

## 7 传入字符串，返回按照字母出现次数 从多到少重拍的字符串， 若不是字符串则返回 实参

```js
//我自己写的方法
 var str = 'def  1  333 333  abc 2  bc 3   c 4 abc';
function sortStringByCount(str){
	if (typeof str === "string") {

		var arr = [],
			newArr = [],
			count = 1,
			newStr = ''

		str = str.replace(/\s+/g,'');
		for (var i = 0; i < str.length; i ++) {
			arr.push(str[i])
		}
		/*
		* 将字符串转成  数组 可以  str.split('')
		**/
		arr.sort();
		//对二维数组 sort 只能不传参使用，会根据二维数组的0位进行排序
		console.log(arr)

		for(var j = 0; j < arr.length; j++) {
			if(arr[j] == arr[j+1]) {
				count ++
			} else if(count > 1){
				newArr.push([count,arr[j]])
				count = 1
			} else {
				count = 1;
				newArr.push([count,arr[j]])
			}
		}
		newArr = newArr.sort().reverse()
		console.log(newArr)
		for(var k = 0; k < newArr.length; k++) {
			for(var l =0; l < newArr[k][0]; l++) {
				newStr += newArr[k][1];
			}
		}
		console.log(newStr)
		return newStr
	} else {
		return str
	}
}
sortStringByCount(str);



```

### 更优秀的方法
```
function sortStringByCount (str) {
	return typeof str === 'string' && str.constructor === String && Object.prototype.toString.call(str) === '[object:string]' && str.split('').sort().match(/(.)\1*/).sort(function(a,b){return b.length - a.length}).join('')
}
```

## 8 实现一个函数，返回斐波那契数列的第n个值

```js
function getFBN (num) {
	if (isNaN(num)) {
		return '请输入数字'
	} else if (num == 1) {
		return 1
	} else if (num == 2) {
		return 1
	} else {
		var a = 1,
			b = 1;
		for (var i = 2; i < num; i ++) {
			oNum = a + b;
			a = b;
			b = oNum;
		}
		console.log(oNum);
		return oNum
	}

}
```

## 9实现函数 判断输入字符串是否为 ‘回文’ 如：'Helleh' 王中王
	
```js
function isPalindrome (str) {
	var arr = [],
		reArr = []

	for (var i = 0; i < str.length; i++) {
		arr.push(str[i]);
	}
	reArr = arr.reverse();
	for (var j = 0; j < arr.length; j++) {
		if (arr[j] !== reArr[j]) {
			console.log(arr[j] +'------'+ reArr[j])
			return str + '---不是回文'
		}
	}
	return str + '---是回数文'
}
```
### 需要改进

```js
	//上面的方法执行了  length 次  
function isPalindrome (str) {
	for(var i = 0; i < str.length / 2; i++ ) {
		// console.log(i)
		if(str[i] != str[str.length-i-1]) {
			//console.log(str[i] + '!==' + str[str.length-i-1])
			//console.log(str.length)
			return false
		}
	}
	return true
}
isPalindrome('王中王王中王')
```
	
## 10 除去字符串中重复的字符

利用对象的属性名不能重复

```js
function removeRepeat (str) {
	var obj = {},
		newStr = ''
	for (var i = 0; i < str.length; i++) {
		obj[str[i]] = 1
	}
	for (var item in obj) {
		newStr += item
	}
	return newStr
}
```
	





