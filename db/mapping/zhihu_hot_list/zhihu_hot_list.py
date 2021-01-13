#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/7/17 13:55
"""

from db.mapping.basemap import BaseMap
from db.mapping.zhihu_hot_list.zhihu_hot_list_item import ZhiHuHotListItem


class ZhiHuHotList(BaseMap):

    @staticmethod
    def is_instance(data):
        return isinstance(data, ZhiHuHotListItem)

    @staticmethod
    def build_item(data):
        pass