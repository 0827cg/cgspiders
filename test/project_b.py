#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/7/10 18:00
"""

from db.mapping.haokanhotwords.haokan_hotwords import HaokanHotWords
from test.project_a import ProjectA


class ProjectB(ProjectA):

    _base_url = "https://www.baidu.com/bb"

    def run(self):

        print("run--project B" + self._base_url)

    @classmethod
    def run_class(cls):
        print("run--project B " + cls._base_url)

    @staticmethod
    def get_collection():
        return HaokanHotWords
