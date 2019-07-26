# VBScript

*visual basic Script!*

```html
1. 大小写不敏感
2. response.write("") 返回结果到页面
3. 在服务端，inputBox， msgBox都不支持
4. 在服务端  <% %> 包裹vbs代码插入到html

```

## 编码约定

### 常数命名约定

const声明的常数,以con开头，然后以驼峰是命名

```vbscript
	const conValue = 12
```
### 变量命名约定

```html
	<pre>
		子类型				前缀
		Boolean				bln
		Byte				byt
		Date(time)			dtm
		Double				dbl
		Error				err
		Integer				int
		Long 	 			log
		Object 				obj
		Single 				sng
		String 				str
	<pre>
```

### 作用域命名

*在vbs中 有过程级作用域和Script级作用域*
过程级作用域 的变量默认填写就好
Script 级作用域的变量  最好以s开头
```vbscript
	sFlag = ture
	'这里的 sFlag的意思就是这事Script级的变量 flag
```
### 描述性变量名和过程名
**驼峰式命名**
*过程命名 应以动词开始*
```vbscript
	initNameArray
```

### 对象命名约定

```html
	<pre>
		对象类型			前缀
		3D面板				pnl
		动画按钮			ani
		复选框				chk
		组合框，下拉列表	cbo
		命令按钮			com
		公共对话框			dlg
		框架				fra
		水平滚动条			hsb
		图像				img
		标签				lbl
		直线				lin
		列表框				lst
		旋钮				spn
		垂直滚动条			vsb
		滑块				sld
	</pre>
```

### 格式化代码
1. 标准嵌套缩进4格
2. 注释 缩进一格

```vbscript
'***************************************
' purpose:sdfasdfasdfasd
' inputs: sdfasdfasdfasf
' returns: asdfasdfasdf
'***************************************


```
	

## 插入到页面

```html
	<script type="text/vbscript">
		....
	</script>
```

## 注释

```vbscript
	' use the point this rol is comment	
```

## 数据类型
	
- VBScript 唯一的数据类型  **Variant**

### Variant 的子类型

```txt
	Empty, Null, Boolean, Byte, Integer, Currency, Long, Single, Double, Date, String, Object, Error
```

获取子类型使用 VarType 函数 返回数据 *[内为vartype 返回值]*

```
Empty:[0] 未初始化的Variant 数字上下文则为0, 字符串上下文则为 "";

Null:[1] 没有任何有效数据;

Integer:[2] -32768 - 32767之间的整数;

Long:[3] -2147483648 - 2147483647 整数

Single:[4] 包含单精度浮点数

Double:[5] 包含双精度浮点数

Currency:[6] -922337203685477.5805 - 922337203685477.5807

Date:[7] 包含表示日期的数字

String:[8] 包含边长字符串，最长可20亿个字符

Object:[9] 包含对象

Error:[10] 包含错误号

Boolean：[11] true, false;

Byte:[17]: 0 - 255 整数;

Array:[8192]: 数组

```


## 变量
	在vbscript中的局部变量叫做（本地变量），全局变量叫做（script变量），局部变量在做用域内有效，当函数执行完释放。

### 变量声明

- 显示变量声明的方式有 Dim reDim Public Private
*需要注意的是 在VBScript中 以上三种方法声明，是不能直接接赋值的，声明多个变量，使用 逗号 隔开，而且在作用域内必须唯一*

```VBScript
	Dim top,left
```

- 隐式声明

*未定义就使用的变量，会成为全局变量* 尽量减少隐式声明，在Script标签的起始 添加 **Option Explicit**

### 声明常量

- 这里的常量声明是可以直接赋值的
```vbscript
	Const myAge = 18
```

### 变量赋值

```VBScript
	top = "1231231"
```

### 变量类型

#### 数组变量
	
- 声明数组变量

*一维数组*
```vbscript
	dim name(2)		'创建一个3个变量的 一维数组
	name(0) = "weibin"
	name(1) = "jiahang"
	name(2) = "yangming"  '数组中的第3位赋值为yangming
```

*二维数组*
```vbscript
	dim sex(5, 1)'创建了一个 6行2列 的二维数组
	sex(0, 0) = weibin
	sex(0, 1) = male	
```

## 运算符

