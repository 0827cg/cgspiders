#!/usr/bin/python3 
"""
 知乎热搜榜, 点击顶部搜索框后出现的面板内容
 Author: cg
 Date: 2020/7/16 17:14
"""

import urllib.request
import json
from crawl.spiders.base_spider import BaseSpider
from util import time_util
from operate.schedulermgr import SchedulerMgr
from db.mapping.zhihu_top_search.zhihu_top_search import ZhiHuTopSearch
from db.mapping.zhihu_top_search.zhihu_top_search_item import ZhiHuTopSearchItem
from sanic.log import logger
from sanic.log import error_logger


class ZhiHuTopSearchSpider(BaseSpider):
    _base_url = "https://www.zhihu.com/api/v4/search/top_search"

    # key: spiderTs ,value: ZhiHuTopSearchItem
    _data_ = dict()

    def __init__(self):
        super().__init__(self._base_url, True)

    def run(self):
        # 每小时的20分钟30秒执行一次
        SchedulerMgr.add_job_cron(self.request_begin, day_of_week='*', hour='*', minute='20', second='30')

    def request(self):
        res = urllib.request.urlopen(self.client)
        res_str = res.read().decode("utf-8")
        res.close()
        res_dict = json.loads(res_str)
        logger.info("请求得到数据: " + str(res_dict))
        suc = self.operate_data(res_dict)
        if not suc:
            error_logger.error("请求处理出错 " + self._base_url)

    def operate_data(self, res_dict):
        if 'top_search' not in res_dict:
            logger.error("返回结果中不包含'top_search'")
            return False

        if 'words' not in res_dict['top_search']:
            logger.error("返回结果top_search中不包含'words'")
            return False

        dict_data = res_dict['top_search']['words']
        cur_ts = time_util.getcurrent_ts_millis()
        item_data = self.operate_item_data(cur_ts, dict_data)
        self._data_[cur_ts] = item_data
        return True

    @staticmethod
    def operate_item_data(cur_ts, dict_data):
        """
        操作一组数据
        :param cur_ts:
        :param dict_data:
        :return:
        """
        item = ZhiHuTopSearchItem()
        item.spiderTs = cur_ts
        item.words = dict_data
        return item

    def get_collection(self):
        return ZhiHuTopSearch
