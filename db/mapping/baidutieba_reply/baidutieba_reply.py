#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/8/26 19:33
"""

from db.mapping.basemap import BaseMap
from db.mapping.baidutieba_reply.baidutieba_reply_item import BaiduTiebaReplyItem


class BaiduTiebaReply(BaseMap):

    @staticmethod
    def is_instance(data):
        return isinstance(data, BaiduTiebaReplyItem)

    @staticmethod
    def build_item(data):
        item = BaiduTiebaReplyItem()
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