```
	求幂: ^										
	负号: -
	乘号: *
	除号: /
	整除：\
	求余: Mod
	加号: +
	减号: -
	字符串拼接: &
	等于: =
	不等于: <>
	大于：>
	小于: <
	大于等于: >=
	小于等于: <=
	对象引用比较: Is
	逻辑非: Not
	逻辑与: And
	逻辑或: Or
	逻辑异或: Xor
	逻辑等价: Eqv
	逻辑隐含：Imp
```
*需要注意的就是 取余：Mod；整除： \; 字符串拼接： &；不等于： <>;等于： =； 逻辑与，或，非： And， Or， Not；这些是与js 不同的*

## VBScript程序

### 子程序

*是被封装在Sub 和 EndSub 内 执行操作但不返回值，*
*调用的时候直接函数名 空格加参数， 参数用逗号隔开   *
*或者用 call 函数名 (参数，参数)*
```VBScript
	Sub mysub () 
		...
	End Sub
```
### 函数程序

*是被封装在Function 和 EndFunction 内 执行操作并且有返回值*
*调用 要用()  在括号里传参，*
```vbscript
	Function myfun () 
		...
		myfun = "some return value"	'要在接为 用自身函数名设置返回值
	End function
```

## 条件语句

### if Then 

```vbscript
	if i = 10 Then msgbox "i=10 msg out!"
		'....
		'....
	end If  Then执行多行代码时结尾要用 end If 表示结束
``` 

### if Then Else

```vbscript
	if i = 10 Then
		msgbox "i = 10 !"
	elseif i = 9 then
		msgbox "i = 9 !"
	else
		msgbox "not 10 and not 9! "
	end If
```

### Select Case

```vbScript
	select case direction
		case "up"
			msgbox "north"
		case "right"
			msgbox "east"
		case "left"
			msgbox "west"
		case Else
			msgbox "south"
	end select
```
## 循环语句

### 

next     

```vbscript
	For i = 1 to 10 Step 2
		......
	Next
	'Next 的步长默认为1，默认步长为1时可不写Step，
	当要更改步长的时候则需要 设置 Step  且 step 可以为负数
```
### for each

*可以遍历数组*
```vbscript
dim names(2)
name(0) = "weibin"
name(1) = "yangming"
name(2) = "wujiamei"

for each x in names
	document.write(x & '<br/>')
next
```

### do while

```vbscript
i = 0	
do while 1 < 10
	document.write(i & "<br>"")
	i = i + 1
loop
```

### do until

```vbscript
	Sub doUntil()
		dim i, times
		i = 0
		times = 0
		do until i = 10
			i = i + 1
			times = times + 1
		loop
		msgbox"循环了" & times & "次！"
	End Sub
	doUntil		'调用sub
```

## IE 中的 vbs

1. 绑定事件 
*定义  name/id _ 事件类型 的 过程 
就会给与 name/id 相对应的DOM绑定事件， 且事件基本和js相同*
```html
	<input type="button" name="btn" value="sayHello!">
	<script type="text/vbscript">
		sub btn_onclick
			document.write("hello world!")
		end sub
	</script>
```

- 另一种方式 *在行间直接 事件=过程*

```html
<div onclick='msgbox "hello world!"'>clickMe!</div>
```

2. 获取表单的值

*document.forms("id/name")* 获取form表单对象,

```html
		输入 数字
	<form id="formList" onsubmit="getFormData()">
		<input type="text" name="inp" id="inpt">
		<input type="submit" name="sub" value="send">
	</form>
	<script type="text/vbscript">
		sub getFormData
			dim	formList
			set formList = document.forms("formList")

			if isnumeric(formList.inpt.value) then
				document.write("is number")
			else
				document.write("is not number")
			end if
		end sub
	</script>
```

3. 创建对象

```vbs
<OBJECT
   width=250
   height=250
   align=left
>
<PARAM NAME="Angle" VALUE="90">
<PARAM NAME="Alignment" VALUE="4">
<PARAM NAME="BackStyle" VALUE="0">
</OBJECT>
``` 

## 语法参考

### vbs常数

1. 颜色常数
```html
<pre>
	常数    		值
	vbBlack			&h00
	vbWhite			&hFFFFFF
	vbRed			&hFF
	vbGreen			&hFF00
	vbBlue			&hFF0000

	vbYellow		&hFFFF
	vbMagenta		&hFF00FF
	vbCyan			&hFFFF00
</pre>
```

