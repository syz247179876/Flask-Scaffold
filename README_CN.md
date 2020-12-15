### 各位好呀~

[英文版](https://github.com/syz247179876/Flask-Scaffold/blob/main/README.md)

### 介绍

这是一个基于flask框架的脚手架,目前已经已成了一些常用的插件,有些插件是本人自己集成到application中的,可能考虑不全,还请谅解,我会不断的完善!

您的项目可以基于此脚手架上进一步开发!

在之后,我会不断的完善该脚手架,任何对此项目有兴趣的朋友们都可以加入我一起完善!

### 如何开始

1. `git clone https://github.com/syz247179876/Flask-Start.git`

2. `pip install -r requirements.txt`

3. 开发及享受编码过程吧~

### 细节

目前以下的库或插件已经被该脚手架支持

1. 支持 Redis

2. 支持 Mongodb

3. 支持 Mysql

3. 支持 Celery and Celery-Beat

4. 支持 Aliyun SMS

5. 支持 Hash encryption

6. 支持 Jwt

7. 支持 Nginx ,已在脚手架中放置Nginx.conf

8. 支持 Gunicon ,已在脚手架中放置Gunicon.conf

9. 支持 Supervisord ,已在脚手架中放置supervisord_flask

10.支持 oss

### 您需要的额外的服务

请去官网安装配置好redis,mongodb,mysql等服务

### 项目启动文件

`python -m wsgi` or `python manage.py runserver`

### 项目文件目录

```shell
root:[/home/syz/FlaskLearning/Flask-Start]
+--requirements.txt
+--wsgi.py
+--tests
|      +--__init__.py
+--depoly
|      +--supervisord_flask
|      +--__init__.py
|      +--nginx.conf
|      +--gunicorn.conf
+--application
|      +--urls
|      |      +--__init__.py
|      |      +--user_urls.py
|      +--tasks
|      |      +--__init__.py
|      |      +--send_code.py
|      +--__init__.py
|      +--signals
|      |      +--__init__.py
|      |      +--signal.py
|      |      +--handle_signal.py
|      +--utils
|      |      +--qq_oauth.py
|      |      +--__init__.py
|      |      +--api_permission.py
|      |      +--exception.py
|      |      +--success_code.py
|      |      +--json.py
|      |      +--fields.py
|      +--models
|      |      +--__init__.py
|      +--api
|      |      +--__init__.py
+--extensions
|      +--__init__.py
|      +--hasher.py
|      +--sms.py
|      +--extensions.py
|      +--celery_app.py
|      +--crypto.py
|      +--database.py
|      +--redis.py
+--logs
+--README.md
+--configs
|      +--__init__.py
|      +--testing.py
|      +--default.py
|      +--development.py
|      +--production.py
+--log.py
+--manage.py
```


