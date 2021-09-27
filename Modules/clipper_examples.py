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
    """
    两个多边形取交
    :param clip:裁剪多边形
    :param subject:主体多边形
    Difference（相剪）时使用 subject 消除 clip 的部分；其他 boolean 操作，两个没有区别
    :return: 返回相交后的结果
    """
    pc = pyclipper.Pyclipper()
    pc.AddPath(clip, pyclipper.PT_CLIP, True)
    pc.AddPath(subject, pyclipper.PT_SUBJECT, True)
    # pc.AddPaths(subject, pyclipper.PT_SUBJECT, True)
    # http://www.angusj.com/delphi/clipper/documentation/Docs/_Body.htm
    # CT=ClipType
    # PFT=PolyFillType
    solution = pc.Execute(pyclipper.CT_INTERSECTION, pyclipper.PFT_EVENODD)
    return solution


def polygon_offset(poly):
    """
    对多边形进行放大或者缩小
    :param poly:
    :param line_width:
    :return:
    """
    pco = pyclipper.PyclipperOffset()
    # JT=JoinType(JT_SQUARE：方形倒角；JT_MITER:设定阈值，方形倒角；JT_ROUND：圆形倒角)
    # 　　jtMiter：对于斜接式交点来说，有必要设定一个阀值，因为偏置的轮廓在极其窄的相交点处可能会造成“尖角”。为了将这些潜在的尖角包含在内，ClippperOffset对象的MiterLimit属性用来制定一个偏置点所能容忍的最大值；对于所有给定的边缘交点处，一旦斜接式交点超过了该阀值，那么方形交角将会被应用；
    # 　　jtRound：当扁平的路径始终无法完美的获取角度信息，他们等价于一系列的圆弧曲线(可以查阅ClipperObject和ArcTolerance属性)
    # 　　jtSquare：相当于斜接式当中的delta值始终为1的情况；
    # ET=EndType
    # 　　　　etClosedPolygon：末点是相交的，并且使用了JoinType来使路径视作一个多边形填充；
    # 　　　　etClosedLine：末点是相交的，并且使用了JoinType来使路径视作一条线进行填充；
    # 　　　　etOpenSqure：末点使用方形尾和扩展的delta角度；
    # 　　　　etOpenRound：末点使用圆形尾和扩展的delta角度；
    # 　　　　etOpenButt：末点使用了方向尾，没有任何扩展；
    pco.AddPath(poly, pyclipper.JT_MITER, pyclipper.ET_CLOSEDPOLYGON)
    return pco.Execute(2)


def main(name):
    print(f'Hi, {name}', datetime.now())

    pass


if __name__ == "__main__":
    __author__ = 'zYx.Tom'
    main(__author__)
