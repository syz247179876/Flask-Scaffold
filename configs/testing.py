# -*- coding: utf-8 -*-
# @Time  : 2020/12/1 下午11:24
# @Author : 司云中
# @File : testing.py
# @Software: Pycharm
from configs.default import DefaultConfig


class TestingConfig(DefaultConfig):
    """the config of testing env"""
    DEBUG = True
    TESTING = True


testing_config = TestingConfig()