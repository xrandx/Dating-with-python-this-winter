#-*- codeing = utf-8 -*-
#@Time : 2021-01-14 19:41
#@Author : 苏苏
#@File : 第五课作业二.py
#@Software : PyCharm


#用递归实现阶乘函数factorial(n)，对于任意的整数n都能返回其对应的阶乘。

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


