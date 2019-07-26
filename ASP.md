#APS

##ASP的起源

	ASP是服务器端脚本语言，运行在服务器上，通过中间插件，CGI（common Gateway Interface）【共同 网络连接器 接口】的处理与web服务器进行通信，在linux系统上的PHP类似

	ASP是 运行在web服务器的内存空间中，可以直接访问web服务器的内存，如dll文件，

- ASP如何与IIS连接

	ASP本身有一个asp.dll文件， 在winnt\system32\inetsrv下通过这个dll识别得到.asp的文件，然后 ---> 脚本引擎 ----> 客户端

- 处理ASP文件

	当ASP从IIS接受到包含服务器端脚本时，会进行逐行解释，

	非服务端或不需ASP处理的：   将被返回到 IIS，然后 发送到客户端，
	服务端脚本：会送入相应的脚本引擎，处理后结果返回IIS 然后插入页面相应位置

- 区分服务器端脚本
	
	1. <%%>   嵌入到html中， 其间为服务器端脚本
	2. <script language="vbscript" RUNAT="server">	当内嵌script的 runat值为 server时 服务器端，为client时为用户端
	3. 同时也支持 script sec进行外链

标记语言 确定编码 <%@ language="vbscript" codepage="65001"%>

---

## request 与 Response对象

### requset对象

- 属性

	TotalBytes	- 	返回客户端发送来字符流的字节数

- 方法

	BinaryRead	-	根据描述，99.99% 不会用到



- 集合

	queryString	-	获取get 提交的数据

	Form		- 	获取post提交的数据

	serverVariable-	获取http报文头，以及web服务器环境变量信息

	cookies		-	获取用户系统发送的所有cookies集合

	clientCertificate- 获取客户端身份权限数据


### response对象

- 属性
	
	buffer	-	可读写，设置  页面是否 先缓冲

	contentType-可读写，设置Response对象的http内容类型

	Expires	-	可读写，设置浏览器缓存页面的时间，

	expiresAbsolute-	可读写，设置页面过期时间

	Status	-	返回服务器对客户端相应的各种状态值

	isClientConnected-	判断客户端与服务器断开连接

- 方法

	write(str)	-	向客户端发送数据

	redirect(url)-	是浏览器重定向到 url

	clear 		-	将服务器缓存中的信息清除

	flush		-	将服务器缓存的数据发送到浏览器

	end			-	结束处理页面脚本，并返回当前已创建内容

	binaryWrite(safeArray)-	在当前的http输出流中写入variant类型的SafeArray，而不经过任何字符转换，通过用于二进制数据 或者图像文件的二进制字节

	addHeader	-	增加带有一个要发送到客户应用程序的特殊HTTP头，他不代替现有的标题，一旦标题被添加就不能删除

	appendToLog()-	给服务器日志添加条目



## Application 与 Session对象

### application

- 集合

	1. contents: 没有使用<OBJECT>元素定义的存储于Application对象中的所有变量的集合，可以省略Contents而直接访问 即  Application("use")

	2. staticObject: 使用<Object> 元素定义的存储于Application对象中所有的变量的一个集合的集合

- 方法
	
	1. Contents.Remove("var"): 从Application.content结合中删除一个名为var的变量

	2. contents.removeAll(): 从appclition对象中删除所有变量

	3. Lock： 锁定Appliction对象那个，使得只有当前的ASP页面内容能够进行访问

	4. Unlock： 解除对象的锁定

- 事件

	1. onStart： 当ASP启动时出发，在所有网页，session的创建之前

	2. onEnd： 在asp应用程序结束时出发，
*处理 onStart和onEnd 事件的函数要放在Global.asa中，当创建一个应用程序时会自动生成global.asa，global.asa 对用户时不可见的，在global.asa中要使用 <\script>标记来规定脚本类型，且global.asa中不能有任何输出语句*

### session对象

其实就是指访问者从到达某个特定位置 到离开位置的那段时间，每个访问都会单独的获取一个session
与Application对象相比  session对象更接近于 普通应用程序中的 **全局变量**， 全局变量在程序执行的过程中始终有效，其他的用户同时启动该程序的副本 使 该程序 的各个实例使用各自的全局变量，在两个继承之间相互不能访问，绝大多数情况下session对象被做为全局变量，以实现在该应用的所有页面中的共享信息

- 设置
	
	session("msg") = 'msg'

- 取出

	session("msg")

- 属性
	
	1. sessionID：只读返回 sessionid

	2. timeout： 可读写，定义时限

	3. codePage： 定义浏览器中显示的内容的  代码页
		这里代码页的意思 大概有点像ASCII编码

	4. LCID： 可读写，定义发送到浏览器页面地区标识

