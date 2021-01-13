#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/6/8 15:19
"""

import os
import urllib.request
from common.headers import headers
from sanic.log import logger
from sanic.log import error_logger
from common import const
from common.schema.account_info import AccountInfo
from util import string_util
from util import cfg_util
from util import com_util


class BaseSpider:

    # 待请求的url
    base_url = None

    # key: spider ts, value: db表中的每一条数据:
    _data_ = dict()

    # 被父类主动落地
    _handle_to_save = True

    def __init__(self, url, init):
        """
        spider初始化
        :param url: 访问url
        :param init: 是否初始化client
        """
        self.headers = headers
        self.base_url = url
        if init:
            self.client = urllib.request.Request(self.base_url, headers=self.headers)

    def run(self):
        """
        子类实现, 设定定时执行方式
        """
        raise NotImplementedError("Must implement method: run")

    def request_begin(self):
        logger.info("执行请求: " + self.base_url)
        self.request()

    def request(self):
        """
        子类实现 执行请求
        """
        raise NotImplementedError("Must implement method: request")

    def stop(self):
        """
        退出操作, 保存数据
        """
        self.save2_db()

    def save2_db_handle(self):
        if self._handle_to_save:
            self.save2_db()

    def save2_db(self):
        """
        保存数据, 仅保存self._data_中的数据
        :return:
        """
        if not self._data_:
            return False

        collection = self.get_collection()
        collection_name = collection.get_name()

        for key, value in self._data_.items():
            suc = collection.insert_data(value)
            if not suc:
                error_logger.error(collection_name + "数据落地出错")
                return False
        logger.info(collection_name + "数据已落地")
        self._data_.clear()
        return True

    def get_collection(self):
        """
        子类实现, 返回保存子类数据的mapping 类
        """
        raise NotImplementedError("Must implement method: get_collection")

    def get_spider_name(self):
        """
        获取spider的名字
        :return:
        """
        class_name = self.__class__.__name__
        str_lowers = string_util.lowers_first(class_name)
        return str_lowers.split("Spider")[0]

    @staticmethod
    def get_conf_path():
        """
        获取存放配置文件的路径
        :return:
        """
        dir_path = cfg_util.get_conf_path() + os.sep + const.spiderConfDirName
        com_util.check_create_dir(dir_path)
        return dir_path

    def get_conf_file_path(self):
        """
        获取配置文件的文件路径
        :return:
        """
        return self.get_conf_path() + os.sep + self._get_config_name()

    def check_generate_config_schema(self):
        exist = com_util.check_file_exist(self.get_conf_file_path())
        if not exist:
            self._generate_config_schema()

    def read_config(self):
        """
        读取配置返回
        :param dict_data:
        :return:
        """
        return cfg_util.read_file(self.get_conf_file_path())

    def _generate_config_schema(self):
        """
        生成基本配置文件
        """
        data = dict()

        account_infos = list()
        account = AccountInfo()
        account.accountName = const.spiderUserNameDef
        account.cookie = const.spiderUserCookieDef
        account_infos.append(account.__dict__)
        data[const.spiderCookiesKey] = account_infos

        com_util.write_to_json(data, self.get_conf_file_path())

    def _get_config_name(self):
        return self.get_spider_name() + ".json"
