#!/usr/bin/python3 
"""
 表映射 mongodb 的 ORM , 自己实现的最基本的关系, 其余的表需要从此继承, 可更方便
 Author: cg
 Date: 2020/6/5 14:31
"""
import random
import pymongo
from db.mongo import MongoDB
from util import string_util
from util import com_util
from util import time_util
from sanic.log import logger
from sanic.log import error_logger


class BaseMap:
    _collection = None

    @classmethod
    def insert_data(cls, data):
        """
        插入数据到数据库
        :param data: PublishedItem对象
        :return: None: 错误
        """
        if not cls.is_instance(data):
            return False
        cur_ts = time_util.getcurrent_ts_millis()
        data.insertTs = cur_ts
        data.updateTs = cur_ts
        try:
            result = cls.get_col().insert_one(dict(data))
            return result.inserted_id is not None
        except Exception as e:
            error_logger.error(e)
            return False

    @classmethod
    def update_data(cls, data):
        if not cls.is_instance(data):
            return
        data.updateTs = time_util.getcurrent_ts()
        cls.get_col().insert_one(data.__dict__)

    @classmethod
    def query_all(cls):
        """
        获取所有数据
        :return:
        """
        col = cls.get_col()
        res = list()
        for item in col.find():
            res.append(cls.build_item(item))
        return res

    @classmethod
    def query_one(cls):
        data = cls.get_col().find_one()
        print(data)
        return cls.build_item(data)

    @classmethod
    def query_one_by_field(cls, **kwargs):
        """
        随机抽取一条
        :param kwargs:  {field: value}
        :return:
        """
        data = cls.get_col().find_one(**kwargs)
        return cls.build_item(data)

    @classmethod
    def query_num_sort_by_field(cls, field, num=1, sort=pymongo.DESCENDING):
        """
        根据字段field的值int来排序, 并获取数据
        :param field 字段(int )
        :param num: 获取的数据条数
        :param sort: 排序方式, 默认降序, 从大到小
        :return: list(子类自己的对象)
        """
        col = cls.get_col()
        res = list()
        list_data = col.find().sort(field, sort).limit(num)
        for item in list_data:
            res.append(cls.build_item(item))
        return res

    @classmethod
    def query_num_contrast_by_view(cls, field, value, num=1, con_type=1):
        """
        根据field字段来抽取运算符内比较value后 的 num条数据
        :param field: 字段名字(int )
        :param value: 比较的值
        :param num: 数量(将会降序排序, 数量为其顺序)
        :param con_type: 1: 大于, 2: 大于等于,
        :return: list(子类自己的对象)
        """
        col = cls.get_col()
        res = list()
        list_data = None
        if con_type == 1:
            # 大于
            list_data = col.find({field: {"$gt": value}}).limit(num)
        elif con_type == 2:
            # 大于等于
            list_data = col.find({field: {"$gte": value}}).limit(num)
        elif con_type == 3:
            # 小于
            list_data = col.find({field: {"$lt": value}}).limit(num)
        elif con_type == 4:
            # 小于等于
            list_data = col.find({field: {"$lte": value}}).limit(num)
        for item in list_data:
            res.append(cls.build_item(item))
        return res

    @classmethod
    def query_bye_view_more_then_one(cls, field, value):
        """
        随机取出一条数据, 依据field这个字段的值, 只需要比value大的数据即可
        :param field: 查找的字段
        :param value: 对比的数值
        :return: 子类自己的对象
        """
        list_data = cls.get_col().find({field: {"$gte": value}})
        if not list_data:
            return None
        ran_index = random.randint(0, list_data.count() - 1)
        return cls.build_item(list_data[ran_index])

    @classmethod
    def query_bye_view_more_then(cls, field, value, num):
        """
        随机抽取一定数量的数据, 根据view字段的数值, 去除的数据其view值大于等于value
        :param field: 对比的字段
        :param value: 对比的数值
        :param num: 数量
        :return: list(子类自己的对象)
        """
        list_data = cls.get_col().find({field: {"$gte": value}})
        if not list_data:
            return None
        list_index = com_util.random_not_repeat(0, list_data.count() - 1, num)
        res = list()
        for i in list_index:
            res.append(cls.build_item(list_data[i]))
        return res

    @classmethod
    def check_exists(cls, **kwargs):
        """
        检测是否存在, {field: value}
        :param kwargs:
        :return: boolean True: 存在
        """
        data = cls.get_col().find_one(**kwargs)
        if data:
            return True
        return False

    @staticmethod
    def is_instance(data):
        """
        检测是否是该对象, 子类实现
        :param data: 外部传入的数据(数据库存放的数据)
        """
        raise NotImplementedError("Must implement method: is_instance")

    @staticmethod
    def build_item(data):
        """
        构造数据对象, 由子类自己构造所需的对象数据, 子类必须继承
        :param data: 外部传入的数据(数据库存放的数据)
        """
        raise NotImplementedError("Must implement method: build_item")

    @classmethod
    def get_col(cls):
        if cls._collection:
            return cls._collection
        col_name = cls.get_name()
        db = MongoDB.get_db()
        cls._collection = db[col_name]
        return cls._collection

    @classmethod
    def get_name(cls):
        class_name = cls.__name__
        return string_util.lowers_first(class_name)
