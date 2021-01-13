#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/5/1 2:04
"""

import string
import random


class RandomStr:

    total_char = None

    def __init__(self):
        self.total_char = string.ascii_letters
        self.total_char += string.digits

    def gen_str(self, num=11):
        """
        生成随机字符串
        :param num: 返回的字符串的个数, 默认为constants.lenValue
        :return:
        """
        s_ran = random.SystemRandom()
        res = str().join(s_ran.choice(self.total_char) for _ in range(num))
        return res


def equals(str1, str2):
    """
    不区分大小写判断字符串是否相等
    :param str1:
    :param str2:
    :return: true: 相等
    """
    return str1.lower() == str2.lower()


def lowers_first(str1):
    first = str1[:1].lower()
    end = str1[1:]
    return first + end


