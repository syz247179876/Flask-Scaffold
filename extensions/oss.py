# -*- coding: utf-8 -*-
# @Time  : 2020/12/13 下午6:02
# @Author : 司云中
# @File : oss.py
# @Software: Pycharm
import os

import oss2
from application.utils.exception import UploadFileOSSError, DeleteFileOSSError


class OSS(object):
    """操作OSS对象存储,上传文件"""

    def __init__(self, app=None, config=None):
        self.config = config
        self.bucket = None
        self.auth = None
        self.base_url = None
        self.app = app

        if self.app:
            self.init_app(app)

    def init_app(self, app):
        """Initialize the app with ALiYun-OSS service"""
        setattr(self, 'app', app)

        # 从配置中导入
        self.set_auth()
        self.set_bucket()
        self.set_base_url()

        # you may use the following attribute in other way, while better not
        _oss = {
            'auth': self.auth,
            'bucket': self.bucket,
            'base_url': self.base_url
        }
        setattr(app, 'OSS', _oss)

    def set_auth(self):
        """设置认证信息"""
        access_key_id = self.app.config.get('ACCESS_KEY_ID')
        access_key_secret = self.app.config.get('ACCESS_KEY_SECRET')
        self.auth = oss2.Auth(access_key_id, access_key_secret)

    def set_bucket(self):
        """设置oss图床"""

        oss_bucket_name = self.app.config.get('OSS_BUCKET_NAME')
        endpoint = self.app.config.get('OSS_ENDPOINT')
        self.bucket = oss2.Bucket(self.auth, endpoint, oss_bucket_name)

    def set_base_url(self):
        """
        获取返回的基本路由,用于提供用户访问数据地址
        或者是存数数据库的字段值
        """
        self.base_url = self.app.config.get('OSS_BASE_URL')

    def upload_file(self, file, folder):
        """
        上传目标文件
        :param file werkzeug.datastructures.FileStorage 对象
        :param folder 文件夹
        :return 用户访问的路径 / 上传异常
        """
        filename = self.filename(file)
        related_path = self.file_related_path(filename, folder)
        outer_net = self.outer_net(related_path)
        is_existed = self.bucket.object_exists(related_path)

        if is_existed:  # 文件已经存在
            raise UploadFileOSSError()
        result = self.bucket.put_object(related_path, file)
        if result.status == 200:
            return outer_net
        raise UploadFileOSSError()

    def delete_file(self, file, folder=None):
        """
        从oss的bucket中删除一个文件
        :param file: 文件
        :param folder:
        :return: True / raise
        """
        folder = folder if folder else ''
        filename = self.filename(file)
        related_path = self.file_related_path(filename, folder)
        result = self.bucket.delete_object(related_path)
        if result.status == 200:
            return True
        raise DeleteFileOSSError()

    def outer_net(self, file_related_path):
        """
        生成外网访问路径
        :param file_related_path:  文件相对bucket的路径
        :return: absolute path of file
        """
        return os.path.join(self.base_url, file_related_path)

    @staticmethod
    def file_related_path(filename, folder=None):
        """
        生成文件相对路径
        :param filename: 文件名
        :param folder: 文件夹
        :return:
        """
        folder = folder if folder else ''
        return os.path.join(folder, filename.replace('\\', '/'))

    @staticmethod
    def filename(file):
        """
        获取文件名
        :param file:FileStorage文件对象
        :return: 文件名
        """
        return file.filename

oss = OSS()
