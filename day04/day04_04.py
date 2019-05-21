# coding=utf-8
"""
输出 9x9 乘法表

version 0.1
Author lql
date 2019-05-21
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j))
    print()
