#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/6/5 10:38
"""
import os
from common import const
from util import com_util
from sanic.log import logger
from sanic.log import error_logger


class CfgData:

    # 基本配置
    _base = dict()
    # mongo配置
    _mongo = dict()
    # server配置
    _server = dict()

    def __init__(self):

        # 读取base.json内容到内存
        CfgData._base = read_cfg(const.baseCfgFileName)

        # mongo.json
        mongo_name = self._base.get(const.baseMongoFileKey)
        CfgData._mongo = read_cfg(mongo_name)

        # server.json
        server_name = self._base.get(const.baseServerFileKey)
        CfgData._server = read_cfg(server_name)

    @classmethod
    def get_base(cls):
        return cls._base

    @classmethod
    def get_mongo(cls):
        return cls._mongo

    @classmethod
    def get_server(cls):
        return cls._server


def check_init():
    exist = com_util.check_file_exist(get_conf_path())
    if not exist:
        # print("配置文件夹不存在, 将初始化")
        logger.log("配置文件夹不存在, 将初始化")
        init()

    # 读取配置到内存
    CfgData()


def read_cfg(file_name):
    file_path = get_conf_path() + os.sep + file_name
    return read_file(file_path)


def read_file(file_path):
    if not com_util.check_file_exist(file_path):
        return None
    try:
        return com_util.read_from_json(file_path)
    except BaseException as e:
        error_logger.error(e)
        return None


def get_conf_path():
    return os.getcwd() + os.sep + const.confDirName

# ============= 配置初始化 =============


def init():
    com_util.check_create_dir(get_conf_path())
    init_base()
    init_server()
    init_mongo()


def init_base():
    """
    初始化base.json配置文件内容
    """
    base = dict()
    base[const.baseServerFileKey] = const.baseServerFileDef
    base[const.baseMongoFileKey] = const.baseMongoFileDef
    base[const.baseScanMinuteKey] = const.baseScanMinuteDef
    base[const.baseThreadPoolNumKey] = const.baseThreadPoolNumDef
    base[const.baseProcessPoolNumKey] = const.baseProcessPoolNumDef

    base_path = get_conf_path() + os.sep + const.baseCfgFileName
    com_util.write_to_json(base, base_path)


def init_server():
    """
    初始化server.json内容
    """
    server = dict()
    server[const.serverIpKey] = const.serverIpDef
    server[const.serverPortKey] = const.serverPortDef
    server_path = get_conf_path() + os.sep + const.baseServerFileDef
    com_util.write_to_json(server, server_path)


def init_mongo():
    """
    初始化mongo.json内容
    """
    mongo = dict()
    mongo[const.mongoHostKey] = const.mongoHostDef
    mongo[const.mongoPortKey] = const.mongoPortDef
    mongo[const.mongoDBKey] = const.mongoDBDef

    mongo_path = os.path.join(get_conf_path(), const.baseMongoFileDef)
    com_util.write_to_json(mongo, mongo_path)



