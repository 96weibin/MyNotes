# [django](https://docs.djangoproject.com/zh-hans/5.0/intro/overview/)

- web 框架

- MVT

```py
ORM Model  - view.py - Template

对象数据映射  - view.py - html
```

## install

    ```shell
    $ pip3 install django
    $ python -m django --version
    ```

## create project

- dajango-admin 

    ```py
    $ django-admin

    ```
    ```txt
    Type 'django-admin help <subcommand>' for help on a specific subcommand.

    Available subcommands:

    [django]
        check
        compilemessages
        createcachetable
        dbshell
        diffsettings
        dumpdata
        flush
        inspectdb
        loaddata
        makemessages
        makemigrations
        migrate
        optimizemigration
        runserver
        sendtestemail
        shell
        showmigrations
        sqlflush
        sqlmigrate
        sqlsequencereset
        squashmigrations
        startapp
        startproject
        test
        testserver
    ```

- startproject

    ```shell
    $ django-admin startproject mysite
    ```

- 目录结构 

    ```py
    mysite/
        manage.py           # 管理 cli 工具
        mysite/             # 
            __init__.py     # 
            settings.py     # 配置
            urls.py         # 路由
            asgi.py         # 兼容 ASGI的web服务器入口
            wsgi.py         # 兼容 WSGI的Web服务器入口
    ```

## 配置路由

### path 函数
- path(route, view, kwargs=None, name=None)
    - route 可以包含变量的 路由
    - 视图函数  返回一个函数或一个基于类的视图
    - kwargs  （可选） 字典
    - name (可选) 唯一名称
```py
# urls.py
from django.urls import include, re_path

urlpatterns = [
    re_path(r'^index/$', views.index, name='index'),    
    re_path(r'^bio/(?P<username>\w+)/$', views.bio, name='bio'),    # 正则url
    re_path(r'^weblog/', include('blog.urls')),    # 引用其他 rul
    ...
]
```

## 末班
