#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/5/9 14:24
"""

projectName = "cgspiders"

logDirName = "logs"

confDirName = "conf"
baseCfgFileName = "base.json"

# =============base 配置=============

# base中server配置
baseServerFileKey = "server"
baseServerFileDef = "server.json"

# base中mongo的配置名
baseMongoFileKey = "mongo"
baseMongoFileDef = "mongo.json"


# 扫描间隔, 分钟
baseScanMinuteKey = "scanMinute"
baseScanMinuteDef = 1

# 线程池大小
baseThreadPoolNumKey = "threadNum"
baseThreadPoolNumDef = 20

# 进程池大小
baseProcessPoolNumKey = "processNum"
baseProcessPoolNumDef = 5

# =============server配置=============

serverIpKey = "ip"
serverIpDef = "127.0.0.1"

serverPortKey = "port"
serverPortDef = 8003

# =============mongo 配置=============
mongoHostKey = "host"
mongoHostDef = "127.0.0.1"

mongoPortKey = "port"
mongoPortDef = 27017

mongoDBKey = "db"
mongoDBDef = "self"

# =============spider配置=============

spiderConfDirName = "spiders"

spiderCookiesKey = "cookies"

spiderUserNameDef = "cg"
spiderUserCookieDef = ""
