#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/7/10 17:59
"""



class ProjectA:

    _base_url = "https://www.baidu.com/"

    def run(self):
        print("run---Project A: " + self._base_url)

    @classmethod
    def run_class(cls):
        print("run--project A " + cls._base_url)

    def show(self):
        collection = self.get_collection()
        print(collection.get_name())

    @staticmethod
    def get_collection():
        raise NotImplementedError("Must implement method: get_collection")

    def get_name(self):
        print(self.__class__.__name__)
