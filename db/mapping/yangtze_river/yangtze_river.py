#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/7/10 9:10
"""

from db.mapping.basemap import BaseMap
from db.mapping.yangtze_river.yangtze_river_item import YangtzeRiverItem


class YangtzeRiver(BaseMap):

    @staticmethod
    def is_instance(data):
        return isinstance(data, YangtzeRiverItem)

    @staticmethod
    def build_item(data):
        item = YangtzeRiverItem()
        item.ts = data['ts']
        item.placeInfos = data['placeInfos']
        item.spiderTs = data['spiderTs']
        item.insertTs = data['insertTs']
        item.updateTs = data['updateTs']
        return item

