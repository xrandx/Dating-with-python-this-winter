# -*- coding: utf-8 -*-
# @Time    : 2021/1/1212 3:49 PM
# @Author  : agrroc
# @File    : py_5_3.py

# 你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，
# 长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。
#
# 返回的长度需要从小到大排列。

def divingBoard(shorter: int, longer: int, k: int):
    if k == 0:
        return []
    if shorter == longer:
        return [k * shorter]
    else:
        return [(k - i) * shorter + i * longer for i in range(k + 1)]


print(divingBoard(1, 2, 3))
