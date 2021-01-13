#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/6/5 10:30
"""
from util.cfg_util import CfgData
from common import const
from util import time_util
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from sanic.log import logger
from sanic.log import error_logger


class SchedulerMgr:

    _scheduler = None

    def __init__(self, app, loop):
        pass

    @classmethod
    def init(cls, app, loop):
        executors = cls.gen_configure_executors()
        SchedulerMgr._scheduler = BackgroundScheduler(executors=executors, event_loop=loop)
        cls._scheduler.add_job(cls.time_to_reset, trigger='cron', day_of_week='*', hour='1', minute='30', second='30')
        cls._scheduler.start()

    @classmethod
    def add_job_run_one(cls, func, ts):
        """
        添加只执行一次的任务
        :param func: 函数
        :param ts: 执行的时间戳
        """
        run_date = time_util.format_time(ts)
        cls._scheduler.add_job(func, 'date', run_date=run_date)

    @classmethod
    def add_job_interval_seconds(cls, func, seconds=5):
        """
        添加按秒来循环执行的任务
        :param func: 函数
        :param seconds: 循环秒, 默认5秒
        """
        cls._scheduler.add_job(func, 'interval', seconds=seconds)

    @classmethod
    def add_job_interval_minute(cls, func, minutes=2):
        logger.info("添加定时模块: {}".format(func))
        cls._scheduler.add_job(func, 'interval', minutes=minutes)

    @classmethod
    def add_job_cron(cls, func, day_of_week, hour, minute, second):
        logger.info("添加cron定时模块: {}".format(func))
        cls._scheduler.add_job(func, trigger='cron', day_of_week=day_of_week, hour=hour, minute=minute, second=second)

    @classmethod
    def time_to_reset(cls):
        """
        重置任务
        """
        print("重置")

    @classmethod
    def stop(cls):
        cls._scheduler.shutdown(wait=False)

    @staticmethod
    def gen_configure_executors():
        thread_num = CfgData.get_base().get(const.baseThreadPoolNumKey)
        process_num = CfgData.get_base().get(const.baseProcessPoolNumKey)

        executors = {
            'default': ThreadPoolExecutor(thread_num),
            'processpool': ProcessPoolExecutor(process_num)
        }
        return executors
