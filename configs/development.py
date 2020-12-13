# -*- coding: utf-8 -*-
# @Time  : 2020/12/1 下午11:24
# @Author : 司云中
# @File : development.py
# @Software: Pycharm
import logging
import os

from celery.schedules import crontab
from flask import current_app

from configs.default import DefaultConfig


class DevelopmentConfig(DefaultConfig):
    """the config of development env"""

    # 项目路径
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 密钥!
    SECRET = ''

    # 日志等级
    LOG_LEVEL = logging.ERROR

    # 发行人
    ISSUER = '<someone>:<info>'

    # 私钥文件路径
    PRIVATE_PATH = os.path.join(BASE_DIR, 'keys/private_key.pem')

    # 公钥文件文件路径

    PUBLIC_PATH = os.path.join(BASE_DIR, 'keys/public_key.pem')

    DEBUG = True
    TESTING = False

    JWT_REFRESH_DAY = 7
    JWT_EXPIRE_DAY = 1

    # 注意url的优先级大于db
    MONGODB_SETTINGS = {
        'db': '<db_name>',
        'host': 'mongodb://127.0.0.1:27017/<db_name>'
    }

    # 捆绑API中所有参数的错误
    BUNDLE_ERRORS = True

    CACHE_NAME = 'redis'

    # redis集群
    STARTUP_NODES = [
        dict(host='0.0.0.0', port=6381, password='', db=10),
        dict(host='0.0.0.0', port=6380, password='', db=10),
        dict(host='0.0.0.0', port=6379, password='', db=10),
    ]

    REDIS_DB = {
        'default':
            {
                'host': '0.0.0.0',
                'port': 6381,
                'password': '',
                'db': 1
            },
        'whole':
            {
                'host': '0.0.0.0',
                'port': 6381,
                'password': '',
                'db': 2
            },
        'user':
            {
                'host': '0.0.0.0',
                'port': 6381,
                'password': '',
                'db': 3
            },
        'code':
            {
                'host': '0.0.0.0',
                'port': 6381,
                'password': '',
                'db': 4
            },
        'redis4':
            {
                'host': '0.0.0.0',
                'port': 6381,
                'password': '',
                'db': 5
            },
        'redis5':
            {
                'host': '0.0.0.0',
                'port': 6381,
                'password': '',
                'db': 6
            }
    }


    # 唯一表示redis实例的title
    REDIS_TITLE = 'title'

    # celery broker
    CELERY_BROKER_URL = 'redis://@127.0.0.1:6379/0'

    # celery backend
    CELERY_RESULT_BACKEND = 'redis://@127.0.0.1:6379/1'

    CELERY_TASK_SERIALIZER = 'json'

    CELERY_RESULT_SERIALIZER = 'json'

    CELERY_TASK_NAME = ''

    # 异步任务
    CELERY_BEAT_SCHEDULE = {
        'rewrite_step_counter': {
            'task': '',
            'args':('',),
            'schedule': crontab(minute=1, hour=0),
        }
    }

    # 阿里云短信参数
    ACCESS_KEY_ID = ''
    ACCESS_KEY_SECRET = ''
    REGION = ''
    SIGN_NAME = ''  # 短信签名

    # 不同的短信模板
    TEMPLATES_CODE_LOGIN = ''
    TEMPLATES_CODE_REGISTER = ''
    TEMPLATES_CODE_IDENTIFY = ''
    TEMPLATES_CODE_MODIFY_PASSWORD = ''
    TEMPLATES_CODE_RETRIEVE_PASSWORD = ''

    # OSS对象存储

    OSS_ENDPOINT = ''

    OSS_BUCKET_NAME = ''

    OSS_BASE_URL = '' # 用于拼接返回给用户的url

    # 加密算法
    PASSWORD_HASHERS = [
        'application.utils.crypto.pbkdf2_crypto'
    ]

    # 认证模型类
    AUTH_USER_MODEL = 'application.models.user_model.User'  # example

    # 模型模块
    APPLICATION_MODELS_MODULE = [
        'application.models.user_model.Address',   # example
    ]


development_config = DevelopmentConfig()
