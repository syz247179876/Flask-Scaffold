# -*- coding: utf-8 -*-
# @Time  : 2020/12/1 下午11:48
# @Author : 司云中
# @File : exception.py
# @Software: Pycharm

import json

import werkzeug as werkzeug

HTTP_100_CONTINUE = 100
HTTP_101_SWITCHING_PROTOCOLS = 101
HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_202_ACCEPTED = 202
HTTP_203_NON_AUTHORITATIVE_INFORMATION = 203
HTTP_204_NO_CONTENT = 204
HTTP_205_RESET_CONTENT = 205
HTTP_206_PARTIAL_CONTENT = 206
HTTP_207_MULTI_STATUS = 207
HTTP_208_ALREADY_REPORTED = 208
HTTP_226_IM_USED = 226
HTTP_300_MULTIPLE_CHOICES = 300
HTTP_301_MOVED_PERMANENTLY = 301
HTTP_302_FOUND = 302
HTTP_303_SEE_OTHER = 303
HTTP_304_NOT_MODIFIED = 304
HTTP_305_USE_PROXY = 305
HTTP_306_RESERVED = 306
HTTP_307_TEMPORARY_REDIRECT = 307
HTTP_308_PERMANENT_REDIRECT = 308
HTTP_400_BAD_REQUEST = 400
HTTP_401_UNAUTHORIZED = 401
HTTP_402_PAYMENT_REQUIRED = 402
HTTP_403_FORBIDDEN = 403
HTTP_404_NOT_FOUND = 404
HTTP_405_METHOD_NOT_ALLOWED = 405
HTTP_406_NOT_ACCEPTABLE = 406
HTTP_407_PROXY_AUTHENTICATION_REQUIRED = 407
HTTP_408_REQUEST_TIMEOUT = 408
HTTP_409_CONFLICT = 409
HTTP_410_GONE = 410
HTTP_411_LENGTH_REQUIRED = 411
HTTP_412_PRECONDITION_FAILED = 412
HTTP_413_REQUEST_ENTITY_TOO_LARGE = 413
HTTP_414_REQUEST_URI_TOO_LONG = 414
HTTP_415_UNSUPPORTED_MEDIA_TYPE = 415
HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE = 416
HTTP_417_EXPECTATION_FAILED = 417
HTTP_418_IM_A_TEAPOT = 418
HTTP_422_UNPROCESSABLE_ENTITY = 422
HTTP_423_LOCKED = 423
HTTP_424_FAILED_DEPENDENCY = 424
HTTP_426_UPGRADE_REQUIRED = 426
HTTP_428_PRECONDITION_REQUIRED = 428
HTTP_429_TOO_MANY_REQUESTS = 429
HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE = 431
HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS = 451
HTTP_500_INTERNAL_SERVER_ERROR = 500
HTTP_501_NOT_IMPLEMENTED = 501
HTTP_502_BAD_GATEWAY = 502
HTTP_503_SERVICE_UNAVAILABLE = 503
HTTP_504_GATEWAY_TIMEOUT = 504
HTTP_505_HTTP_VERSION_NOT_SUPPORTED = 505
HTTP_506_VARIANT_ALSO_NEGOTIATES = 506
HTTP_507_INSUFFICIENT_STORAGE = 507
HTTP_508_LOOP_DETECTED = 508
HTTP_509_BANDWIDTH_LIMIT_EXCEEDED = 509
HTTP_510_NOT_EXTENDED = 510
HTTP_511_NETWORK_AUTHENTICATION_REQUIRED = 511