2. 比较常数

*不造啥用。。。*
```html
	<pre>
		常数    			值
		vbBinaryCompare		0
		vbTextCompare		1
	</pre>
```

3. 日期和时间常数
*还是感觉这些常量没啥用到的地方。。。。。*
```html
<pre>
	常数    				值
	vbSunday				1	星期日
	vbMonday				2
	vbTuesday				3
	vbWednesday				4
	vbThursday				5
	vbFriday				6
	vbSaturday				7


	vbUseSystem				0	使用系统时间
	vbUseSystemDayOfWeek	0	由系统设置定义每周的第一天是星期几
	vbFirstJan1				1	使用包含1月1日的星期(默认)
	vbFirstFourDays			2	使用第一个至少包含新的年终四天的星期
	vbFirstFullweek			3	使用某年的第一个整周
</pre>
```

4. 日期格式常数
*很无奈  没看出来  有啥用    以后用到再说吧*
5. MsgBox常数
*知道有这个常数就好了*
6. 字符串常数

*可能换行符 vbLf 回车符 cbCr可能用得到，很崩溃，这事要闹哪样。。。*
```html
<pre>
	常数    		值					描述
	vbCr    		Chr(13)				回车符
	vbCrLf			Chr(13) & Chr(10)	回车符域换行符
	vbFormFeed		Chr(12)				换页符(在mivrosofs windows 中不适用)
	vbLf    		Chr(10)				换行符
	vbNewLine		Chr(13) & Chr(10) 
					或Chr(10)			平台制定新行字符,适用于任何平台
	vbNullChar		Chr(0)				值为0的字符
	vbNullString	值为0的字符串		与零长度的字符串不同，用于调用外部过程
	vbTab			Chr(9)				水平附签
	vbVerticalTab	Chr(11)				垂直附签，在windows中不适用
</pre>	
```

7. 三态常数

*special： 这里面true/false是使用 vbTrue/vbFalse 而且vbTrue 值为-1*
```html
<pre>
	常数    			值    		
	vbUseDefault		-2	使用来自计算机最初设置中的默认值
	vbTrue				-1
	vbFalse				0
</pre>
```

8. VarType 常数

仅当类型库包含以下常数定义，且在您的工程文件中已经显式引用该类型库后，才允许使用这些常数。对于 VBScript，必须在代码中显式声明这些常数。

*不知道啥用  要引用库才能用，你也不告诉我啥库，不用库还要自己声明，这玩应不就有病么。。。。*

### vbs错误

- vbs运行时错误
*等到要用的时候ctrl&F吧，服务器不响应 462*
```html
<pre>
	错误编号				描述
	429						ActiveX不见无法创建对象
	507						发生异常
	449						参数不可选
	17						无法执行请求的操作
	430						类不支持自动化
	506						类未被定义
	11						被0除
	48						加载 DLL错误
	5020					在正则表达式中需要 ）
	5019					在正则表达式中需要 ]
	432						在自动化操作中未找到文件名或类名
	92						For循环未初始化
	5008					非法赋值
	51						内部错误
	505						无效的或不合格的引用
	481						无效图片
	5						无效过程调用或参数
	5021					字符集越界
	94						非法使用Null
	448						未找到命名参数
	447						对象不支持当前的区域设置
	445						对象不支持此操作
	438						对象不支持该属性或方法
	451						对象不是一个集合
	504						对象不能安全创建
	503						对象不能安全初始化
	502						脚本对象不安全
	424						需要对象
	91						未设置对象变量
	7						内存不足
	28						堆栈溢出
	14						字符串空间溢出
	6						溢出
	35						未定义 Sub 或 Function
	9						下标越界
	5017					正则表达式中的语法错误
	462						远程服务器不存在或不能访问
	10						该数组为定长或临时被锁定
	13						类型不匹配
	5018					错误的数量词
	500						变量未定义
	458						变量使用了一个VBScript不支持的自动化类型
	450						错误的参数个数或无效的参数属性值
</pre>
```

- vbs语法错误
*我就艹了   没有网  这md也不能沾图好像  弄一个传图 转化成 url来用啊 以最快的速度打一遍吧* 

