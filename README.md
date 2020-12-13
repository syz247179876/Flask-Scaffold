### Hello EveryBody!

[中文版](https://github.com/syz247179876/Flask-Scaffold/blob/main/README_CN.md)

[英文版](https://github.com/syz247179876/Flask-Scaffold/blob/main/README.md)

### Introduction

This is a scaffold based on the flask framework, including common plugins, such as redis, mongodb, mysql, jwt. 

Your project can be developed based on this scaffold.

In the future, i will continue to improve this scaffold, any person who interested in can join me to perfect this scaffold 


### How to Start

1. `git clone https://github.com/syz247179876/Flask-Start.git`

2. `pip install -r requirements.txt`

3. developing and enjoy yourself

### Details

Now the following plugin liberay that this scaffold support:

1. Support Redis

2. Support Mongodb

3. Support Mysql

3. Support Celery and Celery-Beat

4. Support Aliyun Short Message

5. Support Hash encryption

6. Support Jwt

7. Support Nginx Config

8. Support Gunicon Config

9. Support Supervisord Config to manage above progresses

### Service you need

Please go to official website to download Redis, Mongodb

### Startup File

`python -m wsgi` or `python manage.py runserver`

### Project File directory

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

