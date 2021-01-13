#!/usr/bin/python3 
"""

 这份key的与爬取到的数据命名一样
 Author: cg
 Date: 2020/7/11 14:49
"""

from db.mapping.basemap_item import BaseMapItem


class JiangxiRiverItem(BaseMapItem):

    upCodes = None

    # 超警戒的个数   overTopWrzSize
    warnStatNum = None

    # 超过警戒的站点信息   overTopWrz
    warnStatInfo = list()

    # 描述  summarize
    desc = None

    # 全省站点信息, list,  rows
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
