#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/7/10 10:58
"""

from crawl.spiders import BaseSpider
from operate.schedulermgr import SchedulerMgr
from sanic.log import logger
from sanic.log import error_logger


class SpiderMgr:
    # 存放的spiders对象(本想将spider都做成单例, 但总觉得不大好)
    _spiders_ = list()

    @classmethod
    def start(cls):
        """
        启动所有spider, 继承了BaseSpider的将启动
        """
        spiders = BaseSpider.__subclasses__()
        for spider in spiders:
            item_spider = spider()
            item_spider.run()
            cls._spiders_.append(item_spider)

        # 增加数据落地执行
        SchedulerMgr.add_job_cron(cls.save2_db, day_of_week='*', hour='*', minute='*/6', second='0')

    @classmethod
    def stop(cls):
        """
        spider停止
        :return:
        """
        if not cls._spiders_:
            error_logger.error("未发现spider")
            return
        for item_spider in cls._spiders_:
            item_spider.stop()

    @classmethod
    def save2_db(cls):
        """
        保存数据
        :return:
        """
        if not cls._spiders_:
            return
        for item_spider in cls._spiders_:
            item_spider.save2_db_handle()
