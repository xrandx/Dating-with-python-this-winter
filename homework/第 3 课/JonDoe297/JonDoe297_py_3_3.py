# -*- coding: utf-8 -*-
# @Time    : 2021/1/1111 7:52 PM
# @Author  : agrroc
# @File    : py_3_3.py
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[0:n]
