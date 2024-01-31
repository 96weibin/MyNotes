# movie-web

### backend
1. 安装 [docker-desktop](https://www.docker.com/)

2. 创建 network

```shell
$ docker add network my_network
```

2. 在docker容器中安装 postgresql

```shell
$ docker pull postgres

# 拉取镜像

$ docker run --name postgrescontainer -e POSTGRES_PASSWORD=test1234 -d --network my_network postgres

# 名字 postgrescontainer
# 密码 test1234
# 网络 my_network

# 运行 movie-web

$ docker run \
    -p 80:80 \
    -e MWB_POSTGRES__CONNECTION=postgres://postgres:"test1234"@postgrescontainer:5432 \
    -e MWB_CRYPTO__SESSION_SECRET=add-your-own-secret123bcdjqwerqsjkllhhhfff38872nnnl \
    -e MWB_META__NAME=unofficial-movie-web \
    --network my_network \
    ghcr.io/movie-web/backend:latest

```

TODO。issue。here

```txt
error:   ▪ error: select "u0"."namespace", "u0"."count" from "users" as "u0" group by "u0"."namespace" - relation "users" does not exist +10ms
 ELIFECYCLE  Command failed with exit code 1.
```
