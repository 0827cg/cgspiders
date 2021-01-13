#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/7/28 19:45
"""

from db.mapping.basemap import BaseMap
from db.mapping.baidutieba_collection.baidutieba_collection_item import BaiduTiebaCollectionItem


class BaiduTiebaCollection(BaseMap):

    @staticmethod
    def is_instance(data):
        return isinstance(data, BaiduTiebaCollectionItem)

    @staticmethod
    def build_item(data):
        item = BaiduTiebaCollectionItem()
        item.spiderTs = data['spiderTs']
        item.insertTs = data['insertTs']
        item.updateTs = data['updateTs']
        item.title = data['title']
        item.pUrl = data['pUrl']
        item.vSrc = data['vSrc']
        item.effect = data['effect']
        item.tag = data['tag']
        item.playerHome = data['playerHome']
        item.playerName = data['playerName']
        item.userName = data['userName']
        return item
