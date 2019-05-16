# coding=utf-8
"""
华氏温度转摄氏温度
F = 1.8C + 32

Version：0.1
Author：lql
"""

C = float(input('当前摄氏温度是 C = '))
F = 1.8*C + 32
print('华氏 F = %d' % (F))

f = float(input('当前华氏温度是：'))
c = float((f - 32)/1.8)
print('摄氏 c = %.2f' % (c))