# 通用自定义异常码
UNIVERSAL_ERROR = 9999
# QQ认证异常码
QQ_AUTHENTICATION_ERROR = 1001
# 微博认证异常码
WeiBo_AUTHENTICATION_ERROR = 1002
# 手机注册异常
PHONE_REGISTER_ERROR = 1003
# 手机号不存在
PHONE_NOT_EXIST = 1004
# 手机号存在
PHONE_HAS_EXISTED = 1005
# 验证码错误
CODE_VALIDATE_FAIL = 1006
# 未认证
AUTHENTICATION_ERROR = 1007
# 丢失密码
PASSWORD_MISSING_ERROR = 1008
# 丢失验证码
CODE_MISSING_ERROR = 1009
# 修改个人信息失败
MODIFY_INFORMATION_ERROR = 1010
# 用户信息存在异常
SESSION_INFORMATION_ERROR = 1011
# 服务器开小车去了
SERVER_ERROR = 1013
# 密码不正确
PASSWORD_ERROR = 1014
# 验证码错误
CODE_ERROR = 1015
# 服务端Token最终失效
SERVER_TOKEN_EXPIRE = 1016
# TOKEN校验失败
TOKEN_DECODE_ERROR = 1017
# MONGODB校验失败
MONGODB_VALIDATION_ERROR = 1018
# 用户已经存在
USER_EXISTED_ERROR = 1019
# 用户积分不足
INTEGRAL_INSUFFICIENT_ERROR = 1020
# 通用校验异常错误
DATA_UNIVERSAL_EXCEPTION = 1021
# API权限校验异常
API_PERMISSION_EXCEPTION = 1022


class ApiException(werkzeug.exceptions.HTTPException):
    """
    1.重写__init__()方法,设定传入值
      code: HTTP常规状态码
      error_code:自定义错误异常码,范围1000-9999
      msg:提示消息,没有则为''
      data:响应数据,没有则为''
    2.重写get_body()方法,重设响应体
    3.重写get_headers()方法,重设响应头部
    """

    def __init__(self, code=None, error_code=None, msg=None, data=None):
        self.code = code or HTTP_500_INTERNAL_SERVER_ERROR
        self.error_code = error_code or UNIVERSAL_ERROR
        self.msg = msg or self.description
        self.data = data
        super().__init__(self.msg, None)  # response is None

    def get_body(self, environ=None):
        """生成body"""
        body = dict(
            code=self.code,
            error_code=self.error_code,
            msg=self.msg,
            data=self.data
        )
        return json.dumps(body, sort_keys=False, ensure_ascii=False)  # json格式化,以中文显示

    def get_headers(self, environ=None):
        """返回application/json的响应格式"""
        return [("Content-Type", "application/json")]


class ServerError(ApiException):
    """通用服务错误"""
    code = HTTP_500_INTERNAL_SERVER_ERROR
    error_code = UNIVERSAL_ERROR
    description = 'Server Error'

    def __init__(self):
        super().__init__(self.code, self.error_code, self.description)


class QQServiceUnavailable(ApiException):
    """QQ认证异常"""
    code = HTTP_400_BAD_REQUEST
    error_code = QQ_AUTHENTICATION_ERROR
    description = 'QQ Authentication error'

    def __init__(self):
        super().__init__(self.code, self.error_code, self.description)


class WbServiceUnavailable(ApiException):
    """微博认证异常"""
    code = HTTP_400_BAD_REQUEST
    error_code = WeiBo_AUTHENTICATION_ERROR
    description = 'WeiBo Authentication error'

    def __init__(self):
        super().__init__(self.code, self.error_code, self.description)


class RegisterExistedException(ApiException):
    """手机注册已存在"""
    code = HTTP_400_BAD_REQUEST
    error_code = PHONE_HAS_EXISTED
    description = 'Mobile phone number exist'

    def __init__(self):
        super().__init__(self.code, self.error_code, self.description)


class LoginNotExistException(ApiException):
    """手机号登录不存在"""
    code = HTTP_400_BAD_REQUEST
    error_code = PHONE_NOT_EXIST
    description = 'Mobile phone number does not exist'

    def __init__(self):
        super().__init__(self.code, self.error_code, self.description)


class VerificationCodeException(ApiException):
    """验证码错误"""

    code = HTTP_400_BAD_REQUEST
    error_code = CODE_VALIDATE_FAIL
    description = 'Verification code is validated error'

    def __init__(self):
        super().__init__(self.code, self.error_code, self.description)


class AuthenticationError(ApiException):
    """认证异常"""
    code = HTTP_401_UNAUTHORIZED
    error_code = AUTHENTICATION_ERROR
    description = 'User Authentication error'

    def __init__(self):
        super().__init__(self.code, self.error_code, self.description)


