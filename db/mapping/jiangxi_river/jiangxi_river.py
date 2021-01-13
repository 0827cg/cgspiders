#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/7/11 14:49
"""


from db.mapping.basemap import BaseMap
from db.mapping.jiangxi_river.jiangxi_river_item import JiangxiRiverItem


class JiangxiRiver(BaseMap):

    @staticmethod
    def is_instance(data):
        return isinstance(data, JiangxiRiverItem)

    @staticmethod
    def build_item(data):
        item = JiangxiRiverItem()
        item.spiderTs = data['spiderTs']
        item.insertTs = data['insertTs']
        item.updateTs = data['updateTs']
        item.upCodes = data['upCodes']
        item.warnStatNum = data['warnStatNum']
        item.warnStatInfo = data['warnStatInfo']
        item.desc = data['desc']
        item.totalStatInfo = data['totalStatInfo']
        return item