#!/usr/bin/python3 
"""
 江西省水利厅
 水库信息
 Author: cg
 Date: 2020/7/11 15:57
"""

from db.mapping.basemap_item import BaseMapItem


class JiangxiReservoirItem(BaseMapItem):

    upCodes = None

    # 超警戒的个数   overTopFLZSize
    warnStatNum = None

    # 超过警戒的水库站点信息   overTopFLZ
    warnStatInfo = list()

    # 描述  summarize
    desc = None

    # 提供的所有水库信息, list,  rows
    totalStatInfo = list()

    def __iter__(self):
        yield 'spiderTs', self.spiderTs
        yield 'insertTs', self.insertTs
        yield 'updateTs', self.updateTs
        yield 'upCodes', self.upCodes
        yield 'warnStatNum', self.warnStatNum
        yield 'warnStatInfo', self.warnStatInfo
        yield 'desc', self.desc
        yield 'totalStatInfo', self.totalStatInfo
