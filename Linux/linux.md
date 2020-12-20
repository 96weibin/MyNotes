# linux

## centos

### 连网

- 方法一
    1. 找到网卡cd /etc/sysconfig/network-scripts/ifcfg-eth0 网卡
    2. 开机启动网卡 vi ifcfg-eth0  修改 onBoot = yes
    3. 重启网络服务 service network restart
- 方法二 
    1. cd /etc/init.d/network restart

### yum(linux 版本管理器)

1. 更改yum源 [网易源](http://mirrors.163.com/.help/centos.html)

```js
$ yum install wget
//wget url 下载url对应资源
$ mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
//备份yum配置文件
$ wget http://mirrors.163.com/.help/CentOS7-Base-163.repo
//下载新的yum配置文件
$ yum clean all  
//清理 yum缓存
$ yum makecache
//重写yum 缓存
```

2. 更新  
    - yum update -y  系统 和软件都更新
    - yum upgrade    只更新系统

### 远程工具  xshell  putty

### vi vim 文本工具

1. 安装 yum install vim -y

2. 使用  


命令模式 | 编辑
-|-
i | 输入
:q | 退出
:wq | 保存退出 
:q! | 不保存退出
i | 当前位置插入
o | 当前位置前一行插入

### 安装nginx

1. [nginx 官网 linux源配置安装](http://nginx.org/en/linux_packages.html#RHEL-CentOS)

2. centOS SELinux 防火墙

```shell
$ iptables -L -n #查看规则
$ iptables -f    #清除一切规则
$ iptables -A INPUT -p tcp --dport 8080 -j ACCEPT # 配置8080端口可入
```

3. 重新指定 配置文件

```shell
$ nginx -c /etc/nginx/nginx.conf
# centOS配置源yum安装 需要指定配置文件
```

4. 关闭seLinux  对http服务请求限制

```
$ setsebool -P httpd_can_network_connect 1
```
- 或者 /etc/eslinux/config 设置 ESLinun=disable

5. 配置端口转发  /etc/nginx/conf.d/default.conf
    - 通过 特殊路由  共用80端口
    - http://111.229.241.56/node
```js
location /node{
    proxy_pass http://111.229.241.56:8080;
    //转发端口
    proxy_set_header Host $host;
    //重置req.header.host
}
```
6. 反向代理 
    - 将其他页面通过 *端口转发* 将其他跨域的资源代理到本服务器对应端口
    - 通过 ./  访问原本跨域的资源
    - http://111.229.241.56/dn

```js
location /dn{
    proxy_pass        https://www.157299.cn/;
}
```
```js
$.ajax('http://111.229.241.56/baidu').then(
    (res)=>{console.log(res)},
    (err)=>{console.log('filed')}
    )
//通过  访问本源/nd  ajax 读取到了dn的数据
```
7. nginx命令

```shell
    
$ /usr/sbin/nginx -s quit   # 启动
$ /usr/sbin/nginx -s reload # 重启

```



### 安装数据库 mariaDB [腾讯云教程](https://cloud.tencent.com/document/product/213/38056)

- 原 mySql作者  开发的 与mySQL基本一样

    1. install安装

    ```shell
    $ yum install mariadb-server
  
    $ mysql_install_db
    ```

    2. 选择配置文件

    ```
    $ cp /usr/share/mysql/my-small.cnf /etc/my.cnf
    ```

    3. 启动

    ```shell
    $ mysqld_safe # mysql 安全启动   会挂起
    # mysqld  d 是指服务端    

    $ service mariadb start
    ```




操作指令|功能
-|-
ls | 显示当前目录下文件(不包括隐藏文件)
ll | 显示当前目录下文件 详细
cd . | 当前目录
find / \| grap ifcfg | find /(从根找所有文件)  \| (管道) grap(正则匹配) ifcfg 

