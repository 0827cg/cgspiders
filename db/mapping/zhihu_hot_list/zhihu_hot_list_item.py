#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/7/17 13:55
"""

from db.mapping.basemap_item import BaseMapItem


class ZhiHuHotListItem(BaseMapItem):

    # id
    id = None

    # 标题
    title = None

    # 问题创建时间
    created = None

    # 摘录
    exerpt = None

    # 回答个数
    answerCount = None

    # 热度描述
    detailText = None
