# -*- coding: utf-8 -*-
# @Time  : 2020/12/2 下午2:48
# @Author : 司云中
# @File : json.py
# @Software: Pycharm

from json import dumps

from flask import current_app, make_response
from flask_restful.utils import PY3


def output_json(data, code, headers=None):
    """
    Makes a Flask response with a JSON encoded body
    override this function to define the custom format of response
    """

    settings = current_app.config.get('RESTFUL_JSON', {})

    # If we're in debug mode, and the indent is not set, we set it to a
    # reasonable value here.  Note that this won't override any existing value
    # that was set.  We also set the "sort_keys" value.

    if 'message' not in data:
        data.update({'message':'If you have problems, please hesitate to contact me at 247179876@qq.com or blog: https://syzzjw.cn'})
    if current_app.debug:
        settings.setdefault('indent', 4)
        settings.setdefault('sort_keys', not PY3)

    # always end the json dumps with a new line
    # see https://github.com/mitsuhiko/flask/pull/1262
    dumped = dumps(data, **settings) + "\n"

    resp = make_response(dumped, code)
    resp.headers.extend(headers or {})
    return resp