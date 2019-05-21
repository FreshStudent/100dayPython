# coding=utf-8
"""

打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

Version: 0.1
Author: lql
date: 2019-05-21
"""
row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ')
        else:
            print('*')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ')
    for _ in range(2 * i + 1):
        print('*')
    print()