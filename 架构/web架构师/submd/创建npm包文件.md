# 创建npm包文件

1. init

```shell
$ mkdir wb
$ cd wb
$ npm inint 
# 注意 name 要独一无二， 不能与已有的公共库 重名
```

- package.json

```json
{
  "name": "wb230904",
  "version": "1.0.0",
  "description": "package setst",
  "main": "index.js",
  "bin": {
    "wb": "bin/index.js"
  },
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [
    "pkg"
  ],
  "author": "96weibin",
  "license": "ISC"
}
```
> 添加bin 指定执行文件

2. 创建执行文件 bin/index.js

``` js
#!/usr/bin/env node
// 启用环境变量中的node
console.log('this is a cli test');
```

