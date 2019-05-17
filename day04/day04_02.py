"""
for循环实现100内的偶数求和

version 0.1
author lql

"""

sum = 0
for x in range(0,100,2):
    sum = sum+x
print(sum)

"""
另外一种实现方式
"""
sum = 0
for x in range(0,100):
    if x%2 ==0:
        sum +=x
    print(sum)