- 方法
	
	1. abandon： 清除存储在Session中的所有对象和变量

	2. contents.remove("var"): 在session合集中删除 var变量

	3. contents.removeAll() 从合集中删除所有变量

- 事件 
	
	1. onStart: 

	2. onEnd


## server对象

- 属性
	
	1. scriptTimeout   设置超时时间，默认单位为 s

- 方法
	
	1. HTMLEncode： 将字符串 以 html的编码输出

	2. URLEncode： 将输入的字符串 无效 字符转化成 等价的URL条目

	3. MapPath： 返回虚拟路径实际在服务器上的实际路径

	4. createObject： 创建以注册到服务器上的Activex组件

	5. Excute方法： 停止当前页面的执行，把控制转到指定页面  session等也传递到此页面， 当前页面执行完后 控制传回原页面

	6. transfer： 与excute方法类似，不同在于 新页面执行完毕，会结束执行过程

	7. GetLastError: 返回ASPError对象的引用，包含最后一次报错数据
---
- #include 引用外部文件
```asp
'相对于当前真实目录的引用
<!--#include file="./wwwroot/index.asp" -->

'相对于web虚拟目录的引用
<!--#include virtual="./wwwroot/index.asp"-->

与 Excute 相反
```

---

## ADO组件(AvtiveX Data Object)


### SQL

1. 数据库查询 Select

```
select [all | distinct] <目标表达式>[,<目标表达式2>]

from <表名1>[,<表名2>]
[where <条件表达式>]
[group by <列名1> [having<条件表达式>]]
[order by <列名2> [ASC | Desc]]
```

- 条件表达式
	
	除了常规的 比较表达式之外 还有

	1. between...and 和 not between...and

```asp
where age between 18 and 50
```
	
	2. like 和 not like

```asp
	where name like "__斌"
	'模糊搜索    * 斌 ，  _  代表  一个字符 汉字需要两个字符

	where name like "%斌"
	'模糊搜索   ...斌，  % 代表任意字符长度
```

	3. And 和 or  来链接多个条件

	4. order by 对获取的数据进行排序

```asp
	order by userID, sage Desc
	'默认 是升序  在后面加 Desc就可以 改为降序排列
```

	5. distinct删除重复行

```asp
	select distinct age from studentList
	where sex = "male"

	'就是在 要 select 的条件表达式前 加一个关键字  distinct
	'这样返回的数据就会  删除重复的数据
```
	
	6. top n [precent]限制返回行数

```asp
	select top 2 name from studentList 
	where like "赵%"

	'这里 在目标表达式前面添加 top 2 则最多返回 2条符合的数据，也可以 top 20 percent 可以返回所有符合条件的数据中的20%'
```

	7. 多表查询

	where [<表名1>.]<列名1> = [<表名2>.]<列名2>


2. insert 插入 

```asp
	insert into studentList
	value ("0123", "zhaoxue", "female", 20)
```

3. Update更新数据

```asp
	update studentList
	set age = 22
	where name = "weibin"
```

4. Delete 删除操作

```asp
delete
from studentList
where no = "13246"
```


5. 函数合集

*const*记录条数

```asp
const([all|distinct]<要查询的表名，列名>)
```

```asp
	Select Count(*) From Student
```

*sum*数值总和

```asp
sum([all|distinct]<要计算的列>)
```

*avg*数值 平均值

```asp
avg([all|distinct]<要计算的列>)
```

*max*返回一列中最大值

```asp
max([all|distinct]<列名>)
```

*min*一列中的最小值

```asp
min([all|distinct]<列名>)
```

6. 存储过程

创建存储过程

```asp
create procedure[拥有者,]存储过程名[;程序编号][(参数#1,....,参数#n)]
[with
{recompile | necryption | recompile, encryption}
]
[for replication]
```

### 连接数据库

#### SQLServer 数据库

1. 通过DSN链接数据库 (存在较明显缺陷)

```asp
	<%
		set con = server.createObject("adodb.connection")
		con.open "DSN = data; UID = LoginID; PWD=password"
	%>
```

2. 使用OLEDB链接数据库

```asp
	<%
		set Conn = server.createObject("adodb.connection")
		Conn.connectionString = "driver={sql server};server=10.30.1.99;uid=dev;pwd=dev;dataBase=Development"
		Conn.open
		'这里数据库就链接上了 就可以进行操作了

		Conn.close
		set Conn = nothing
	%>
```


### connection 对象

1. connection 对象的创建

```asp
set conn = server.createObject("adodb.connection")
```

