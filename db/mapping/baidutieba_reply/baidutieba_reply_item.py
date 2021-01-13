#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/8/26 19:33
"""

from db.mapping.basemap_item import BaseMapItem


class BaiduTiebaReplyItem(BaseMapItem):
    # 标题
    title = None

    # 帖子 url
    pUrl = None

    # 视频url
    vSrc = None

    # 标签
    tag = None

    # 自己的上传脚本是否访问过
    effect = None

    # 发布这个帖子的玩家主页url
    playerHome = None

    # 发布这个帖子的玩家名字
    playerName = None

    # 来自谁的收藏
    userName = None

    def __iter__(self):
        yield 'spiderTs', self.spiderTs
        yield 'insertTs', self.insertTs
        yield 'updateTs', self.updateTs
        yield 'title', self.title
        yield 'pUrl', self.pUrl
        yield 'vSrc', self.vSrc
        yield 'tag', self.tag
        yield 'effect', self.effect
        yield 'playerHome', self.playerHome
        yield 'playerName', self.playerName
        yield 'userName', self.userName