```html
<pre>
	错误代码	描述
	1052		在类中不能有多个缺省的属性/方法
	1044		调用Sub是不能使用圆括号
	1053		类初始化或终止不能带参数
	1058		只能在Property Get 中调用 Default
	1057		说明 Default 必须同时说明 public
	1005		需要 （
	1006		需要 ）
	1011		需要 =
	1021		需要 case
	1047		需要 class
	1014		需要 end
	1025		需要语句的结束
	1023		需要表达式
	1015		需要function
	1010		需要标识符
	1012		需要if
	1049		在属性声明中需要 Let Set Get
	1045		需要文字常数
	1019		需要Loop
	1020		需要Next
	1050		需要property
	1022		需要select
	1024		需要语句
	1016		需要Sub
	1017		需要then
	1013		需要to
	1018		需要wend
	1027		需要while 或 until
	1028		需要while 或 until 或 语句结束
	1029		需要with
	1030		标识太长
	1014		无效字符
	1039		无效 exit 语句
	1040		无效for循环控制变量
	1013		无效数字
	1037		无效使用关键字Me
	1039		Loop没有 do
	1048		必须在一个雷的内部定义
	1042		必须为行的第一个语句
	1041		名称重定义
	0151		参数数目必须与属性说明一直
	1001		内存不足
	1054		Property Let 或 set 至少应该有一个参数
	1002		语法错误
	1055		不需要 Next
	1015		未终止字符串常数
</pre>
``` 

### vbs事件

- Initialize事件




- Terminate事件


### vbs关键字

**Emoty, Null, False, True, Nothing**

### vbs方法

- Raise方法
*生成运行时错误*
**object.Raise(number, source, description, helpfile, helpcontext)**

- Clear方法
*清除Err对象的所有属性设置*
**object.clear**


- Execute方法
*对指定的字符串执行正则表达式搜索， 返回字符串中所有符合正则的字符串片段*
**RegExp.Execute(string)**

- reokace方法
*替换在正则表达式中找到的文本*
**RegExp.replace(string1, string2)**

- Test方法
*正则表达式测试*
**RegExp.test(string)**

### vbs对象
1. Class 对象  

*使用class 语句创建的对象，提供了对类的各种事件的访问*


```vbscript
	class classname
		...
	end class 	'生成了一个类

	dim x 
	set x = new classname  'new 出了class对象
```

2. Err

*全局的错误对象，可以直接使用*

```vbscript
On Error Resume Next
Err.Raise 28  '产生堆栈溢出错误。
MsgBox ("Error # " & CStr(Err.Number) & " " & Err.Description)
Err.Clear    '清除错误。
```

3. Match对象

*根据我看文档的描述  这个对象好像就是   正则表达式 execute 出来的结果集合*
**不懂  这你是想告诉我啥**

4. Matches集合

*Matches集合中包含若干独立的 match对象*
**what 我在弄啥呢   感觉看的都是没啥用的东西呢、、、、、、、、、、、**

5. 正则表达式对象

```vbscript
set reg = new RegExp
reg.pattern = patrn
reg.IgnoreCase = true
reg.global = true
```

### vbs运算符
- + 运算
	*主要用于数字相加，也可以拼接字符串，但是与js不同的是 当加好前后一个为数字型字符串，一个为数字时就会进行相加运算，如果非数字型字符串和数字相加估计时报错了*

- And运算符
	*逻辑与*

- 算数运算符

1. 赋值运算符
	*使用 = 与js相同*

2. 比较运算符

```html
<pre>
	运算符			功能
	<				小于
	<=				小于等于
	>				大于
	>=				大于等于
	=				等于
	<>				不等于

特殊表达式之间比较

类型    					如何比较

两个字符串					字符串比较
一个数字，一个字符串		数字<字符串
与Empty比较					empty 看做 0 或 "" 进行比较

</pre>
```

3. 链接运算符 &

*链接字符串，null & null -> null  仅一个参数为null 则null作为空字符串处理，其余表达式相连接，都作为字符串来链接*

4. 除运算符

*null / null -> Null 任何表达式为 Empty 按0 处理*

5. Eqv运算符
*逻辑等价运算 true eqv true 为 true;  false eqv false 为 true； true eqv false 为 false*

6. 幂运算 ^

*num^mi 仅当mi为整数的时候，num可以为负数，存在多幂从左到右依次计算，如果 num 和 mi中任意为 null 则结果为 null*

7. Imp运算符 逻辑蕴含*result = A Imp B*


