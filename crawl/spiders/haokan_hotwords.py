#!/usr/bin/python3 
"""
 好看视频的今日热词

 Author: cg
 Date: 2020/7/10 15:50
"""

import urllib.request
import json
from crawl.spiders.base_spider import BaseSpider
from util import time_util
from operate.schedulermgr import SchedulerMgr
from db.mapping.haokanhotwords.haokan_hotwords import HaokanHotWords
from db.mapping.haokanhotwords.haokan_hotwords_item import HaokanHotWordsItem
from sanic.log import logger
from sanic.log import error_logger


class HaokanHotWordsSpider(BaseSpider):

    # 需要请求的url
    _base_url = "https://haokan.baidu.com/videoui/api/hotwords"

    # key: spider ts, value:
    _data_ = dict()

    def __init__(self):
        super().__init__(self._base_url, True)

    def run(self):
        # 8点，17点, 的00分钟30秒执行一次
        SchedulerMgr.add_job_cron(self.request_begin, day_of_week='*', hour='8, 17', minute='00', second='30')

    def request(self):
        res = urllib.request.urlopen(self.client)
        res_str = res.read().decode("utf-8")
        res.close()
        res_dict = json.loads(res_str)
        logger.info("请求得到数据: " + str(res_dict))
        suc = self.operate_data(res_dict)
        if not suc:
            logger.error("请求处理出错 " + self._base_url)

    def operate_data(self, res_dict):
        if 'data' not in res_dict:
            logger.error("返回结果中不包含'data'")
            return False

        if 'response' not in res_dict['data']:
            logger.error("返回结果data中不包含'response'")
            return False

        if 'hotwords' not in res_dict['data']['response']:
            logger.error("返回结果data.response中不包含'hotwords', 或许更换了")
            return False

        dict_data = res_dict['data']['response']['hotwords']
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
        item = HaokanHotWordsItem()
        item.spiderTs = cur_ts
        item.hotWords = dict_data
        return item

    def get_collection(self):
        return HaokanHotWords
