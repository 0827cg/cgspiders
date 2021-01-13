#!/usr/bin/python3 
"""

 百度贴吧收藏页面的数据, 目前只准备实现自己账户的

 Author: cg
 Date: 2020/7/28 19:36
"""

import requests
import time
import json
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from crawl.spiders.base_spider import BaseSpider
from util import time_util
from util import com_util
from util import time_util
from common import const
from operate.schedulermgr import SchedulerMgr
from db.mapping.baidutieba_collection.baidutieba_collection import BaiduTiebaCollection
from db.mapping.baidutieba_collection.baidutieba_collection_item import BaiduTiebaCollectionItem
from sanic.log import logger
from sanic.log import error_logger


class BaiduTiebaCollectionSpider(BaseSpider):
    _base_url = "http://tieba.baidu.com/i/i/storethread"

    # db中的帖子信息, 新增的也将放到这里, 用以对比是否重复. key: url item, value: 帖子信息(非视频帖子也存)
    _t_data_ = dict()

    # key: spider ts, value: 新增的收餐帖子信息, 数据落地从此
    _data_ = dict()

    # 配置存放
    _cfg_data = dict()

    _handle_to_save = False

    def __init__(self):
        super().__init__(self._base_url, False)
        self.check_generate_config_schema()
        self._cfg_data = self.read_config()
        self.boot_db_data()

    def run(self):
        # 每6分钟执行一次
        # SchedulerMgr.add_job_cron(self.request_begin, day_of_week='*', hour='*', minute='*/5', second='*')
        SchedulerMgr.add_job_interval_minute(self.request_begin, 6)

    def request(self):
        if not self._cfg_data:
            error_logger.error("配置为空")
            return
        if const.spiderCookiesKey not in self._cfg_data:
            error_logger.error("cookie未配置")
            return

        list_account = self._cfg_data.get(const.spiderCookiesKey)
        for account in list_account:
            account_name = account.get('accountName')
            cookie = account.get('cookie')
            dict_cookie = com_util.build_cookie(cookie)
            if not dict_cookie:
                error_logger.error("未获取到cookie, accountName: {}".format(account_name))
                continue

            res = requests.get(self.base_url, headers=self.headers, cookies=dict_cookie)
            if res.status_code != 200:
                error_logger.error("请求失败, accountName: {}".format(account_name))
                continue
            res_text = res.text
            self.analysis_card_list(res_text, dict_cookie, account_name)

            # 手动落地
            self.save2_db()

    def analysis_card_list(self, str_page, dict_cookie, account_name):
        """
        分析收藏页面, 并爬取收藏帖子信息
        :param str_page: 收藏页面内容
        :param dict_cookie: cookie
        :param account_name 贴吧账户名字
        :return:
        """
        beautiful_data = BeautifulSoup(str_page, "html.parser")
        result_set = beautiful_data.find_all("li", class_="feed_item clearfix feed_favts j_feed_favts")

        if result_set is None:
            error_logger.error("收藏页面分析出错,未找到list, url: {}".format(self._base_url))
            return
        for i in result_set:
            card_tag = i.find("a", class_="itb_thread")
            if card_tag is None:
                error_logger.error("未找到帖子url等信息")
                break

            url_item = card_tag.get('href')
            title = card_tag.get('title')
            if url_item is None or title is None:
                error_logger.error("帖子url: {}或者title: {}为空".format(url_item, title))
                continue

            card_url = self.get_base_url() + url_item

            # 是否已经存在
            if card_url in self._t_data_:
                continue

            item_data = BaiduTiebaCollectionItem()
            # 内存中保存一份, 非视频帖子也存下, 用以下次不用继续请求
            self._t_data_[card_url] = item_data

            video_url = self.request_card_page(card_url, dict_cookie)
            if video_url is None:
                continue

            item_data.spiderTs = time_util.getcurrent_ts_millis()
            item_data.title = title
            item_data.pUrl = card_url
            item_data.vSrc = video_url
            item_data.tag = list()
            item_data.effect = False
            item_data.userName = account_name

            # 发布者信息
            card_user_tag = i.find("a", class_="itb_user")
            if card_user_tag is not None:
                item_data.playerHome = self.get_base_url() + card_user_tag.get('href')
                item_data.playerName = card_user_tag.get_text()

            # 存放做为新数据, 等待插入
            self._data_[item_data.spiderTs] = item_data

    def request_card_page(self, url, dict_cookie):
        """
        请求帖子页面, 爬取视频url
        :param url: 帖子url
        :param dict_cookie: cookie
        :return: 视频url, None: 未发现视频/url
        """
        res = requests.get(url, headers=self.headers, cookies=dict_cookie)
        if res.status_code != 200:
            error_logger.error("帖子请求出错, url: {}".format(url))
            return None
        video_url = self.analysis_card_info(res.text)
        if video_url is None:
            error_logger.error("未获取到video url, 帖子url: {}".format(url))
            return None
        return video_url

    @staticmethod
    def analysis_card_info(str_card_page):
        """
        帖子页面 分析 解析到视频的url, 并返回
        :param str_card_page:
        :return: url, None: 未获取到
        """
        if str_card_page is None:
            return None
        soup = BeautifulSoup(str_card_page, "html.parser")
        tag = soup.find("embed", {'allowfullscreen': "true"})
        if tag is None:
            error_logger.error("未找到embed视频标签")
            return None
        return tag.get('data-video')

    def get_base_url(self):
        parse_result = urlparse(self._base_url)
        return parse_result.scheme + "://" + parse_result.netloc

    def boot_db_data(self):
        """
        将db表里的数据读取到内存中
        :return: None
        """
        data_list = BaiduTiebaCollection.query_all()
        if not data_list:
            return
        for data in data_list:
            url = data.pUrl
            if url is None:
                continue
            self._t_data_[url] = data

    def get_collection(self):
        return BaiduTiebaCollection