2. connection 对象的属性

```html
Attribute		用于指定一个对下那个的一个或多个特性
```


	1. attribute：
		定义connection对象的事件处理方法，
		1） 设置为131072 或 adXactCommitRetaining 的 ADODB常数----数据写入数据库，另个一个事务将自动启动 即： 保留提交
		2） 设置为26214
		
		
		
		4 或 adXactAbortRataining的adodb常量---- 事务被取消则另一个事务会自动启动   即： 保留取消

	2. commandTimeOut
		设置超时时间，如果在限定时间内没有完成指令，就会报错，默认值为30S， 可以设置成任意值，当设置为0就取消超时判断

	3. connectionString
		以key:value包含用于建立链接数据源的信息。

		connectionString的5个属性
		1) DSN : 数据源名*
		2）PWD : 数据源名*
		3）UID : 访问数据源的用户账号
		4）Provider : 指定用来连接数据提供者的名称
		5）FileName : 指定数据源的某这个特定文件

*在connection对象打开之前connectionString是可以读写的，而当connection对象打开之后 connectionString 变为只读*

	4. connectionTimeout
		创建连接所需要的时间， 缺省为15s    0 为 不限时间
	5. defaultDatabase
		用来定义connection链接缺省时  默认链接的数据库
	6. mode属性
		用来表示连接的权限，这个属性只能在connection对象没有打开的时候设置，其可以设置的值如下

```
	adModeUnknow			默认值，表示权限尚未设置或无法确定
	adModeRead				只读模式
	adModeWrite				只写模式
	adModeReadWrite			读写模式
	adModeShareDenyRead		防止其他用户使用读权限打开连接
	adModShareDenyWrite		防止其他用户使用写权限打开连接
	adModeShareExclusive	防止其他用户使用读/写权限打开连接
	adModeShareNone			表示其他用户不得用任何方式打开连接
```
	
	7. provider属性
		该属性返回或设置  数据提供者的名称，
	8. IsolationLevel属性
		表示connection对象的隔离级别  可读写    下次调用  biginTrans方法才会生效
	9. Provider 指定数据提供者的名字
	10.state 对象状态
	11.version 指定当前使用ADO的版本 

3. Connection对象的方法

```html
open			打开与数据库的链接
close			关闭与数据库的链接
	
			'close断开连接后 connection对象也被释放，要再用需要重新创建
			'一般close后 还要设置 Conn = nothing

BeginTrans		生成一个新的事务
commitTrans		用于保存当前事务的所有修改
RollbackTrans	用于取消当前事务所做的修改并结束该事务

execute			执行指定的  字符串格式语句
	set res = connection.execute(commendText,recordsAffected, options)
	三个参数 
		commendText——* 是SQL命令字符串
		recordsAffected—— 长整型变量保存SQL操作记录
		option—— 指定commendText的性质
			1) adCmdTxt			SQL串
			2) adCmdTable		表名
			3) adCmdStoreproc	存储过程
			4) adCmdUnknown		默认值--不指定

openShchema		用于打开服务器端数据库的计划信息
```

4. connection对象的errors集合

	属性： 
	1.count 		返回错误对象个数
	2.item 			返回具体的错误对象
	方法：
	1. 清除Errors合集的所有错误成员
	对象：
	1. description	返回错误信息
	2. number		返回错误代码
	3. source 		返回错误对象
	4. SQLState		返回错误代码
	5. nativeError		对应特定数据提供者代码？？？？？
	6. HelpFile、 helpcontext   帮助文档

### Command对象

#### 创建Command对象

```asp
	database="数据库名"
	str="provider= 提供者; data source = 虚拟路径对应的物理路径"

	set oCon = server.createObject("adodb.connection")
	oCon.open str  '链接数据库'

	set oCmd = server.createObject("adodb.command")

	oCmd.activeConnection = oCon	'设置cmd对象所属的con对象

```


#### comand对象的属性

activeConnection	**指定command对象所述的connection对象**
commandText			定义命令
commandTimeOut		设置指令执行时间， 0 则不限时
commandType			指定命令类型，优化数据性能
prepared			执行前是否保存命令的编译版本
name 				指定command的名称


#### command对象的方法

execute 		执行字符串个是命令
createParameter 使用指定属性创建parameter对象
cancel			取消执行挂起的异步Execute方法的调用



#### command对象的parameters集合
	
	属性 
		count : 返回command对象的参数的个数
		item  : 返回某个参数
	方法
		append:	调用command 对象的createObject方法创建一个参数后使用 append 将参数添加到 parameters集合中

		delete: 用于删除parameters集合中的parameter对象 

