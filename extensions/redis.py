# -*- coding: utf-8 -*-
# @Time  : 2020/12/3 上午9:10
# @Author : 司云中
# @File : redis.py
# @Software: Pycharm
import contextlib
import datetime

from redis import Redis


class BaseRedis:
    _instance = {}
    _redis_instances = {}

    def __init__(self, db, redis):
        self.db = db  # 选择配置中哪一种的数据库
        self.__redis = redis

    @classmethod
    def init_app(cls, app):
        return cls.load_config_redis(app)

    @classmethod
    def load_config_redis(cls, app):
        """
        加载配置中的缓存数据库
        单例模式，减小new实例的大量创建的次数，减少内存等资源的消耗（打开和关闭连接），共享同一个资源
        """
        if not cls._instance.setdefault(cls.__name__, None):
            db = app.config.get('REDIS_DB')

            assert 'default' in db, " 'default' config should be declared in CACHES attribute"

            for name, config in db.items():
                cls._redis_instances[name] = Redis(**config)
            cls._instance[cls.__name__] = cls(db, cls._redis_instances.get('default'))  # 默认配置default
        return cls._instance[cls.__name__]

    @property
    def redis(self):
        """default redis"""
        return self.__redis

    @redis.setter
    def redis(self, value):
        self.__redis = value

    def get_redis(self, redis_name):
        """从redis实例群中获取制定的redis_name"""
        return self._redis_instances[redis_name]

    @classmethod
    def redis_instance(cls, redis_name):
        """获取存放单例字典中的redis实例"""
        return cls._redis_instances[redis_name]

    @classmethod
    def redis_operation_instance(cls):
        """获取当前操作类(BaseRedis)的实例"""
        return cls._instance[cls.__name__]

    @staticmethod
    def record_ip(ip, redis_name='default'):
        """记录IP"""
        with manager_redis(redis_name) as redis:
            redis.hset(name='ip_record', key=ip, value=datetime.datetime.now().strftime('%Y-%m-%d'))

    @staticmethod
    def key(*args):
        """
        字符串拼接形成key
        :param args: 元祖依赖值
        :return: str
        """
        keywords = (str(value) if not isinstance(value, str) else value for value in args)
        return '-'.join(keywords)

    @staticmethod
    def check_code(key, value, redis_name='default'):
        """
        检查value是否和redis中key映射的value对应？
        :param redis_name: redis name in config
        :param key: key in key
        :param value: value from outside
        :return: bool
        """
        with manager_redis(redis_name) as redis:
            if redis is None:
                return False
            elif redis.exists(key):
                _value = redis.get(key).decode()
                return True if _value == value else False
            else:
                return False

    @staticmethod
    def save_code(key, code, time, redis_name='default'):
        """
        缓存验证码并存活 time（s）
        :param redis_name: redis name in config
        :param key: key of redis
        :param code: code from outside
        :param time: (second)
        :return: bool
        """

        with manager_redis(redis_name) as redis:
            if redis is None:
                return False
            redis.setex(key, time, code)  # 原子操作，设置键和存活时间

    @staticmethod
    def get_ttl(key, redis_name='default'):
        """
        获取某个键的剩余过期时间
        键永久：-1
        键不存在：-2
        :param redis_name: redis name in config
        :param key: key of redis
        :return: int
        """
        with manager_redis(redis_name) as redis:
            if redis is None:
                return False
            redis.ttl(key)

    @staticmethod
    def get_token_exp(identity, redis_name='default'):
        """
        :param redis_name: redis name in config
        :param identity:用户id
        获取token最终失效时间
        数据结构:hash
        """

        with manager_redis(redis_name) as redis:
            return redis.hget(identity, 'refresh_time').decode()

    @staticmethod
    def save_token_kwargs(redis_name, **kwargs):
        """
        存id号, token, 生成token起始时间,token最终过期时间
        每次检测请求token,看是否需要刷新自动获取

        数据结构:hash
        """

        _copy = kwargs.copy()
        with manager_redis(redis_name) as redis:
            redis.hset(_copy.pop('id'), mapping=_copy)



@contextlib.contextmanager
def manager_redis(redis_name=None, redis_class=BaseRedis):
    redis = None
    redis_name = redis_name or 'default'
    try:
        redis = redis_class.redis_instance(redis_name)
        yield redis                 # 如有异常,回退到此,抛出异常
    except Exception as e:
        # TODO: 自定义异常处理
        print(e)
    finally:
        redis.close()  # 其实可以不要,除非single client connection, 每条执行执行完都会调用conn.release()


@contextlib.contextmanager
def manager_redis_operation(redis_class=BaseRedis):
    try:
        instance = redis_class.redis_operation_instance()
        yield instance
    except Exception as e:
        # TODO: 自定义异常处理
        print(e)