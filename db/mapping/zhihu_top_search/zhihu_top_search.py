#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/7/16 17:18
"""

from db.mapping.basemap import BaseMap
from db.mapping.zhihu_top_search.zhihu_top_search_item import ZhiHuTopSearchItem


class ZhiHuTopSearch(BaseMap):

    @staticmethod
    def is_instance(data):
        return isinstance(data, ZhiHuTopSearchItem)

    @staticmethod
    def build_item(data):
        item = ZhiHuTopSearchItem()
        item.spiderTs = data['spiderTs']
        item.insertTs = data['insertTs']
        item.updateTs = data['updateTs']
        item.words = data['words']
        return item
