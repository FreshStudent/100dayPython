# coding=utf-8
"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

Version: 0.1
Date: 2019-05-16
Author: lql
"""

x = float(input('请输入x：'))
if x>1:
    y = 3*x -5
elif x>=-1 and x<=1:
    y = x+2
else:
    y = 5 * x +3
print('f(%.2f)= %.2f' % (x,y))
