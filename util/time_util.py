#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/5/14 15:59
"""
import time
import datetime


def getcurrent_ts_millis():
    return int(time.time() * 1000)


def getcurrent_ts():
    return int(time.time())


def getcurrent_time_date():
    return format_time(getcurrent_ts())


def format_time(timestamp):
    """
    格式化时间戳,
    :param timestamp:
    :return: str %Y-%m-%d %H:%M:%S
    """
    if len(str(timestamp)) >= 13:
        timestamp = timestamp / 1000
    time_loc = time.localtime(int(timestamp))
    return time.strftime("%Y-%m-%d %H:%M:%S", time_loc)


def get_format_date_now(fmt="%Y-%m-%d-%H"):
    """
    按格式获取当前日期,
    :param fmt: 默认%Y-%m-%d-%H
    :return: str
    """
    ts = int(time.time())
    tm_local = time.localtime(ts)
    return time.strftime(fmt, tm_local)


def get_format_today():
    """
    获取当天日期 yyyy-mm-dd
    :return: str
    """
    return str(datetime.date.today())


def get_day_of_week(is_num=True):
    t = time.localtime()
    if is_num:
        return time.strftime("%w", t)
    return time.strftime("%A", t)


def gen_time_tuple_today(hour, minute):
    """
    根据小时, 分钟, 来获取当天的time.struct_time, 秒未定义
    :param hour: 需要定义的小时数
    :param minute: 需要定义的分钟数
    :return: time.struct_time
    """
    str_time = time.localtime()
    tuple_time = tuple(str_time)
    new_list = list()
    index = 0
    for i in tuple_time:
        if index == 3:
            # hour
            new_list.append(hour)
        elif index == 4:
            new_list.append(minute)
        else:
            new_list.append(i)
        index += 1
    new_tuple = tuple(new_list)
    return time.struct_time(new_tuple)


def get_split_time_min(time_item):
    """
    将"17:15"这种小时分钟时间分割
    :param time_item:
    :return: hour, minute
    """
    tm_list = time_item.split(":")
    if len(tm_list) != 2:
        return None, None
    return int(tm_list[0]), int(tm_list[1])


def get_ts_today_hour_min(hour, minute):
    str_time = gen_time_tuple_today(hour, minute)
    return get_ts_by_struct_time(str_time)


def get_ts_by_struct_time(str_time):
    """
    根据time.struct_time 来获取该时间戳, 秒
    :param str_time: time.struct_time对象
    :return: 时间戳, 秒级别
    """
    if isinstance(str_time, time.struct_time):
        return time.mktime(str_time)
    return 0
