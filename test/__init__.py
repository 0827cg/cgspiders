#!/usr/bin/python3 
"""
 Author: cg
 Date: 2020/7/10 17:58
"""

# from test.project_a import ProjectA
# from test.project_b import ProjectB
# from test.project_c import ProjectC

from test import project_a
from test import project_b
from test import project_c

import os
from util import com_util

# item_path = os.sep + "test"
# print(os.getcwd() + item_path)
# list_file = com_util.get_total_file(os.getcwd() + item_path, end_with=".py")
# for item in list_file:
#     print(item)

# list_file = list()
# list_file.append('project_a')
# list_file.append('project_b')
# list_file.append('project_c')
# for item in list_file:
#     from test import item


# 使用__all__的功能
# 如在无此__all__时候, 外界包导入ProjectB 其导入语句from test.project_b import ProjectB
# 那有此__all__后, 外界导入可以直接 from test import ProjectB
# 当然, 目前来说对我是没用的
__all__ = [
    # 'ProjectA',
    # 'ProjectB',
    # 'ProjectC'
]