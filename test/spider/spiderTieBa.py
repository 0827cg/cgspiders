#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/8/8 10:27
"""

import urllib.request
import requests
from bs4 import BeautifulSoup
from common.headers import headers
from util import com_util
from util import file_util



url = "http://tieba.baidu.com/i/i/storethread"

strCookie = "BAIDUID=2E09BFD8C5A7B071AB32F873BE669B9B:FG=1; BIDUPSID=C0C119689AA633AA2E1518107F96F833; PSTM=1588814713; TIEBA_USERTYPE=14d764bc6a533bb13562395b; TIEBAUID=99184f06374b83cb232b636c; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1595491981; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1595492112; BDUSS=XdPSk9KdERGOFdSUjQ3UDdjRHFaUjJEUmJiRHZYTDZEfmRpdlFIMFp6WEgwMEJmSVFBQUFBJCQAAAAAAAAAAAEAAAAeXa49WFNZtO25~QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMdGGV~HRhlfT; STOKEN=5fbbd3775de6b7d52f058f53ef8747a4bb42c8a11ac6d500d1c9e7461b8955f5; wise_device=0; bdshare_firstime=1595492076136; st_data=ce9614ed142f124ed302150991bfcf7e93fa8d511c6022acfed1d7b52210c8c90e7f3dca90fcff8b0abb0cde169e759f1d03321f0fb4d114ad89afcbccb0272d4b7996478fd728acf3516072a8d3a831f2304de5be5eda176dd460ece3728fa890ddb2508bef286a03f38c3e2d79c0ad3354b2c7611458cba89b7f3612a659b0; st_key_id=17; st_sign=d444f645"


def test():

    # cookie_dict = com_util.build_cookie(strCookie)
    # req_data = requests.get(url=url, headers=headers, cookies=cookie_dict)
    # if req_data.status_code == 200:
    #     print("请求成功")
    #
    # str_res = req_data.text

    str_res = file_util.read_file("D:\\desktop\\desktop-io\\test\\test\\replay-page.html")
    get_video_url(str_res)


    # str_res = file_util.read_file("D:\\desktop\\desktop-io\\test\\test\\list.html")
    # # print(str_res)
    #
    # beautiful_data = BeautifulSoup(str_res, "html.parser")
    # result_set = beautiful_data.find_all("li", class_="feed_item clearfix feed_favts j_feed_favts")
    # for i in result_set:
    #
    #     card_tag = i.find("a", class_="itb_thread")
    #     card_user_tag = i.find("a", class_="itb_user")
    #
    #     if card_tag is not None:
    #         url_item = card_tag.get('href')
    #         title = card_tag.get('title')
    #
    #         print("url: " + url_item + " title: " + title)
    #
    #     if card_user_tag is not None:
    #         url_user_item = card_user_tag.get('href')
    #         user_name = card_user_tag.get_text()
    #
    #         print("url_user_item: " + url_user_item + " user_name: " + user_name)


def get_video_url(video_page_data):
    soup = BeautifulSoup(video_page_data, "html.parser")
    result_set = soup.find_all("div", class_="b_right_up")
    if result_set is None:
        print("not found")
        return

    if len(result_set) <= 0:
        print("no")
        return
    for i in result_set:

        a_tags = i.find_all("a")
        if a_tags is None:
            return
        tag_arr = a_tags[1].get_text()
        tie_url = a_tags[3].get("href")
        title = a_tags[3].get_text()
        print("tag_arr: {}, tie_url: {}, title: {}".format(tag_arr, tie_url, title))

        #==============

        reply_tag = i.find("a", class_="for_reply_context")
        if reply_tag is None:
            break

        reply_str = reply_tag.get_text()
        if reply_str.find("-") == -1:
            break

        # 标签, 约定使用"-"作为分隔符
        reply_list = reply_str.split("-")
        arr_len = len(reply_list)
        if arr_len > 5 or arr_len <= 0:
            break

        card_tag = i.find("a", class_="thread_title")
        if card_tag is None:
            print("未找到帖子url等信息")
            break

        url_item = card_tag.get('href')
        title = card_tag.get_text()
        print("url_item: {}, title: {}".format(url_item, title))

        card_user_tag = i.find_all("a")
        print(len(card_user_tag))
        if card_user_tag is not None:
            playerHome = card_user_tag[5].get('href')
            playerName = card_user_tag[5].get_text()
            p_name = playerName[0:playerName.find("的个人主页")]
            print("playerHome: {}, playerName: {}".format(playerHome, p_name))


test()