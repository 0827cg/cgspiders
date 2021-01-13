#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/5/10 11:10
"""

import pymongo
from common import const
from util.cfg_util import CfgData
from sanic.log import logger
from sanic.log import error_logger


class MongoDB:

    _client = None
    _db = None

    def __init__(self):

        if MongoDB._client or MongoDB._db:
            return
        mongo_dict = CfgData.get_mongo()
        mongo_host = mongo_dict.get(const.mongoHostKey)
        mongo_port = mongo_dict.get(const.mongoPortKey)
        mongo_db = mongo_dict.get(const.mongoDBKey)
        MongoDB._client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
        MongoDB._db = self._client[mongo_db]

    @classmethod
    def get_client(cls):
        return cls._client

    @classmethod
    def get_db(cls):
        return cls._db
