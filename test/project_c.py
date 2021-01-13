#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/7/10 18:01
"""
from db.mapping.jiangxi_reservoir.jiangxi_reservoir import JiangxiReservoir
from test.project_a import ProjectA


class ProjectC(ProjectA):

    _base_url = "https://www.baidu.com/cc"

    def run(self):
        print("run --project C" + self._base_url)

    @classmethod
    def run_class(cls):
        print("run--project C " + cls._base_url)

    @staticmethod
    def get_collection():
        return JiangxiReservoir
