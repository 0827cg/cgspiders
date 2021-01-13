#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/7/11 15:57
"""

from db.mapping.basemap import BaseMap
from db.mapping.jiangxi_reservoir.jiangxi_reservoir_item import JiangxiReservoirItem


class JiangxiReservoir(BaseMap):

    @staticmethod
    def is_instance(data):
        return isinstance(data, JiangxiReservoirItem)

    @staticmethod
    def build_item(data):
        item = JiangxiReservoirItem()
        item.spiderTs = data['spiderTs']
        item.insertTs = data['insertTs']
        item.updateTs = data['updateTs']
        item.upCodes = data['upCodes']
        item.warnStatNum = data['warnStatNum']
        item.warnStatInfo = data['warnStatInfo']
        item.desc = data['desc']
        item.totalStatInfo = data['totalStatInfo']
        return item