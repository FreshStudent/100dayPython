# coding=utf-8
"""
随机数决定干嘛
date:2019-05-17
author:lql

"""
from random import randint

# 用randint在指定范围生成随机数
face = randint(1,6)
if face == 1:
    result = '1'
elif face == 2:
    result = '2'
elif face == 3:
    result = '3'
elif face == 4:
    result = '4'
elif face == 5:
    result = '5'
elif face == 6:
    result = '6'
print(result)
