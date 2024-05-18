# [django](https://docs.djangoproject.com/zh-hans/5.0/intro/overview/)

- web 框架

## install

    ```shell
    $ pip3 install django
    $ python -m django --version
    ```

## create project

- startproject

    ```shell
    $ django-admin startproject mysite
    ```

- 目录结构 

    ```py
    mysite/
        manage.py           # 管理
        mysite/             # 
            __init__.py
            settings.py
            urls.py
            asgi.py
            wsgi.py
    ```