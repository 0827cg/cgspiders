#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/7/10 16:02
"""

from db.mapping.basemap import BaseMap
from db.mapping.haokanhotwords.haokan_hotwords_item import HaokanHotWordsItem


class HaokanHotWords(BaseMap):

    @staticmethod
    def is_instance(data):
        return isinstance(data, HaokanHotWordsItem)

    @staticmethod
    def build_item(data):
        item = HaokanHotWordsItem()
        item.spiderTs = data['spiderTs']
        item.insertTs = data['insertTs']
        item.updateTs = data['updateTs']
        item.hotWords = data['hotWords']
        return item
