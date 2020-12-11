# -*- coding: utf-8 -*-
# @Time  : 2020/12/4 上午2:07
# @Author : 司云中
# @File : signal.py
# @Software: Pycharm

from blinker import Namespace

user_signals = Namespace()  # 声明信号映射

# 创建信号对象
send_code_signal = user_signals.signal('send-code')                     # 发送验证码

update_session_user_signal = user_signals.signal('update-information')  # 更新session中的数据

generate_token_signal = user_signals.signal('generate_token')           # 生成token




