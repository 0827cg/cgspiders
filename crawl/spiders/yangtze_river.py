#!/usr/bin/python3 
"""
 获取长江水文局公布的一些地方的水位信息
 Author: cg
 Date: 2020/7/9 16:55
"""

import re
import json
import urllib.request
from crawl.spiders.base_spider import BaseSpider
from operate.schedulermgr import SchedulerMgr
from db.mapping.yangtze_river.yangtze_river import YangtzeRiver
from db.mapping.yangtze_river.yangtze_river_item import YangtzeRiverItem
from db.mapping.yangtze_river.river_place_info import RiverPlaceInfo
from util import time_util
from sanic.log import logger
from sanic.log import error_logger


class YangtzeRiverSpider(BaseSpider):
    # 需要请求的url
    _base_url = "http://www.cjh.com.cn/sqindex.html"

    # 请求得到的数据key: spiderTs  value: YangtzeRiverItem
    _data_ = dict()

    def __init__(self):
        super().__init__(self._base_url, True)

    def run(self):
        # 每小时的01分, 30分30秒执行
        SchedulerMgr.add_job_cron(self.request_begin, day_of_week='*', hour='*', minute='01,31', second='30')

    def request(self):
        """
        执行请求
        """
        res = urllib.request.urlopen(self.client)
        str_html = res.read().decode("utf-8")
        res.close()
        suc = self.operate_data(str_html)
        if not suc:
            error_logger.error("请求处理出错 " + self._base_url)

    def operate_data(self, data):
        """
        处理请求得到的数据
        :param data: 请求得到的数据, string
        :return:
        """
        # 正则表达规则, 为找到 字符串'var sssq = '那一行
        pattern = re.compile(r"^.*var sssq =.*$", re.M)
        line = pattern.search(data).group(0)
        line_list = line.split(' = ')
        if len(line_list) != 2:
            error_logger.error("爬取到的数据异常" + str(line_list))
            return False

        # 获取var sssq = 的值, 并去除最后的';'(爬取到的内容, 行尾貌似 为'; ', 多了各空格, 所以为-2)
        value = line_list[1][0:-2]
        logger.info("爬取到的数据: " + value)
        value_json = json.loads(value)
        # 当前时间戳 作为爬取时间
        cur_ts = time_util.getcurrent_ts_millis()
        space_infos = list()
        ts = None

        for item in value_json:
            item_space_info = self.operate_space_item(item)
            space_infos.append(dict(item_space_info))
            if ts is None:
                ts = item['tm']

        # 得到YangtzeRiverItem对象数据, 存入内存中
        data_item = self.operate_data_item(cur_ts, ts, space_infos)
        self._data_[cur_ts] = data_item
        return True

    @staticmethod
    def operate_data_item(cur_ts, ts, space_infos):
        """
        构造生成一条数据, YangtzeRiverItem
        :param cur_ts: 当前时间
        :param ts: 各地信息对应的时间戳
        :param space_infos: 各地信息
        :return: YangtzeRiverItem对象
        """
        data_item = YangtzeRiverItem()
        data_item.ts = ts
        data_item.placeInfos = space_infos
        data_item.spiderTs = cur_ts
        return data_item

    @staticmethod
    def operate_space_item(item_data):
        """
        在一条数据中, 构造出单个地方的数据
        :param item_data:
        :return: RiverPlaceInfo对象
        """
        item = RiverPlaceInfo()
        item.riverName = item_data['rvnm']
        item.spaceName = item_data['stnm']
        item.spaceCode = item_data['stcd']
        item.enterSpeed = item_data['q']
        item.level = item_data['z']
        if item_data['wptn'] == 4:
            item.rise = False
        else:
            item.rise = True
        item.ts = item_data['tm']
        item.outSpeed = item_data['oq']
        return item

    def get_collection(self):
        return YangtzeRiver