**eq1**
*A 我去了富士山 B我去了日本    那么就是  A _> B，result就为true   就是如果我去过富士山，那么我一定去过了日本，  A是一个小的集合， B是一个大的集合， A包含在B中   就叫做 A 蕴含于 B*

**eq2**

*A 我娶了一个金发维密模特， B 我去了个金发美女， 同样也是B 比 A的集合大    就叫做 A 蕴含于 B   A _> B*

**简言之就是 B >= A 就是 True 就是 A蕴含(于)B**

- 在vbs中 蕴含 有三个参数 true、 false、 null， 其真值表如下

*感觉 就只有 true 和 false  还是很好理解的，这里面有 null  根据下表 大概可以推出来  ture 包含一切  最大  其次是  null   最小的是 false 比较特别的是   null->false = null; ture -> null = null; null -> null = null*
```html
	A        B          result
	true 	true 		true
	false 	true 		true
	null 	true 		true

	true 	false 		false
	false 	false 		true
	null 	false 		null

	true 	null 		null
	false 	null 		true
	null 	null 		null
```

**不知道这个逻辑蕴含  以后会不会用到。。。**

8. \ 相除，结果取整数位

9. Is 运算符

*判断是否是统一对象的属性 返回 boolean*

10. Mod运算符	

*取余， 对于浮点数先进性四舍五入在进行取余*

11. * 相乘运算

12. 逻辑非运算符 Not

13. 逻辑与运算符 And

14. 逻辑或运算符 Or

15. Xor 异或 运算符

*相同为false 不同为true*

### vbs属性

*看了看  文档介绍的几个属性  感觉没啥用，不知道他在说啥呢*

### vbs语句

1. call语句

*call name ()*调用sub 或 function  参数要用()括起来, 这样就放弃了 过程的返回值

2. class语句

*声明一个类， 这个类可以包含多个过程，这些过程可以被声明为public 和 private*

```vbs
	Class className
		statements
	End Class
```
**没有设置private 的就是默认的就算是public，被声明为public 的变量就会成为这个类的属性，过程叫做方法。**

3. const语句

*[public | private] const conName = expression*  其中定义public 或 private 不可以在过程中使用

expression 可以是不包含 IS 的其他任何表达式的任意组合

4. Dim语句

*Dim varname，varArr(num)* 在过程中声明变量或数组，在过程中声明的只能用于过程中。   
由此可见 VBS是 过程作用域   与js 的 函数作用与相似

5. Do...Loop 语句

```vbs
	Do [{while | until} condition]
	[statements]
	[Exit Do]
	[statements]
	Loop
	
	'或者
	Do 
	[statements]
	[Exit Do]
	[statements]
	Loop [{while | until} condition]
```

*这可以选择两种Do的方式 while 和 until，condition是判断条件。
其中特别的是 Exit Do 这个地意思是  出口，  配合 if Then 当达到想要的值的时候  在if true 中改变一个值，通过 exit do 传出去 从而停止循环*

6. erase语句

*Erase array*用于重新初始化数组，并释放空间，不同类型的数组，初始化会得到不同的，
数字数组 —— 将每个元素设置成0;	字符串数组 —— 将每个元素设置成 "";  对象数组 —— 将每个元素设置成 nothing

7. execute
*Execute statements*执行一个或多个字符串形式的表达式若需要换行  用 : 表示换行

```vbs
	Execute "sub fun1 : document.write(X) : end sub"
```

**如果 在过程A中 excute 了一个过程B 那么 这个过程B内的变量值  不会继承于A过程的作用域中的值，而是继承于全局，且此过程B仅能在过程A中调用
如果在全局Excutel了一个 过程，那么这个过程的作用域就是全局的，而且这个过程可以在任意位置调用**

- 由此可见 一般 创建的过程的的作用域是全局的

8. executeGlobal

*与 execute功能类似，不同点在于它声明的普通的语句也会在global中*

9. Exit语句

*用于跳出 Do...Loop, for...Next, Function， 或 Sub 代码段*

```vbscript
	Exit Do
	Exit For
	Exit Function
```

10. for each...next
	对数组或集合遍历

```vbscript
	for each element in group
	[statements]
	[Exit For]
	[statements]
	Next [element]
```

11. for ... next

```vbscript
	for counter = start To end [step step]
	[statements]
	[Exit For]
	[statements]
	next
```

12. function

