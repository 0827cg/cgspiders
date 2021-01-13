#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/7/10 9:11
"""

from db.mapping.basemap_item import BaseMapItem
from db.mapping.yangtze_river.river_place_info import RiverPlaceInfo


class YangtzeRiverItem(BaseMapItem):

    # 信息对应的时间
    ts = None

    # 各站点信息 list(dict river_place_info)
    placeInfos = list()

    def __iter__(self):
        # super().__iter__()

        yield 'spiderTs', self.spiderTs
        yield 'insertTs', self.insertTs
        yield 'updateTs', self.updateTs
        yield 'ts', self.ts
        yield 'placeInfos', self.placeInfos
