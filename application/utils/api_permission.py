# -*- coding: utf-8 -*-
# @Time  : 2020/12/10 下午2:18
# @Author : 司云中
# @File : api_permission.py
# @Software: Pycharm
import functools
from flask import g

from application.utils.exception import ApiPermissionError


def api_permission_check(func):
    """API权限检查装饰器"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user = getattr(g, 'user')
        if user.check_permission():
            return func(*args, **kwargs)
        raise ApiPermissionError()
    return wrapper