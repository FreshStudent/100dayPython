# coding=utf-8

"""
函数定义
data 2019-05-24
Author lql
"""
def factorial(num):
    """
    求阶乘
    :param num: 非负数
    :return: num的阶乘
    """
    result = 1
    for n in range(1,num+1):
        result *= n
    return result1

m = int(input('m = '))
n = int(input('n = '))

# 当需要计算阶乘的时候不用再写循环求阶乘而是直接调用已经定义好的函数

print(factorial(m) // factorial(n) // factorial(m-n))