```
	[Public [Default]| Private] Function name [(arglist)]
	[statements]
	[name = expression]
	[Exit Function] 
	[statements]
	[name = expression]
	End Function
```
*需要注意的是 function  要设置返回值 funName = expression*

13. if...then...else语句

```
	if a > 10 then
	...
	else
	...
	end if
```

14. on error

*启用或禁用错误处理程序*

```vbs
	On Error Resume Next    ' 开启错误处理
	On Error GoTo 0			'关闭错误处理
```

```vbs
	On Error Resume Next
	Err.Raise 6  '产生溢出错误。
	MsgBox ("Error # " & CStr(Err.Number) & " " & Err.Description)
	Err.Clear    '清除错误。
```

15. Option Explicit 语句

*写在语句之前  强制要求 显示声明 脚本内所有的变量，从而避免忘记 声明而产生变量*

```vbs
	Option Explicit    ' 强制显示声明变量。
	Dim MyVar          '声明变量。
	MyInt = 10         '未声明变量产生错误。
	MyVar = 10         '声明变量不产生错误。
```

16. private语句

*定义私有变量并分配存储空间, 如果Private， public， Dim 语句已经指定了数组的大小，再想重新声明数组维数就会发生错误*

17. Property Get 语句

**在class块中**，**声明**
构成 用来取得(返回)的值 的属性**过程**的
主体的 **名称**、**参数**、和**代码**

```
	[Public [Default]| Private] Property Get name [(arglist)]
	    [statements]
	    [[Set] name = expression]
	    [Exit Property] 
	    [statements]
	    [[Set] name = expression]
	End Property
```
*说的是人话么。。。。  经过分析  意思应该是  在class中 声明 一个过程 的名称等*、

18. Property Let

**在class块中**，**声明**名称、参数和代码等，他们构成了赋值(设置)的property**过程的主体**
```
	[Public | Private] Property Let name ([arglist,] value)
	    [statement]
	    [Exit Property] 
	    [statement]
	End Property 
```

19. Property Set
**在class块中**，声明名称、参数、和代码， 这些构成了将以弄设置到对象的property**过程的主体**

```
	 [Public | Private] Property Set name(
	  [arglist,] reference
	)
	    [statement]
	    [Exit Property] 
	    [statement]
	End Property 
```

20. Public语句

*定义公有变量并分配存储空间，*在class块中定**义私有变量**you lost me~
```vbs
	Public varArr(num), varVal
```
也可用带空圆括号的 Public 语句来声明动态数组。
声明动态数组后，可在过程内使用 ReDim 语句来定义该数组的维数和元素。
如果试图重新声明数组变量的维数，且此数组变量的大小已在 Private、Public 或 Dim 语句中显式地指定，则会发生错误。

21. Randomize语句
*初始化随机数生成器*
```vbs
	Dim MyValue, Response
	Randomize '初始化随机数生成器。
	Do Until Response = vbNo
	   MyValue = Int((6 * Rnd) + 1)' 产生 1 到 6 之间的随机数。
	   MsgBox MyValue
	   Response = MsgBox ("Roll again? ", vbYesNo)
	Loop
```

22. ReDim 
*在过程中声明动态数组变量并分配或重新分配存储空间*

23. Rem
*注释*

```
Rem ......
'.....
```

与 ' 的注释是相同效果，不同在于如果使用rem进行注释，需要用分号与前面分隔。而'不需要

24. set

*将对象引用赋值给一个 variable 或 property 或者将对象引用与事件关联*

25. Sub

*声明过程，参数，等
Sub 的过程是 公共的
不可已在 过程中定义sub过程*

26. while...wend

*当condition 为 truee 时 执行statements*
```
	while condition
		statements
	wend
```

27. with
*对同一个对象,执行一多条语句*

with objName
	statements
end with

### vbs函数

1. Abs

```vbs
	Abs(number)
```
*特别的是  null的绝对值是 null； 为初始化的变量----0*

2. Array函数

*感觉像是数组的字面量   不过依然需要先声明 另起一行来赋值*
```vbs
	dim arr
	arr = Array(1,2,3,...,)
```

3. Asc函数

*返回字符串首字母的ANSI字符代码 ---即拓展的ASII
码*

4. Atn函数

*返回 反正切值 arctan
若 tanA = 1.9/5 则 A= arctan 1.9/5*

