# coding=utf-8
"""
IF else 语句
用户身份验证
date：2019-05-16
Author：lql
"""

username = input('请输入用户名：')
password = input('请输入口令：')


if username == 'admin' and password == '123456':
    print('身份验证成功')
else:
    print('身份验证失败')

#output
"""
请输入用户名：'qaasd'
请输入口令：'12312'
身份验证失败
"""