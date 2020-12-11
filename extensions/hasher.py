# -*- coding: utf-8 -*-
# @Time  : 2020/12/4 下午4:34
# @Author : 司云中
# @File : hasher.py
# @Software: Pycharm
import functools

from werkzeug.utils import import_string
from extensions.extensions import encryption
from application.utils.exception import ImproperlyConfigured
from flask import current_app

def get_salt(salt):
    return salt or 'https://syzzjw.cn/'

def check_password(raw_password, password, salt=None):
    """
    校验密码
    Validating the password supported
    """
    salt = get_salt(salt)
    if password == encryption.encode(raw_password,salt):
        return True
    return False


def make_password(password, salt=None, hasher='default'):
    """
    加密
    Turn a plain-text password into a hash for database storage
    """

    # hasher = get_hasher(hasher)
    #
    # salt = salt or hasher.salt()
    # return hasher.encode(password, salt)

    salt = get_salt(salt)
    return encryption.encode(password, salt)



@functools.lru_cache()
def get_hashers():
    """
    从settings.py中动态导入一连串hashers对象
    Read list of hashers from app.settings.py
    """
    hashers = []
    # 导入报名
    for hasher_path in current_app.config.get('PASSWORD_HASHERS'):
        hasher_cls = import_string(hasher_path)
        hasher = hasher_cls()
        hashers.append(hashers)
        if not getattr(hasher, 'algorithm'):
            raise ImproperlyConfigured("hasher doesn't specify an "
                                       "algorithm name: %s" % hasher_path)
        hashers.append(hasher)
    return hashers


@functools.lru_cache()
def get_hashers_by_algorithm():
    """以字典形式重构加密模块"""
    return {hasher.algorithm: hasher for hasher in get_hashers()}


def get_hasher(algorithm='default'):
    """
    返回配置中加密实例
    Return an instance of a loaded password hasher
    :param algorithm: the algorithm to encrypt
    :return: hasher
    """

    if hasattr(algorithm, 'algorithm'):
        return algorithm

    elif algorithm == 'default':
        return get_hashers()[0] # retrieve the first algorithm of list

    else:
        hashers = get_hashers_by_algorithm()
        try:
            return hashers[algorithm]
        except KeyError:
            raise ValueError("Unknown password hashing algorithm '%s'. "
                             "Did you specify it in the PASSWORD_HASHERS "
                             "setting?" % algorithm)
