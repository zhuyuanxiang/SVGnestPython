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

from Modules.clipper_examples import polygon_offset
from Modules.clipper_examples import two_polygons_intersection

# 被裁剪使用的多边形，的部分会在相减时被放弃掉
subject = (
        ((180, 200), (260, 200), (260, 150), (180, 150)),
        ((215, 160), (230, 190), (200, 190))
)

# 裁剪使用的多边形，即边界
clip1 = ((190, 210), (240, 210), (240, 130), (190, 130))
clip2 = ((240, 210), (190, 210), (190, 130), (240, 130))
clip3 = ((240, 130), (240, 210), (190, 210), (190, 130))


def test_two_polygons_intersection():
    assert two_polygons_intersection(clip1, subject[0]) == [[[240, 200], [190, 200], [190, 150], [240, 150]]]
    assert two_polygons_intersection(clip2, subject[0]) == [[[240, 200], [190, 200], [190, 150], [240, 150]]]
    assert two_polygons_intersection(clip3, subject[0]) == [[[240, 200], [190, 200], [190, 150], [240, 150]]]
    assert two_polygons_intersection(clip1, subject[1]) == [[[230, 190], [200, 190], [215, 160]]]


def test_polygon_offset():
    assert polygon_offset(clip1) == [[[242, 212], [188, 212], [188, 128], [242, 128]]]
    assert polygon_offset(clip2) == [[[242, 212], [188, 212], [188, 128], [242, 128]]]
    assert polygon_offset(clip3) == [[[242, 212], [188, 212], [188, 128], [242, 128]]]


def main(name):
    print(f'Hi, {name}', datetime.now())
    pass


if __name__ == "__main__":
    __author__ = 'zYx.Tom'
    main(__author__)
