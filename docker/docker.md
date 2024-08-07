# docker

- 容器化应用    docker运行多个相互隔离app 
- 比虚拟机性能、资源利用率高
- app之间 文件、资源、网络隔离
- 变更管理、日志记录
- 写时复制  部署变快
- 操作系统 -> docker ->app 
    - 在一台安装docker的服务器下启动app1， 换另外的任何操作系统计算机，只要同样安装docker 就可以直接run拉取
    - 不同服务器版本  docker去解决


## 安装Docker[github](https://github.com/docker/docker-install)

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
    # 下载
    $ sudo chmod +x /usr/local/bin/docker-compose
    # 赋予执行权限
    $ docker-compose --version

   ```
3. 更换中国源

    ```js
   
    // /etc/docker/daemon.js
  
    {
    "registry-mirrors":["https://registry.docker-cn.com"]
    }

    ```


## 命令  

1. 常用命令

    命令 | 功能
    -|-
    docker run xxx | 启动xxx容器
    docker stop xxx | 启动xxx容器
    docker ps -a | docker运行状态
    docker rm xxx | 删除停止的xxx(名称或id)容器   
    docker logs | 日志

2. docker Compose 集合命令 一条命令执行多个容器

    - docker-compose.yml 配置文件

        ```yml
        # 空格缩进 
        # 冒号后面 一定有空格否则报错
        version: '3'
        services:
        mysql1:
            image : mysql  # 镜像
            environment:   # 环境变量
            - MYSQL_ROOT_PASSWORD=123456
            ports:         # 端口映射
            - 28002:3306  
        mysql2:
            image : mysql
            environment:
            - MYSQL_ROOT_PASSWORD=123456
            ports:
            - 28003:3306

        ```

    - docker-compose up -d 在后台同时启动多个服务

    命令 | 功能
    -|-
    docker-compose up | 根据docker-compose.yml 启动服务
    docker-compose stop | 停止服务
    docker-compose rm | 移除服务


## [docker hub](https://hub.docker.com/u/96weibin)

1. 登录 

    ```shell
    $ docker login
    ```
2. 提交推送

    ```shell
    $ docker ps # commit提交  container id
    $ docker commit 6a5df50548a3 96weibin/omysql:1.0.1  # ：设置版本号tag
    $ docker push 96weibin/omysql:1.0.1   # 推送到dockerhub
    ```
3. 拉取镜像

    ```shell
    $ docker image rm 96weibin/omysql:1.0.1 #删除之前创建的镜像
    $ docker pull 96weibin/omysql:1.0.1     #下载镜像
    ```


    