#### parameter对象
	parameters是 command对象的所有参数的集合，而么一个参数就是一个parameter对象，

	parameter对象的属性

	1. Attributes 设置或返回所能接受的任何特殊类型的数据


#### command对象的使用

```
	set oCon = server.createObject("adodb.connection")
	oCon.open str 

	set oCmd = server.createObject("adodb.command")
	set oCmd.activeConnection = oCon

	oCmd.commandText = "select * from student"
	oCmd.commandType = adCmdText
	oCmd.Execute
```
使用这个 command对象  要用activeConnection指明这是哪个链接的命令
然后 使用 .commandText 来执行SQL语句

如果要操作返回记录集
	RS = oCmd.Execute() 操作RS即可

### recordset  对象

1. recordest对象的属性

```html
activeConnection  rw 指向此对象对应的connection

absolutePage	rw 指定当前页

absolutePosition rw 在记录集中的位置序号

source 			rw 用于设置或返回字符串

BOF 			ro 标记， 当前记录位置在recordSet对象的第一个记录之前

EOF 			ro 标记，当前记录位置在recordset对象的最后一个记录之后

CursorLocation 	rw 设置或返回游标位置


cursorType 		rw 在recordSet对象中的游标类型

PageCount 		ro 返回记录集中总的逻辑页数

pagesize		rw 制定逻辑页面的记录个数默认为10

RecordCount	 	ro 	记录集中的记录总数

BookMark		rw 返回唯一标识 recordSet 对象中当前记录的书签， 后者将recordSet对象的当前记录设置为由有效书签所标记的记录

maxRecords	 	rw 限制从数据库中查询返回到一个记录集中的记录数目

```

##### CursorType属性

指示*出在RecordSet对象中游标的类型*

###### 游标的类型

1. adOpenForwardOnly：默认游标，只能在记录集中向前移动，可以进行遍历且速度较快
2. adOpenKeyset：键集游标，游标可以前后移动，其他用户可以修改，但是不能增删
3. adOpenDynameic： 动态游标，可以前后移动， 其他用户对记录的任何操作，都会反应到记录集中，这种游标消耗资源较多
4. adOpenStatic: 静态游标， 可以前后移动，但任何操作不会影响到结果集

##### LockType属性

*当不止一个用户同时改变一个记录时，数据库应如何处理*

1. adLockReadOnly： 默认值   只读锁定，   不允许修改记录
2. adLockPessimistic： 保守是锁定，在编辑一个记录时立即锁定他，即 只能有一个用户进行编辑一条记录
3. adLockOptimistic： 开放是锁定，只有调用update方法才能锁定记录
4. adLockBatchOptimistic： 开放式批锁定，指定记录只能成批的更新

```asp
<%
	set conn =  server.CreateObject("adodb.connection")
	conn.connectionString = "..........."
	conn.open


	set rs = server.createObject("adodb.recordSet")

	rs.open "select * from student", conn, adOpenFrowardOnly, adLockPessimistic
	

	rs.close
	set rs = nothing

	conn.close
	set conn = nothing
%>
```


#### recordset对象的方法

```html
addNew 				向记录集中添加一条新记录
delete 				删除当前记录或记录组
move 				在记录中向前或向后移动指定数目的记录数
moveFirst 			移动到第一条记录
moveLast 			移动到最后一条记录
moveNext 			移动到下一条记录
movePrevious 		移动到前一条记录
open 				打开记录集
close 				关闭记录集
update 				保存对当前记录集所做的修改
getRows 			将记录集中的多个记录读取到数组中
updateBatch 		当记录集处于批量更新模式时，保存对该批量记录的修改

```

##### Open()方法

```html
recordSet.open [source],[activeConnection],[CursorType],[LockType],[options]
'select的SQL语句, conn, 指针类型, 锁定类型, 
```
option参数是  标识 RecordeSet的类型

##### Move()方法

```asp
recordSet.move n, start
'n为要移动的步数，正数前进，负数倒退
'start是一个选择变量，根据有表中的bookMark
'书签值移动指针记录，如果不传BookMark的值，相对于当前记录进行移动
```
用于在记录集中向前或向后移动给定记录个数，

##### getRows() 方法

```asp
myArray = rescordset.getrows(rows, start, fields)
'rows:取出数组的行数，如果省略，那么记录集中所有记录都被取出放入数组中
'start： 指定从何处开始去记录
'fields: 指定要读取的字段
```
用于从数据源中读取数据，将取出的数据放入一个数组中

##### AddNew() 与 Update()方法
使用recordSet对象的AddNew()和Update()方法

