#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/6/5 10:27
"""
from sanic import Sanic
from sanic.response import json
from util import log_cfg
from common import const
from sanic.log import logger
from sanic.log import error_logger
from db.mongo import MongoDB
from operate.schedulermgr import SchedulerMgr
from util import cfg_util
from util.cfg_util import CfgData
from crawl.spidermgr import SpiderMgr


class FrameMgr:

    frame = None

    def __init__(self):
        self.frame = Sanic(name=const.projectName, log_config=log_cfg.get_config())
        self.boot()

    def boot(self):
        cfg_util.check_init()

        MongoDB()

        self.frame.register_listener(self.register_http_route, 'before_server_start')
        self.frame.register_listener(self.boot_module, 'after_server_start')
        self.frame.register_listener(self.stop, 'before_server_stop')

    @staticmethod
    def boot_module(app, loop):
        """
        after_server_start 初始化并启动别的模块
        :param app:
        :param loop:
        """

        SchedulerMgr.init(app, loop)

        SpiderMgr.start()

    def register_http_route(self, app, loop):
        logger.info("注册http路由")
        self.frame.add_route(handler=self.index_handler, uri="/", methods=["GET"])

    @staticmethod
    async def index_handler(request):
        return json({"hello": "world"})

    def start(self):
        host = CfgData.get_server().get(const.serverIpKey)
        port = CfgData.get_server().get(const.serverPortKey)
        if not host or not port:
            error_logger.error("server 配置不存在")
        self.frame.run(host=host, port=port)

    @staticmethod
    def stop(app, loop):
        """
        before_server_stop
        :param app:
        :param loop:
        """
        SchedulerMgr.stop()

        SpiderMgr.stop()
        logger.info("stop")
