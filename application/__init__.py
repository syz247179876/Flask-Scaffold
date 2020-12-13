# -*- coding: utf-8 -*-
# @Time  : 2020/12/11 下午5:04
# @Author : 司云中
# @File : __init__.py.py
# @Software: Pycharm
from flask import Flask, got_request_exception

from configs import load_config
from extensions.extensions import celery_app, redis_app, sms
from extensions.database import db
from application.signals.handle_signal import signal
from log import setup_log

CONFIGS = {
    "1": "TESTING",
    "2": "DEVELOPMENT",
    "3": "PRODUCTION"
}


def log_exception(sender, exception, **extra):
    """ 记录请求的异常"""
    sender.logger.debug('Got exception during processing: %s', exception)



def create_app():
    """create flask-sports app"""

    app = Flask(__name__)

    app.secret_key = '4A8BF09E6732FDC682988A8SYZ666AB7CF53176D08631E'

    config = load_config(CONFIGS['2'])  # 选择环境

    # load logger
    setup_log(config)

    # load config
    app.config.from_object(config)

    # register blueprint
    # app.register_blueprint(test)

    celery_app.init_app(app)   # 注册celery应用
    redis_app.init_app(app)    # 注册redis应用
    sms.init_app(app)          # 注册阿里云短信服务
    signal.init_app(app)  # 注册发送验证码信号
    db.init_app(app)           # 注册mongodb实例


    with app.app_context():
        # 手动推送上下文
        # get_user_model(app) # 注册用户模型表
        pass

    got_request_exception.connect(log_exception, app) # 记录请求的异常

    return app