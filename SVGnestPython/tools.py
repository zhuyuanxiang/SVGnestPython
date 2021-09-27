# -*- encoding: utf-8 -*-
"""
=================================================
@path   : SVGnestPython -> tools.py
@IDE    : PyCharm
@Author : zYx.Tom, 526614962@qq.com
@Date   : 2021-09-27 16:41
@Version: v0.1
@License: (C)Copyright 2020-2021, zYx.Tom
@Reference:
@Desc   :
==================================================
"""
import os
import time
from datetime import datetime

from config import PROJECT_NAME


def func_time(func):
    def wrapper(*args, **kw):
        start_time = time.time()  # ----->函数运行前时间
        func(*args, **kw)
        end_time = time.time()  # ----->函数运行后时间
        cost_time = end_time - start_time  # ---->运行函数消耗时间
        print("函数%s()消耗时间为%s" % (func.__name__, cost_time))

    return wrapper  # ---->装饰器其实是对闭包的一个应用


def getProjectPath():
    file_path = os.getcwd()
    project_path = file_path[:file_path.index(PROJECT_NAME)] + PROJECT_NAME
    return project_path


@func_time
def main(name):
    print(f'Hi, {name}', datetime.now())
    print("Project Path=", getProjectPath())
    pass


if __name__ == "__main__":
    __author__ = 'zYx.Tom'
    main(__author__)
