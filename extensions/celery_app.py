# -*- coding: utf-8 -*-
# @Time  : 2020/12/3 上午9:50
# @Author : 司云中
# @File : celery_app.py
# @Software: Pycharm

from __future__ import absolute_import, unicode_literals
from celery import Celery
from werkzeug.utils import import_string


def get_model(import_name):
    """获取具体module下的model_name"""
    model_name = import_string(import_name)
    return model_name


class PyCelery(object):
    """Manages the creation of celery for your Flask app"""

    def __init__(self, app=None, name=None, config=None, *args, **kwargs):
        if app is not None:
            self.init_app(app, name, config, *args, **kwargs)
            self.app = app

    def init_app(self, app, name=None, config=None, *args, **kwargs):
        """
        Initialize this :class:`PyCelery` for use.
        """
        if name is None:
            name = app.config.get('CELERY_TASK_NAME', app.name)
        if config is None:
            config = app.config

        celery = Celery(name, broker=app.config['CELERY_BROKER_URL'])
        celery.config_from_object(config, namespace='CELERY')  # 指明配置前缀
        # celery.autodiscover_tasks()
        app.config.update({'CELERY_INSTANCE': celery})
        self.configure_celery(app, celery)

        setattr(self, 'app', app)

    def scan_tasks(self, app):
        """
        扫描配置文件中所有的任务
        :return task func tuple
        """
        tasks_func = app.config.get('CELERY_TASKS_FUNC')
        tasks_func_instance = (get_model(func) for func in tasks_func)
        return tasks_func_instance

    def register_task(self, app, celery):
        """
        注册所有任务任务到Celery
        :param celery: celery instance
        :param funcs: 所有任务函数
        :return: 任务dict
        """
        task_dict = {}
        tasks_tuple = self.scan_tasks(app)
        task_dict = {task_dict.update({task.__name__: celery.task(task)}) for task in tasks_tuple}
        return task_dict

    def configure_celery(self, app, celery):
        """
        向app中添加tasks
        :param app: flask应用
        :param celery: celery instance
        """
        tasks = self.register_task(app, celery)
        setattr(app, 'tasks', tasks)


celery_app = PyCelery()  # celery application