```asp
<%
rs.open "......",conn
	rs.addnew
	rs("user") = trim(request("username"))
	rs("pass") = trim(request("password"))
		'...............
rs.update
rs.close
set rs = nothing
%>
'这种方法效率较低,费性能不建议使用'
```

#### recordset对象的fields集合

	fields集合是Recordset对象的字段集合
	感觉像是一个笨重的二维数组,切换到下一行需要 movenext

	count属性： 返回RecordSet的列数，可以用来遍历
	注意是列数 只能遍历curosr指向的这一行

```asp
<%
conn.open
set rs = setver.createObject("adodb.recordset")
rs.open "select * from Student", conn
do while not rs.eof
for i = 0 to rs.fields.count-1
response.writh rs(i) & "&nbsp;&nbsp;"
next
%>
<br>
<%
rs.movenext
loop
rs.close
set rs= notheing 
conn.close
set conn = nothing

%>
```


Item属性： 可以访问RecordSet指定的字段， Item属性是Fields集合的默认属性，一次访问一个字段值时，可以使用一下的几种不同的方法

```asp
RecordSet.Fields.item(2)
RecordSet.Fields.item("name")
RecordSet.fiels(2)
RecordSet.Fields("name")
RecordSet(2)
RecordSet("name")	'直接使用rs.name其实底层是调用了item
```

#### field对象

*fields集合中的一条就是field对象*

- 属性

```asp
actualSize	ro	返回当前记录一个字段的实际长度
attributes 		指定字段的特的属性
defineSize 		在数据源中定义，返回字段的最大尺寸
name 			返回字段的名字
value 			可缺省属性，返回字段值 与 re(i)返回一致
numericScale ro	把序号数字返回给数字型field对象能识别的10进制
originalValue	定义修改前的字段值
precision 		设置或返回可以用field对象中显示数字值得整个数字序号
```



```asp
...

response.write rs(i).name
response.write rs(i).value
response.write rs(i)

...
'这里的i 是 通过0 到 rs.fields.count-1 遍历的 i
```

- 方法 

*如果field对象的Attributes属性取值为adFldLong则可用以下两种方法*

AppendChunk
*使用appendChunk方法将长文本和二进制数据插入到字段中*

GeChunk

*从字段中取出长文本或二进制数据*

```asp
set myChunk = field.getChunk(bytesNum)

```

#### recirdSet对象的使用

返回数据分页

```asp
	RS.PageSize = 5			'设置返回每页数据的个数
	allPage = RS.pageCount 	'根据每页多少数据的到的总页数
	RS.AbsolutePage = 2		'设置RS 返回的是第几页

	'之后对rs进行遍历   以pageSize  每次减一 减到1  截取每页长度

```




编写asp文件时的编码

```asp

<%@ language="vbscript" codepage="65001"%>

```

拼接 json字符串

```asp
<%@ language="vbscript" codepage="65001"%>
<%
set Conn = server.createObject("adodb.connection")
set Rs = server.createObject("adodb.recordSet")

Conn.ConnectionString = "driver={sql server}; server=10.30.1.99;uid=dev;pwd=dev;dataBase=Development"

Conn.Open

dim page, allPage

page = request.Form("page")

Rs.open "SELECT   TOP (200) Phone, Number, Name, Sex, Department, IDCard, JoinDate, Birthday FROM P_User", Conn, 1, 3


If Not (Rs.Bof and Rs.Eof) Then
	Rs.PageSize = 5
	allPage = Rs.pageCount

	' response.write RS.RecordCount
	' response.write page
	Rs.Absolutepage = page

	count = 1
	RequireJsonStr = "{""code"":0,""data"":{"
	do while not (Rs.Bof or Rs.Eof)
		RequireJsonStr = RequireJsonStr & """"&count&""":{""Phone"":"""&Rs("Phone")&""",""Number"":"""& Rs("Number") &""",""Name"":"""&Rs("Name")&""",""Sex"":"""& Rs("Sex") &""",""Department"":"""& Rs("Department") &""",""IDCard"":"""&Rs("IDCard")& """,""JoinDate"":"""&Rs("JoinDate")&""",""Birthday"":"""&Rs("Birthday")&"""},"
		count = count + 1
		Rs.movenext
	loop
	' response.write(len(RequireJsonStr))
	RequireJsonStr = left(RequireJsonStr,len(RequireJsonStr) - 1)
	response.write RequireJsonStr &"},""count"":"&count-1&"}"

	Rs.Close
	set Rs = Nothing

Else
	response.write("无数据")
End If

Conn.close
set Conn = nothing

%>
```