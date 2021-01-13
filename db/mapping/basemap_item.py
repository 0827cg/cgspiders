#!/usr/bin/python3 
"""
 表的数据格式
 Author: cg
 Date: 2020/6/5 17:07
"""


class BaseMapItem:

    # 爬取时间
    spiderTs = None

    # 本条数据创建的时间戳
    insertTs = None

    # 更新的时间戳
    updateTs = None

    def __iter__(self):
        yield 'spiderTs', self.spiderTs
        yield 'insertTs', self.insertTs
        yield 'updateTs', self.updateTs
