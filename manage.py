# -*- coding: utf-8 -*-
# @Time  : 2020/12/1 下午11:28
# @Author : 司云中
# @File : manage.py.py
# @Software: Pycharm

from application import create_app
from flask_script import Manager, Server

from application.models import get_user_model


app = create_app()
User = get_user_model(app)
manager = Manager(app)
# 使用python manage.py runserver启动服务器
manager.add_command('runserver', Server)

@manager.shell
def make_shell_context():
    return dict(app=app, User=User)

if __name__ == '__main__':
    # 启动flask服务
    manager.run()