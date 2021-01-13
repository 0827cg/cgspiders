#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/7/16 17:18
"""

from db.mapping.basemap_item import BaseMapItem


class ZhiHuTopSearchItem(BaseMapItem):

    # 热搜信息
    words = list()

    def __iter__(self):
        yield 'spiderTs', self.spiderTs
        yield 'insertTs', self.insertTs
        yield 'updateTs', self.updateTs
        yield 'words', self.words
