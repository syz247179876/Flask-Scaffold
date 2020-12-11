# -*- coding: utf-8 -*-
# @Time  : 2020/12/11 下午5:29
# @Author : 司云中
# @File : send_code.py
# @Software: Pycharm

# -*- coding: utf-8 -*-
# @Time  : 2020/12/4 上午4:06
# @Author : 司云中
# @File : task.py
# @Software: Pycharm
import uuid

from extensions.sms import sms
from flask import current_app


def send_phone(sender, phone_numbers, template_code, template_param):
    """发送手机验证码"""
    _business_id = uuid.uuid1()
    sms.send_sms(_business_id, phone_numbers=phone_numbers, sign_name=current_app.config.get('SIGN_NAME'),
                 template_code=template_code,
                 template_param=template_param)
