# -*- coding: utf-8 -*-
# @Time    : 2021/1/1111 4:40 PM
# @Author  : agrroc
# @File    : py_2_2.py

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['likes', 'dislikes', 'own']
]
# 打印出Google likes Python
print("{0} {1} {2}".format(L[0][1], L[2][0], L[1][1]))  # 用format拼接{}之间用什么都可以