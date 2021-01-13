#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/5/8 17:50
"""

import sys
import os
from common import const
from util.com_util import check_create_dir

dir_name = const.logDirName
com_dir_name = "common"
err_dir_name = "error"

config = {
    'version': 1,
    'loggers': {
        'sanic.root': {
            "level": "INFO",
            "handlers": ['console', 'com_file'],
            # 'propagate': True
        },
        'sanic.error': {
            'level': 'ERROR',
            'handlers': ['console', 'err_file'],
            # 'propagate': True
        },
        'sanic.access': {
            # 既有 console Handler，还有 file Handler
            'level': 'INFO',
            'handlers': ['console', 'com_file'],
            # 'propagate': True
        }
        # 其他的 Logger
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'general',
            "stream": sys.stdout,
        },
        'com_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': dir_name + os.sep + com_dir_name + os.sep + 'common.log',
            'level': 'INFO',
            'encoding': 'utf-8',
            'formatter': 'general',
            'when': 'midnight',
            'backupCount': 30
        },
        'err_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': dir_name + os.sep + err_dir_name + os.sep + 'error.log',
            'level': 'ERROR',
            'encoding': 'utf-8',
            'formatter': 'general',
            'when': 'midnight',
            'backupCount': 30
        },
        # 其他的 handler
    },
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
        'general': {
            'format': '%(asctime)s-%(name)s-%(filename)s[%(funcName)s:%(lineno)d]-%(levelname)s : %(message)s'
        },
        'careful': {
            'format': '%(asctime)s-%(name)s-%(process)d-%(thread)d-%(threadName)s-%(pathname)s-%(module)s[%(funcName)s:%(lineno)d]-%(levelname)s : %(message)s'
        }
    }
}


def get_config():
    global dir_name, com_dir_name, err_dir_name
    check_create_dir(dir_name + os.sep + com_dir_name)
    check_create_dir(dir_name + os.sep + err_dir_name)
    return config

