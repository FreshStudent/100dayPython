# coding=utf-8
"""
演示调用不同模块的函数的引用方式

date 2019-05-24
Author lql
version 0.1

"""

from day06_04_module1 import foo

foo()

from day06_04_module2 import foo

foo()


import day06_04_module1 as m1
m1.foo()

import day06_04_module2 as m2
m2.foo()
