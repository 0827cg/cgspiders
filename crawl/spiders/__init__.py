#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/7/15 19:54
"""

from crawl.spiders.base_spider import BaseSpider
# from crawl.spiders import haokanshipin
from crawl.spiders import yangtze_river
from crawl.spiders import haokan_hotwords
from crawl.spiders import jiangxi_river
from crawl.spiders import jiangxi_reservoir
from crawl.spiders import zhihu_top_search
# from crawl.spiders import baidutieba_collection
from crawl.spiders import baidutieba_reply

__all__ = [
    'BaseSpider'
]
