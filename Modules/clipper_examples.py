# -*- encoding: utf-8 -*-
"""
=================================================
@path   : SVGnestPython -> clipper_examples.py
@IDE    : PyCharm
@Author : zYx.Tom, 526614962@qq.com
@Date   : 2021-09-27 17:17
@Version: v0.1
@License: (C)Copyright 2020-2021, zYx.Tom
@Reference:
@Desc   :
==================================================
"""
from datetime import datetime

import pyclipper


def two_polygons_intersection(clip, subject):
    # 主体(subject)和裁剪(clip)的多边形
    # Difference（相剪）时使用 subject 消除 clip 的部分
    # 其他 boolean 操作，两个没有区别
    pc = pyclipper.Pyclipper()
    pc.AddPath(clip, pyclipper.PT_CLIP, True)
    pc.AddPath(subject, pyclipper.PT_SUBJECT, True)
    # pc.AddPaths(subject, pyclipper.PT_SUBJECT, True)
    solution = pc.Execute(pyclipper.CT_INTERSECTION, pyclipper.PFT_EVENODD)
    return solution


def main(name):
    print(f'Hi, {name}', datetime.now())


    pass


if __name__ == "__main__":
    __author__ = 'zYx.Tom'
    main(__author__)
