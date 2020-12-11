# -*- coding: utf-8 -*-
# @Time  : 2020/12/1 下午11:34
# @Author : 司云中
# @File : wsgi.py
# @Software: Pycharm

# gunicorn 启动
from application import create_app
app = create_app()
celery = app.config.get('CELERY_INSTANCE')  # celery -A wsgi:celery worker -l info

if __name__ == '__main__':
    # 启动flask服务
    app.run(host='127.0.0.1', port=5001)
