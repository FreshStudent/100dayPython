# coding=utf-8
"""
date 2019-05-24
Author lql
version 0.1

"""

# 在参数名前的* 代表args是一个可变参数
# 即在调用的add函数的时候 可以传入 0 或者多个参数


def add(*args):
    total = 0
    for val in args:
        total +=val
    return total


print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))