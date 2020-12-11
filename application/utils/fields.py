# -*- coding: utf-8 -*-
# @Time  : 2020/12/3 上午12:22
# @Author : 司云中
# @File : fields.py
# @Software: Pycharm

from flask_restful import fields
import re

def phone_string(value):
    """手机号输入类型"""
    if len(value) != 11 or re.match(r'13[0-9]{9}|15[0-9]{9}', value) is None:
        raise ValueError('手机号格式不合法')
    return value

def password_string(value):
    """密码输入类型"""
    if len(value) < 8 or len(value) > 20 or re.match(r'^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,20}$', value) is None:
        raise ValueError('密码至少包含 数字和英文，长度6-20,不能出现非法字符')
    return value

def identify_code_string(value):
    """验证码输入类型"""
    if re.match(r'^[0-9A-Za-z]{5}', value) is None:
        raise ValueError('验证码格式不正确')
    return value

def get_params_int(value):
    """GET请求时 ,int类型参数校验错误"""
    value = int(value)
    if not isinstance(value, int) or value > 9999999 or value < 1:
        raise ValueError('请求的参数不规范')
    return value

def username_string(value):
    """用户名输入类型"""
    if len(value) > 20 or len(value) < 1:
        raise ValueError('用户名格式不正确')
    return value

class PhoneString(fields.Raw):
    """构建手机号字段"""
    def format(self, value):
        if len(value) != 11 or re.match(r'13[0-9]{9}|15[0-9]{9}', value) is None:
            raise ValueError('手机号格式不合法')
        return value

class PasswordString(fields.Raw):
    """构建密码字段"""
    def format(self, value):
        if len(value) < 8 or len(value) > 20 or re.match(r'^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,20}$', value) is None:
            raise ValueError('密码至少包含 数字和英文，长度6-20,不能出现非法字符')
        return value

class IdentifyingCodeString(fields.Raw):
    """构建验证码字段"""
    def format(self, value):
        if re.match(r'^[0-9A-Za-z]{6}', value) is None:
            raise ValueError('验证码格式不正确')
        return value