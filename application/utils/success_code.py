# -*- coding: utf-8 -*-
# @Time : 2020/5/8 18:37
# @Author : 司云中
# @File : response_code.py
# @Software: PyCharm

"""
自定义业务逻辑Code
"""

# 验证码验证成功
VERIFICATION_CODE_SUCCESS = 2000

# 登录验证成功
LOGIN_VERIFICATION_SUCCESS = 2002

# 注册验证成功
REGISTER_SUCCESS = 2004

# 邮件验证成功
EMAIL_VERIFICATION_SUCCESS = 2006

# 电话验证成功
PHONE_VERIFICATION_SUCCESS = 2008

# 找回密码验证成功
FIND_PASSWORD_VERIFICATION_SUCCESS = 2010

# 修改密码验证成功
MODIFY_PASSWORD_VERIFICATION_SUCCESS = 2012

# 保存用户信息成功
USER_INFOR_CHANGE_SUCCESS = 2018

# 保存用户信息成功

USER_INFOR_CHANGE_ERROR = 2019

# 绑定手机成功

BIND_SUCCESS = 2021

# 验证码发送成功
SEND_VERIFICATION_CODE_SUCCESS = 2023

# 修改信息成功
MODIFY_INFORMATION_SUCCESS = 2024


class ResponseCode:
    result = {
        'code': '',
        'msg': '',
        'status': '',
        'data': '',
    }

    @property
    def validation_error(self):
        self.result.update(dict(code=VERIFICATION_CODE_SUCCESS, msg='校验成功', status='success'))
        return self.result


response_code = ResponseCode()
