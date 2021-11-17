# 常用搜索引擎语法

- 好像并不怎么好用。。。。

关键字 | 功能 | 示例
-|-|-
intitle | 搜索标题中含有关键字的网站 | intitle: xxx
intext | 搜索正文中含有关键字的网站 | intext: xxx
site | 搜索域名下的所有网页 | site: www.baidu.com

## 常见攻击手段

- 客户端

    - xss
    - csrf
    - 点击劫持
    - url跳转
- 服务端
    - sql注入
    - 命令注入
    - 文件操作类

### 暗链

- 功能
    - 黑客攻破网页植入  链接  提升seo
- 发现
    - intext: www.sajinn.com    搜索常用的暗链链接

### webshell

- 实现

    - 通过手段黑进服务器，在服务器内上传webshell 软件，之后即可  远程链接，完成大操作。
