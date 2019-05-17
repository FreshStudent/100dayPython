# coding=utf-8

"""
百分成绩转等级成绩
90分以上    --> A
80分~89分    --> B
70分~79分	   --> C
60分~69分    --> D
60分以下    --> E

Version: 0.1
Author:lql
date: 2019-05-17
"""

score = float(input('请输入成绩：'))
if score<60:
    grade = 'E'
elif score >=60 and score<=69:
    grade = 'D'
elif score >=70 and score<=79:
    grade = 'C'
elif score >=80 and score<=69:
    grade = 'B'
elif score >=90:
    grade = 'A'
print('对应的成绩是:', grade)

