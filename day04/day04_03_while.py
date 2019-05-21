# coding=utf-8
"""
猜数字
随机生成大小 1-100
计算机根据人猜的数字分别给出提示大一点、小一点、猜对了

version 0.1
Author lql
date 2019-05-21

"""

import random

answer = random.randint(1,100)
counter = 0
while True:
    counter +=1
    number = int(input('请输入数字:'))
    if number < answer:
        print('大一点')
    elif number == answer:
        print('猜对了')
        break
    else:
        print('小一点')
print('你总共猜了%d次' % (counter))
if(counter>7):
    print('你的智商需要充值！')