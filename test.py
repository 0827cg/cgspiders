#!/usr/bin/python3
"""
 Author: cg
 Date: 2020/6/5 11:24
"""

from test.project_a import ProjectA
from test.spider import spiderTieBa
from urllib.parse import urlparse


def test_children_class():

    projectA = ProjectA()
    projectA.get_name()


def spider_str():
    # str_text = "BaiduTiebaCollectionSpider"
    # str_text = "BaiduTiebaCollection"
    # arr_list = str_text.split("Spider")
    # print(arr_list)

    # 爬取测试
    spiderTieBa.test()

def test_url():
    url = "http://tieba.baidu.com/i/i/storethread"
    parse_result = urlparse(url)
    print(parse_result)
    print(parse_result.scheme)
    print(parse_result.netloc)


test_url()