#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/7/10 16:03
"""

from db.mapping.basemap_item import BaseMapItem


class HaokanHotWordsItem(BaseMapItem):

    # 数据
    hotWords = list()

    def __iter__(self):
        yield 'spiderTs', self.spiderTs
        yield 'insertTs', self.insertTs
        yield 'updateTs', self.updateTs
        yield 'hotWords', self.hotWords
