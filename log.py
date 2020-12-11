# -*- coding: utf-8 -*-
# @Time  : 2020/12/1 下午11:28
# @Author : 司云中
# @File : log.py
# @Software: Pycharm

import logging
import os
from logging.handlers import RotatingFileHandler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def setup_log(config):
    """配置日志"""

    # 设置日志的记录等级
    logging.basicConfig(level=config.LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler(os.path.join(BASE_DIR, "logs/log-{level}".format(level=config.LOG_LEVEL)), maxBytes=1024 * 1024 * 100,
                                           backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)