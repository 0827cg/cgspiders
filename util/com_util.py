#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/5/1 1:59
"""

import json
import os
import time
import datetime
import random
from zlib import crc32


def build_cookie(cookie_str):
    cookies = cookie_str.split("; ")
    cookie_dict = dict()
    for item in cookies:
        try:
            items = item.split("=")
        except BaseException as e:
            continue
        if len(items) != 2:
            continue

        cookie_dict[items[0]] = items[1]
    return cookie_dict


def size_convert(size):
    K, M, G = 1024, 1024 ** 2, 1024 ** 3
    if size >= G:
        return str(size / G) + 'G Bytes'
    elif size >= M:
        return str(size / M) + 'M Bytes'
    elif size >= K:
        return str(size / K) + 'K Bytes'
    else:
        return str(size) + 'Bytes'


def get_total_file(dir_path, end_with=".mp4"):
    """
    获取目录下的所有文件,
    :param dir_path: 目录路径
    :param end_with: 后缀, 默认为.mp4
    :return: list(各个文件的绝对路径)
    """
    res = list()
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            (name, extension) = os.path.splitext(file)
            if extension == end_with:
                file_path = os.path.join(root, file)
                res.append(file_path)
    return res


def get_file_path_name(file_path):
    """
    获取文件信息
    :param file_path: 绝对路径
    :return: 文件绝对路径, 文件名字(无后缀), 文件后缀
    """
    (path, full_name) = os.path.split(file_path)
    (name, extension) = os.path.splitext(full_name)
    return path, name, extension


def get_crc32_value_file(file_path):
    with open(file_path, 'rb') as f:
        return crc32(f.read())


def get_crc32_from_data(data):
    x = crc32(data)
    return format(x & 0xFFFFFFFF, '08x')


def get_crc32_value_data(data):
    return crc32(data)


def check_create_dir(dir_name):
    """
    describe: 检测文件夹是否存在, 若不存在则创建
    :param dir_name: 文件夹名
    :return:
    """
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def check_file_exist(file_path):
    return os.path.exists(file_path)


def create_params_json(params):
    """
    将字符串,dict转换成json格式
    @param params: 参数
    @return: json
    """
    return json.dumps(params, separators=(',', ':'), ensure_ascii=False)


def pretty_to_json(params_dict):
    """
    格式化dict成json 字符串
    @param params_dict:
    @return: json
    """
    return json.dumps(params_dict, indent=4, ensure_ascii=False)


def write_to_json(data, file_path):
    """
    数据写入到json文件中
    :param data: json/dict
    :param file_path: 输出的文件路径
    :return: true
    """
    if isinstance(data, dict):
        data = pretty_to_json(data)

    with open(file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(data)
    return True


def read_from_json(file_path):
    """
    读取json文件内容
    :param file_path: 需要读取的路径
    :return: dict
    """
    with open(file_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
    return json_data


def random_not_repeat(min_value, max_value, num):
    if max_value - min_value + 1 <= num:
        return None
    res = list()
    for i in range(num):
        test = random.randint(min_value, max_value)
        if test not in res:
            res.append(test)
        else:
            i -= 1
    return res


def random_from_arr(max_num, arr):
    if max_num >= len(arr):
        return arr
    return random.sample(arr, max_num)


def remove_video_json_file_after_publisher(json_path):
    json_exist = check_file_exist(json_path)
    if not json_exist:
        return

    json_data = read_from_json(json_path)
    if not json_data:
        return

    v_path = json_data['path']
    v_exist = check_file_exist(v_path)
    os.remove(json_path)
    if not v_exist:
        return
    os.remove(v_path)
