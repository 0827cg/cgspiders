#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/6/5 17:54
"""
from db.mapping.basemap_item import BaseMapItem


class HaoKanShiPinItem(BaseMapItem):

    # 平台上的视频id
    vid = None

    # 标题
    title = None

    # 作者名字
    vAuthor = None

    # 已经观看的次数描述
    viewText = None

    # 已经观看的次数
    view = None

    # 封面url
    pic = None

    # 视频页面url
    pageUrl = None

    # 视频url
    vSrc = None

    # 发布时间
    pubTime = None

    # 视频时长
    durTime = None

    # 来自的平台
    platform = None
