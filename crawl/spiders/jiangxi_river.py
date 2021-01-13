#!/usr/bin/python3 
"""
 爬取江西水位局 公开的江河水位信息
 url: http://slt.jiangxi.gov.cn/col/col28224/index.html

 Author: cg
 Date: 2020/7/11 14:43
"""

import json
import urllib.request
from crawl.spiders.base_spider import BaseSpider
from operate.schedulermgr import SchedulerMgr
from db.mapping.jiangxi_river.jiangxi_river import JiangxiRiver
from db.mapping.jiangxi_river.jiangxi_river_item import JiangxiRiverItem
from db.mapping.jiangxi_river.jiangxi_river_item_place import JiangxiRiverItemPlace
from util import time_util
from sanic.log import logger
from sanic.log import error_logger


class JiangxiRiverSpider(BaseSpider):

    # 接口地址
    _base_url = "http://111.75.205.67:7080/syq/rivermap/riverMapHandler"

    # key: spider ts, value: 每次爬取到的数据, 封装在JiangxiRiverItem中
    _data_ = dict()

    def __init__(self):
        super().__init__(self._base_url, True)

    def run(self):
        # 每小时的05, 35分钟30秒执行一次
        SchedulerMgr.add_job_cron(self.request_begin, day_of_week='*', hour='*', minute='05,35', second='30')

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
        if 'data' not in res_dict:
            logger.error("返回结果中不包含'data'")
            return False
        dict_data = res_dict['data']
        cur_ts = time_util.getcurrent_ts_millis()
        data_item = self.operate_item_data(cur_ts, dict_data)
        self._data_[cur_ts] = data_item
        return True

    def operate_item_data(self, cur_ts, dict_data):
        item = JiangxiRiverItem()
        item.spiderTs = cur_ts
        item.upCodes = dict_data['upCodes']
        item.warnStatNum = dict_data['overTopWrzSize']
        item.warnStatInfo = self.operate_item_space(dict_data['overTopWrz'])
        item.desc = dict_data['summarize']
        item.totalStatInfo = self.operate_item_space(dict_data['rows'])
        return item

    def operate_item_space(self, warn_list):
        res = list()
        for item in warn_list:
            data = self.build_space_info(item)
            res.append(data.__dict__)
        return res

    @staticmethod
    def build_space_info(dict_info):
        item_data = JiangxiRiverItemPlace()
        item_data.hTM = dict_info['hTM']
        item_data.wptn = dict_info['wptn']
        item_data.county = dict_info['county']
        item_data.maxLevelTime = dict_info['obhtztm']
        item_data.maxLevel = dict_info['obhtz']
        item_data.enterSpeed = dict_info['q']
        item_data.exceedLevel = dict_info['cwrz']
        item_data.stcd = dict_info['stcd']
        item_data.stnm = dict_info['stnm']
        item_data.tm = dict_info['tm']
        item_data.style = dict_info['style']
        item_data.level = dict_info['z']
        item_data.belongRiveName = dict_info['bsnm']
        item_data.warnLevel = dict_info['wrz']
        return item_data

    def get_collection(self):
        return JiangxiRiver
