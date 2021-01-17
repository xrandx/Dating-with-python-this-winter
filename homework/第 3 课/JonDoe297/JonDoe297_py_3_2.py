# -*- coding: utf-8 -*-
# @Time    : 2021/1/1111 7:46 PM
# @Author  : agrroc
# @File    : py_3_2.py

# 首先输入一个整数 n ，然后程序连续接受输入 n 个数字，最终程序输出 n 个数字的平均值。
n = int(input())  # 输入一个数
total = 0.0
for i in range(n):  # 连续输入n个数字
    total += float(input())
print(total / n)