class PasswordMissingError(ApiException):
    """缺失密码异常"""
    code = HTTP_400_BAD_REQUEST
    error_code = PASSWORD_MISSING_ERROR
    description = 'Password must be required'

    def __init__(self):
        super().__init__(self.code, self.error_code, self.description)


class CodeMissingError(ApiException):
    """缺失验证码异常"""
    code = HTTP_400_BAD_REQUEST
    error_code = CODE_MISSING_ERROR
    description = 'Code must be required'

    def __init__(self):
        super().__init__(self.code, self.error_code, self.description)


class ModifyInformationError(ApiException):
    """修改信息异常"""
    code = HTTP_500_INTERNAL_SERVER_ERROR
    error_code = MODIFY_INFORMATION_ERROR
    description = 'modify information error'

    def __init__(self):
        super().__init__(self.code, self.error_code, self.description)


class SessionUserInformationException(ApiException):
    """Session 存储异常"""
    code = HTTP_500_INTERNAL_SERVER_ERROR
    error_code = SESSION_INFORMATION_ERROR
    description = 'User information seem to exist exception'

    def __init__(self):
        super().__init__(self.code, self.error_code, self.description)


class ServerErrors(ApiException):
    """服务器错误"""
    code = HTTP_500_INTERNAL_SERVER_ERROR
    error_code = SERVER_ERROR
    description = 'Server may be leave a little time'

    def __init__(self):
        super().__init__(self.code, self.error_code, self.description)

class PasswordError(ApiException):
    """密码或手机号异常"""
    code = HTTP_400_BAD_REQUEST
    error_code = PASSWORD_ERROR
    description = 'password or phone error'

    def __init__(self):
        super().__init__(self.code, self.error_code, self.description)

class CodeError(ApiException):
    """验证码异常"""
    code = HTTP_400_BAD_REQUEST
    error_code = CODE_ERROR
    description = 'code error'

    def __init__(self):
        super().__init__(self.code, self.error_code, self.description)

class ServerTokenExpire(ApiException):
    """
    服务端Token过期,
    意味着用户必须强制重定向到登录页
    """
    code = HTTP_401_UNAUTHORIZED
    error_code = SERVER_TOKEN_EXPIRE
    description = 'server token is expired up to the uttermost'

    def __init__(self):
        super().__init__(self.code, self.error_code, self.description)

class TokenDecodeError(ApiException):
    """
    Token校验错误
    """
    code = HTTP_403_FORBIDDEN
    error_code = TOKEN_DECODE_ERROR
    description = 'The token you supply is error, please check it'

    def __init__(self):
        super().__init__(self.code, self.error_code, self.description)

class MongodbValidationError(ApiException):
    """Mongodb校验错误"""

    code = HTTP_400_BAD_REQUEST
    error_code = MONGODB_VALIDATION_ERROR
    description = 'Mongodb Validation Error'

    def __init__(self):
        super().__init__(self.code, self.error_code, self.description)

class UserExistedError(ApiException):
    """用户已经存在"""

    code = HTTP_500_INTERNAL_SERVER_ERROR
    error_code = USER_EXISTED_ERROR
    description = 'User has existed'

    def __init__(self):
        super().__init__(self.code, self.error_code, self.description)

class IntegralInsufficientError(ApiException):
    """积分值不够错误"""

    code = HTTP_500_INTERNAL_SERVER_ERROR
    error_code = INTEGRAL_INSUFFICIENT_ERROR
    description = 'The integral of user is insufficient'

    def __init__(self):
        super().__init__(self.code, self.error_code, self.description)

class DataUniversalException(ApiException):
    """通用数据校验异常"""

    code = HTTP_400_BAD_REQUEST
    error_code = DATA_UNIVERSAL_EXCEPTION
    description = 'Data verification is abnormal'

    def __init__(self):
        super().__init__(self.code, self.error_code, self.description)

class ApiPermissionError(ApiException):
    """Api权限异常"""

    code = HTTP_403_FORBIDDEN
    error_code = API_PERMISSION_EXCEPTION
    description = 'API Permission verification failed'

    def __init__(self):
        super().__init__(self.code, self.error_code, self.description)

class ImproperlyConfigured(Exception):
    """Flask is somehow improperly configured"""
    pass