5. CBool 函数

*返回Boolean子类型的variant*

6. cByte 函数

*返回 byte 子类型的variant*

7. CCur 函数

*返回 currency子类型的variant*

8. CDate 函数

*返回Date子类型的variant*

9. cDdl 函数

* 返回 double子类型 的variant*

10. Chr 函数

*返回 与输入ANSI对应的字符*

11. CInt 函数

*返回 Integer 子类型的variant*

12. CLng 函数

*返回 Long 子类型的variant*

13. Cos 函数

*返回某个角的余弦值*
```
	dim myAngle, mySecant
	myAngle = 1.3				'用弧度定义一个角
	mySecant = 1 / Cos(myAngle) '计算正切
```

14. createObject函数

*创建并返回对 automation 对象的引用*
**automation对象：**通过Automation借口显露于其他应用程序或编程工具的对象
```
createObject(servername.typename[, location])
```
**servername:**必选，提供对象的应用程序名称
**typename：**必选，要创建的对象类型或类
**location：**可选项，对象所在的网络服务器将被创建
。。。。。。看不懂

15. CSng函数
*返回 single子类型的variant*

16. Cstr函数

*返回 string 子类型的 variant*
```html

值类型				转化为

Boolean 			ture/false 字符串
Date 				断日期格式 字符串
Null 				运行时错误
Empty 				""
Error 				报错信息	字符串
```

17. Date 函数

*返回系统日期*
```
	dim now
	now = Date
```

18. DateAdd 函数
*返回 增加了 num个 时间间隔的 新时间，三个参数都是必传的*

```html
nowDate = dateAdd("m", 1, "31-may-2018")
```
第一个参数是 单位步长 string类型
```html
	yyyy年,q季度，m月，y一年的天数，d日，w一周的天数，ww周，h小时，n分钟，s秒
```
第二个参数是 步数 NUmber 类型 可以负数
第三个参数是 起始日期 字符串形式  年-月-日 / 日-月-年 根据长度  自行判断

19. DateDiff 函数

*返回两个日期间的时间间隔*

```html
	DateDiff(interval, date1, date2[, firsdayofweek[,firstweekofyear]])
```
*interval* 必选 想要的 date1 和 date2 之间间隔的单位
*date1，date2* 必选 要计算的两个日期
*firstdayofweek* 非必选 指定一周中的第一天是星期几， 没有指定默认 为周日
*firstweekofyear* 非必选 指定 一年中的第一周是第几周， 默认为一月一的那周为第一周

20. DatePart函数

*返回给定日期的指定部分*

```html
	datePart(interval, date[,firstdayofweek[,firstweekofyear]])
```
*前两个参数为必选，与DatePart传参类型相同* 

21. DateSerial函数
*传三个参数 返回Date 类型*

```vbs
	DateSerial(2018,8,8)
```

22. DateValue函数

*返回 date子类型的 variant*

```vbs
	DateValue(dateString) '将 日期字符串转化成 date 类型
```

23. Day 函数

*返回 日期表达式中的天数*

24. 派生数学函数
。。。。。。。。疯了再去看吧

25. Eval函数

*计算一个表达式的值并返回结果*
```vbs
[result = ] Eval(expression)
```

26. Exp 函数

*返回 e 的幂次方*
```vbs
	num = Exp(6)		'e的6次幂
```

27. Filter函数

*返回符合条件的字符串集合数组*

```vbs
	Filter(InputStrings, Value[,Include[,Compare]])
```

28. FormatCurrency

*格式化成货币格式*
```
	FormatCurrency(num)
```

29. FormatDateTime

* 返回日期格式化的 表达式*

```vbs
FormatDateTime(Date[, NameFormat])
```

30. FormatNumber

*返回 数值格式化的表达式*

31. FormatPercent

*返回 百分数格式化的表达式*

32. GetLocale

*返回 当前所在地区 ID值*

33. GetObject函数

*感觉像是  node.js里面的 require   返回文件中 Automation对象的引用*

```vbs
GetObject([pathname][,class])
```

pathname: 为要要引用的文件的路径，如果必须要有class

34. GetRef

*给对象绑定事件*

```vbs
	set object.eventname = GetRef(procname)
```

**object** 必选项， 要绑定事件的对象
**eventname** 必选项，绑定的事件名称
**procname** 必选项，绑定的过程的名称

