# -*- coding: utf-8 -*-
# @Time  : 2020/12/11 下午5:06
# @Author : 司云中
# @File : __init__.py.py
# @Software: Pycharm

import os

def load_config(mode=os.environ.get('MODE')):
    """
    load config which would be required in
    different environment decided by param 'mode'
    """
    try:
        if mode == 'TESTING':
            from .testing import testing_config
            return testing_config
        elif mode == 'PRODUCTION':
            from .production import production_config
            return production_config
        elif mode == 'DEVELOPMENT':
            from .development import development_config
            return development_config
    except ImportError:
        from .default import default
        return default

__all__ = ['load_config']