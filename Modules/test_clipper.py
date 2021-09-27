# -*- encoding: utf-8 -*-
"""
=================================================
@path   : SVGnestPython -> test_clipper.py
@IDE    : PyCharm
@Author : zYx.Tom, 526614962@qq.com
@Date   : 2021-09-27 17:56
@Version: v0.1
@License: (C)Copyright 2020-2021, zYx.Tom
@Reference:
@Desc   :
==================================================
"""
from datetime import datetime

from Modules.clipper_examples import two_polygons_intersection


def test_two_polygons_intersection():
    # 被裁剪使用的多边形，的部分会在相减时被放弃掉
    subject = (
            ((180, 200), (260, 200), (260, 150), (180, 150)),
            ((215, 160), (230, 190), (200, 190))
    )

    # 裁剪使用的多边形，即边界
    clip = ((190, 210), (240, 210), (240, 130), (190, 130))

    # print(two_polygons_intersection(clip, subject))
    # [
    #         [[240, 200], [190, 200], [190, 150], [240, 150]],
    #         [[200, 190], [230, 190], [215, 160]]
    # ]

    assert two_polygons_intersection(clip, subject[0]) == [[[240, 200], [190, 200], [190, 150], [240, 150]]]
    assert two_polygons_intersection(clip, subject[1]) == [[[230, 190], [200, 190], [215, 160]]]

    def main(name):
        print(f'Hi, {name}', datetime.now())
        pass

    if __name__ == "__main__":
        __author__ = 'zYx.Tom'
        main(__author__)
