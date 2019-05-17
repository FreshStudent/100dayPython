"""
输入3条边，如果能构成三角形的话就计算周长面积
version：0.1
Author：lql
date：2019-05-17

海伦公式：
p=(a+b+c)/2）
S=sqrt[p(p-a)(p-b)(p-c)]

"""

import math

a = float(input('请输入第1条边：'))
b = float(input('请输入第2条边：'))
c = float(input('请输入第3条边：'))

if a+b>c and a+c>b and b+c>a:
    C = a+b+c
    print('周长是：%.2f' %(C))

    # 海伦公式
    p = C / 2
    S=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('面积是：%.2f' %(S))
else:
    print('不能构成三角形！')