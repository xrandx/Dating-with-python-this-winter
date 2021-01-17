# -*- coding: utf-8 -*-
# @Time    : 2021/1/1212 3:29 PM
# @Author  : agrroc
# @File    : py_5_1.py

# 定义一个gcd(m, n)函数，
# 该函数可以求出m与n的最大公约数，用辗转相除法递归实现。

def gcd(m, n):
    x = m % n
    if x == 0:
        return n
    else:
        return gcd(m, x)


print(gcd(6, 4))
