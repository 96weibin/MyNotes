# linux

## centos

1. 查看磁盘

    ```shell
    df -Th
    ```
2. 文件结构 ls -la

    目录 | 功能
    -|-
    home | 个人
    etc | 配置文件
    usr | 可执行文件
    usr/sbin | 超级管理员执行文件
    usr/local | 本地执行文件
    var | www等常变目录
3. 查看运行的进程 top

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
    - yum upgrade    只更新软件

### 远程工具  xshell  putty

- ssh

    ```shell
    $ ssh -p port user@address
    ``` 

### 安装node


### 安装Docker[github](https://github.com/docker/docker-install)

1. docker 
    ```shell
    $ curl -fsSL https://get.docker.com -o get-docker.sh
    $ sh get-docker.sh
    $ docker -v  #已经安装好了
    $ service docker restart # 重启docker 
    ```
2. 集合命令工具[docker compose](https://docs.docker.com/compose/install/)
   
    ```shell
    $ sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

    $ sudo chmod +x /usr/local/bin/docker-compose
    
    $ docker-compose --version

   ```
3. 更换中国源

    ```js
   
    // /etc/docker/daemon.js
  
    {
    "registry-mirrors":["https://registry.docker-cn.com"]
    }

    ```
4. 安装mongo从[docker hub](https://hub.docker.com/_/mongo)

    ```shell
    $ docker pull mongo:4 # 可以用冒号指定版本  默认最新版
    ```
5. 查看docker 命令

    ```shell
    $ docker images # 查看已安装的镜像
    $ docker ps     # 正在运行的docker 服务
    ```
6. 运行mongo
    ```shell
    $ docker run -d --name some-mongo -p 10050:27017 mongo:4
      # -d        服务端
      # --name    命名为
      # -p        指定端口
      # 10050:27017    指定10050给默认端口27017使用
    ```
7. 防火墙放行端口

    ```shell
    $ service firewalld stop  #关闭防火墙
    # 或者
    $ service firewalld start #开启防火墙
    $ firewall-cmd --zone=public --add-port=10050/tcp --permanent 
    # 放行10050                                          永久
    $ firewall-cmd --reload # 重启防火请
    ```
8. [robo 3t 可视远程mongo](https://robomongo.org/download)

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
    **```****`**
    ```js
    location /node{
        root '/etc/www';
        index index.html index.php;
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
    // etc/nginx/conf.d/default.conf
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



### 安装数据库 mariaDB 

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

### 安装yarn [官网](https://yarn.bootcss.com/docs/install/#centos-stable)

- 比npm快，支持离线下载

    ```shell
    $ curl --silent --location https://dl.yarnpkg.com/rpm/yarn.repo | sudo tee /etc/yum.repos.d/yarn.repo

    $ sudo yum install yarn

    $ yarn config set registry http://registry.npm.taobao.org/
    # 设置淘宝源
    ```

    命令 | 功能
    -|-
    yarn init | 生成package,json
    yarn add xxx |  安装依赖
    yarn add xxx -D | 安装开发依赖
    yarn upgrade xxx | 更新依赖
    yarn remove xxx | 移除依赖
    yarn 或 yarn install | 安装 package.json 里的全部依赖

### 常用命令 

1. 文件相关

    操作指令|功能
    -|-
    ls | 显示当前目录下文件(不包括隐藏文件)
    ll | 显示当前目录下文件 详细
    cd . | 当前目录
    mkdir xxx | 创建目录
    touch xxx | 创建文件
    cat xxx | 查看文件
    echo 'hello' >> xxx | 向xxx末尾插入hello
    echo 'hello' >> xxx | 覆盖xxx为hello
    rm xxx |  删除文件
    rm -r xxx | 删除目录
    rm -rf xxx | 强制(force)删除目录 
    find / \| grap ifcfg | find /(从根找所有文件)  \| (管道) grap(正则匹配) ifcfg 

2. 下载解压压缩
    操作指令|功能
    -|-
    tar zxvf xxx | (z .gz结尾) (x 解压缩) (v 显示过程)  (f使用xxx名)
    tar zcvf xxx.gz yyy zzz | 将yyy、zzz压缩 名为xxx.gz

3. 进程
    操作指令|功能
    -|-
    systemtcl start xxx | 执行xxx执行文件
    systemtcl daemon-reload | 重启后台程序
    systemtcl restart xxx  | 重启xxx
    systemtcl stop xxx  | 停止xxx
    systemtcl status xxx  | 查看xxx运行状态
