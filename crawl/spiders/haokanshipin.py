#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/6/8 15:12
"""
from crawl.spiders.base_spider import BaseSpider


class HaoKanShiPin(BaseSpider):

    _base_url = "https://haokan.baidu.com/"

    def __init__(self):
        super().__init__(self._base_url, True)

    def run(self):
        print("run")

