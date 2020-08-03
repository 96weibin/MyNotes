# IndexedDB

* 类似于 local storage 和 section storage的浏览器端本地存储 

	**但是他是  非关系型   指针类型  数据库**
 *

## 判断浏览器是否支持

```js
	window.indexedDB = window.indexedDB || window.mozIndexedDB || window.webkitIndexedDB || window.msIndexedDB;
	if(!window.indexedDB) {
		//不支持   IndexedDB
	}
```

## 操作数据库

### 打开数据库

```js
	var request = window.indexedDB.open('DBName',version);
	/**
	* 此 request 有三个状态  onupgradeneeded(升级需要？？？？), onsuccess, onerror
	* request 就是返回了一个 IDBOpenDBRequest对象  包含了 以上三个函数.
	* 其中  onupgradeneeded 是最为重要的  当版本改变的时候 触发（第一次也是  作为初始化使用）
	* 这三个事件最先  触发  onupgradeneeded  然后根据情况  会运行 onsuccess 或 onerror
	*/
```

### onupgradeneeded 

#### 初始化数据库
```js
	request.onupgradeneeded = function(event){
		/*
		*创建objectStore名为objectStoreName 主键为 goodsName 是否自增 为 true
		*/

		var objectStore = request.result.createObjectStore('objectStoreName', keyPath: 'goodsName',autoIncrement: ture);
		


		//创建index

		objectStore.createIndex('goodsName', 'goodsName', {unique: true});
		objectStore.createIndex('goodsPrice', 'goodsPrice', {unique: false});
		objectStore.createIndex('goodsNumber', 'goodsNumber', {unique: false});
		/*
		* 这里再利用createIndex在 objectStore 里面创建index 传的前两个参数
		* 设置成一样的就好，感觉设置成不一样的是自己给自己找事情，就是创建的
		* index 的名字  和 索引时的名字  用一个就好    然后第三个参数是  
		* 是否唯一  
		*/


		//在这里给数据进行    逻辑操作  事件绑定
	};

```

#### 功能函数

```js
	//这里定义的功能函数 是在用来在   onupgradeneeded中调用的
```

IndexedDB的操作都是基于  交易的  开启一个交易可以执行多个操作，如果任何一个操作失败，那么所有操作被还原，

- 开启交易

```js
	transaction = db.transaction('Goods', 'readwrite'),	
	/*创建与objectStore的交易
	*第一个参数   是objectStore的名字
	*第二个参数   是权限  有readonly readewrite 
	*/
	tStore = transaction.objectStore('Goods');
	/*
	* 获取 要交易的objectStore
	*/
```


- indexedDB 操作都是基于 交易的，下面的增删改查各个操作，都需要创建对应的交易，
以及找到对应交易的objectStore，来进行操作。



##### 增加
```js
	putRequest = tStore.put({goodsName: gName, goodsPrice: gPric, goodsNumber: gNum});
	/*
	* put 如果要增加的数据已经存在，则会更新
	*/
	addRequest = tStore.add({goodsName: gName, goodsPrice: gPric, goodsNumber: gNum});
	/*
	* add 只能用于添加数据库中没有的数据
	*/
```

##### 查询
```js
	var index = sStore.index('goodsName'),
		sRequest = index.openCursor(IDBKeyRange.only(search.value),IDBCursor.NEXT);
	/*
	*	调用指针对象查询 
	*/

```

##### 删除
```js
	request = delStore.delete(delName.value);
```

### onsuccess 

这个是与onupgradeneeded相对应的 数据库打开成功
```js
	request.onsuccess = function (evnent) {
		/*
		* 没啥事 就是告诉开成功了  功能的设置都在onupgradeneeded 里面 
		*/
	}

```

### onerror 

这个是与onupgradeneeded相对应的 数据库打开失败
```js
	request.onerror = function (event) {
		console.log('DB open fail')
		console.log(event.target.error.message);
		/*
		* 这个事件相比onsuccess还是有些用的 通过传进函数的  evnet 找到打开失败的原因
		* 小编  就遇到了 错误  "The user denied permission to access the database."
		* chrome 如果禁止了 cookie   这个数据库就不能使用了  ，  所以 在设置中打开cookie就好了
		* 所以 本人感觉  这样轻易就不能用了  而且 浏览器 并不都支持  
		* 这个 indexedDB 还是需要在经过一段时间的发展 才会普遍应用
		*/
	}

```