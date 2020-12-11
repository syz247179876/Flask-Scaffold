# -*- coding: utf-8 -*-
# @Time  : 2020/12/11 下午5:05
# @Author : 司云中
# @File : __init__.py.py
# @Software: Pycharm

import os

from flask import current_app
from werkzeug.utils import import_string
from application.utils.exception import ImproperlyConfigured

def get_model(import_name):
    """获取具体module下的model_name"""
    model_name = import_string(import_name)
    return model_name

def get_user_model(app):
    """
    Return the User model that is active in this project.
    """
    try:
        app.config.setdefault('AUTH_USER', get_model(current_app.config.get('AUTH_USER_MODEL')))
    except ValueError:
        raise ImproperlyConfigured("AUTH_USER_MODEL must be of the form 'app_label.module.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "AUTH_USER_MODEL refers to model '%s' that has not been installed" % current_app.config.get('AUTH_USER_MODEL')
        )

def import_models(module):
    model_dict = {}
    for root, dirs, files in os.walk(module):
        # 获取目录下所有文件文件
        for file in files:
            if os.path.splitext(file)[0].endswith('_model'):
                model_dict[os.path.splitext(file)[0]] = get_model(module)


def register_all_model(app):
    """
    Register all models file which end with '_model' in application
    """

    try:
        model_dict = {}
        modules = current_app.config.get('APPLICATION_MODELS_MODULE')
        for module in modules:
            model_dict[module.rsplit('.', 1)[1]] = get_model(module)  # {'模型名':模型类}
        app.config.setdefault('models', model_dict) # 添入dict
    except ValueError as e:
        raise ImproperlyConfigured("APPLICATION_MODELS_MODULE must be of the form 'app_label.module.model_name'")