# coding=utf-8
"""
输入半径计算圆的周长和面积


"""

import math

radius = float(input('请输入半径 : '))
C = 2 * math.pi * radius
S = math.pi * radius * radius
print('周长：%.2f' % (C))
print('面积：%.2f' % (S))