# -*- coding: utf-8 -*-
# @Time    : 2021/1/1212 3:44 PM
# @Author  : agrroc
# @File    : py_5_2.py

# 用递归实现阶乘函数factorial(n)，
# 对于任意的整数n都能返回其对应的阶乘。

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(6))
