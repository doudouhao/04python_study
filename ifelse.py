# -*- coding:utf-8 -*-
# Author:wanghao
# date:2020年5月17日

height = 1.75
weight = 80.5
bmi = weight / (height * height)
# if bmi < 18.5:
#     print("过轻")
# elif   25 > bmi >= 18.5:
#     print("正常")
# elif  28 > bmi >= 25:
#     print("过重")
# elif  32 > bmi >= 28:
#     print("肥胖")
# else:
#     print("严重肥胖")

if 18.5 > bmi:
    print("过轻")
elif 18.5 <= bmi < 25:
    print("正常")
elif 28 > bmi >= 25:
    print("过重")
elif 32 > bmi >= 28:
    print("肥胖")
else:
    print("严重肥胖")
# 条件判断中 大于等于 >= 与 小于等于 <=