35. Hex 函数

*转化成十六进制字符串输出*

Hex (number)

36. Hour 函数

*返回 小时 0-23*

```vbs
	Hour(time)
```

37. InputBox 函数

*在对话框中显示*

```vbs
InputBox(prompt[,title][,default][,xpos][,ypos][,helpfile,context])
```

38. InStr 函数

*返回str2字符串 在str1中第一次出现的位置*

```vbs
	InStr([start, ]str1, str2[, compare])
```

39. InStrRev
*返回str2 在str1中最后出现的位置*

```vbs
InStrRev(string1, string2[, start[, compare]])
```

40. Int、 Fix函数
*返回数字的整数部分*
**Int(num)  /  Fix(num)**
区别，在输入为负数的时候， 
Int 返回 小于等于的值， 而Fix返回大于等于的值

41. IsArray函数

*判断是不是Array，返回boolean*

42. IsDate

*判断是否能转化为日期， 返回boolean*

43. IsEmpty

*判断变量是否初始化  返回Boolean值*
- 即 初始化时赋值位  Empty

44. IsNull

*判断 值是否为null   返回boolean* 
- Enpty 与 null 是不同的

45. IsNumeric

*判断是否为数字  返回boolean*

46. IsObject

*判断 变量是否引用了有效的 Automation对象 返回boolean*

47. Join函数

*将字符串数组 拼接成一个字符串*

48. LBound 函数

*返回数组最小的可用下标*

49. LCase函数

*返回字符串的小写形式*

50. Left 函数

*返回 从字符串左边截取len长度的字符串，如果len大于字符串长度则返回整个字符串   不改变原字符串*

51. len 函数

*获取字符串长度*

52. LoadPicture

*获取图片对象*

53. Log函数

*返回自然数对*

54. Ltrim、RTrim、 Trim函数

*返回不 左不带空格、右不带空格、 左右都不带空格*


55. Mid函数

*在str中 返回从 start 向后获取length长的字符串*

```abs
	Mid(string, start[,length])
```

如果省略length 则返回从start 到结尾

56. Minute函数

*获取Date的分钟*

57. Month函数

*获取Date的小时*

58. MonthName

*返回 月份字符串*

59. MsgBox

*在对话框中显示消息*

```vbs
MsgBox(prompt[, buttons][, title][, helpfile, context])
```

60. Now

*根据 计算机系统设定的日期返回当前的日期和时间*

```vbs
	dim nov 
	nov = now
	document.write(nov)
```

**这里比较特殊  ，可以获得最小到秒**

61. Oct

*返回 八进制字符串*

62. Replace

*返回 被替换后的字符串*

```vbs
	Replaace(string, find, replacewith[, compare[, count[, start]]])
```

63. RGB

*返回代表RGB颜色的整数*

64. Right

*从字符串string 右端返回length长 字符串*
```vbs
	right(string, length)
```

65. Rnd函数

*返回一个随机数*

66. Round

*返回四舍五入的数值*

67. ScriptEngine 函数

*返回代表当前使用脚本语言的字符串*

68. Microsoft(R) Visual Basic(R) Scripting Edition 

*返回使用的编写脚本引擎的编译版本号。*

69. ScriptEngineMajorVersion 函数
*返回使用的编写脚本引擎的主版本号。*

70. ScriptEngineMinorVersion 函数

*返回使用的编写引擎引擎的次版本号。*

71. Second

*返回 秒*

72. setLocale

*设置时区*

73. sgn函数

*判断 number的 正，负，0   返回 1， -1， 0*

74. sin

*返回角的正弦值*

75. Space 函数

*返回length 长的 空格组成的字符串*

```vbs
	space(length)
```

76. split

*与 join 相对 这是将数组字符串 拆分成 数组*

77. sqr

*返回数的平方根*

78. StrComp

*返回一个表明字符串比较结果的值  返回 -1， 0，1。 若一方存在null 则返回null*

79. String函数

*返回具有指定长度的重复字符组成的字符串*

```vbs
String(length, character)
```

80. StrReverse
*返回倒序字符串*

81. Tan

*返回正切值*

82. Time

*返回系统时间   时分秒*

83. Timer

*返回0:00 到现在 多少秒*

84. TimeSerial

*返回 Date 的 时、分、秒的时间*


## FileSystemObject用户指南

### FileSystemObject对象模型












