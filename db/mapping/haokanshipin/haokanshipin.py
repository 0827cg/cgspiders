#!/usr/bin/python3 
"""

 好看视频这个平台上面的数据格式

 目前的想法是, 每个用户的主页的视频数据都存放再同一张表中, 因为存再风格类型不同的情况
 同时也方便更新
 这样的情况下, 就不会出现haoKanShiPing这张表(每个用户的表继承这张表就可以了)

 但是现在又想放到同一张表中,

 Author: cg
 Date: 2020/6/5 17:53
"""
from db.mapping.basemap import BaseMap
from db.mapping.haokanshipin.haokanshipin_item import HaoKanShiPinItem


class HaoKanShiPin(BaseMap):

    @staticmethod
    def is_instance(data):
        return isinstance(data, HaoKanShiPinItem)

    @staticmethod
    def build_item(data):
        item = HaoKanShiPinItem()
        item.vid = data["vid"]
        item.title = data["title"]
        item.vAuthor = data["vAuthor"]
        item.viewText = data["viewText"]
        item.view = data["view"]
        item.pic = data["pic"]
        item.pageUrl = data["pageUrl"]
        item.vSrc = data["vSrc"]
        item.pubTime = data["pubTime"]
        item.durTime = data["durTime"]
        item.createTime = data["createTime"]
        item.createTimeDate = data["createTimeDate"]
        return item
