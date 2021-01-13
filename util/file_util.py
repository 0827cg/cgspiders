#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/7/9 14:38
"""

import os
import time


def read_file(file_path, encode='utf-8', byte_num=1000):
    """
    读取普通文件内容并返回,默认每次只读取1000字节
    :param file_path: 需要读取的文件存放路径
    :param encode: 编码字符串
    :param byte_num: 每次读取的字节数, 默认1000
    :return: str 返回一个字符串类型, 为文件内容
    """
    if not os.path.exists(file_path):
        raise FileExistsError(file_path + "文件不存在")

    res = str()
    with open(file_path, 'r', encoding=encode) as file:
        while file.readable():
            item = file.read(byte_num)
            if item is None or item == '':
                break
            res += item
    return res


def read_file_line(file_path, encode='utf-8', line_num=1):
    """
    读取普通文件内容并返回, 一行一行读取
    :param file_path: 需要读取的文件存放路径
    :param encode: 编码字符串
    :param line_num: 每次读取的行数
    :return: str 内容
    """

    if not os.path.exists(file_path):
        raise FileExistsError(file_path + "文件不存在")

    res = str()
    with open(file_path, 'r', encoding=encode) as file:
        while file.readable():
            item = file.readline(line_num)
            if item is None or item == '':
                break
            res += item
    return res


def read_last_line_small(file_path):
    """
    读取文件的最后一行, 给小的文件使用
    code write in 2018-07-05

    review and change in 2020-07-09 15:03

    :param file_path:
    :return: str
    """
    # 读取文件的最后一行
    # 给小的文件使用
    # add in 2018-07-05

    with open(file_path, 'rb') as file:
        for strLine in file.readlines():
            pass
    return strLine.decode()


def read_last_line_large(file_path):
    """
    读取文件的最后一行  给大文件使用

    code write add in 2018-07-05

    review and change in 2020-07-09 15:05

    :param file_path:
    :return:
    """
    with open(file_path, 'rb') as file:
        file.seek(-2, os.SEEK_END)

        while file.read(1) != b'\n':
            file.seek(-2, os.SEEK_CUR)

        return file.readline().decode()


def tail_file(file_path):
    """
    实现的功能类似tail -f命令读取内容

    add in 2018-08-03

    review and change in 2020-07-09 15:09

    返回迭代器

    :param file_path:
    """
    with open(file_path, 'rb') as fileObj:
        pos = fileObj.seek(0, os.SEEK_END)
        print(pos)

        try:

            while True:
                time.sleep(0.02)
                res = fileObj.readline()
                if not res:
                    continue
                else:
                    yield res.decode('utf-8').strip('\n')
        except KeyboardInterrupt:
            pass


def write_file(file_path, content, encode='utf-8', add=True):
    """
    写入内容到指定文件,
    :param file_path:
    :param content:
    :param encode: 编码
    :param add: 是否清空追加, true 清空
    """
    if add:
        with open(file_path, 'w', encoding=encode) as file:
            file.write(content)
    else:
        with open(file_path, 'a', encoding=encode) as file:
            file.write("\n" + content)
