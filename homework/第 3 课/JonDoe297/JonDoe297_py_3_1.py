# -*- coding: utf-8 -*-
# @Time    : 2021/1/1111 7:36 PM
# @Author  : agrroc
# @File    : py_3_1.py

# 输入分数 x (0 < x < 100)，程序输出分数对应的等级：x < 60 不及格，60 < x < 80 及格，80 < x < 90 良好，90 < x < 100 优秀。

score = int(input())
if score < 60:
    print("不及格")
elif 60 <= score <= 80:
    print("及格")
elif 80 <= score <= 90:
    print("良好")
elif 90 <= score <= 100:
    print("优秀")
